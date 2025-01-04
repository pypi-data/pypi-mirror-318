from archytas.tool_utils import tool
from typing import Callable, Any, TypedDict, Literal, overload
from typing_extensions import Annotated, NotRequired
from functools import cache

from .utils import Logger, SimpleLogger, get_code, set_openai_api_key, set_gemini_api_key, set_anthropic_api_key
from .uaii import UAII, GeminiModel, GeminiAgent, OpenAIModel, OpenAIAgent, ClaudeModel, ClaudeAgent


import pdb


# configuration for agents that the user passes in
class GeminiConfig(TypedDict):
    provider: Literal['google']
    api_key: NotRequired[Annotated[str, 'The API key for the Gemini API']]
    model: Annotated[GeminiModel, 'The model to use for the Gemini API']
    ttl_seconds: NotRequired[Annotated[int, "The time-to-live in seconds for the Gemini API cache"]]
GEMINI_DEFAULTS = {
    'ttl_seconds': 1800
}


class GPTConfig(TypedDict):
    provider: Literal['openai']
    api_key: NotRequired[Annotated[str, 'The API key for the OpenAI API']]
    model: Annotated[OpenAIModel, 'The model to use for the OpenAI API']
GPT_DEFAULTS = {}


class ClaudeConfig(TypedDict):
    provider: Literal['anthropic']
    api_key: NotRequired[Annotated[str, 'The API key for the Anthropic API']]
    model: Annotated[ClaudeModel, 'The model to use for the Anthropic API']
CLAUDE_DEFAULTS = {}

DrafterConfig = GeminiConfig | GPTConfig | ClaudeConfig

def validate_config(config: DrafterConfig):
    """
    Validate a configuration for a drafter agent.

    Args:
        config (DrafterConfig): The configuration to validate
    """
    if config['provider'] == 'google':
        config_type = GeminiConfig
    elif config['provider'] == 'openai':
        config_type = GPTConfig
    elif config['provider'] == 'anthropic':
        config_type = ClaudeConfig
    else:
        raise ValueError(f'Unknown provider "{config["provider"]}"')

    config_keys = set(config.keys())
    allowed_keys = set(config_type.__annotations__.keys())
    if not config_keys.issubset(allowed_keys):
        raise ValueError(f'Invalid {config_type.__name__} keys {config_keys - allowed_keys} for drafter config {config}')


def set_api_key(config: DrafterConfig):
    """
    Set the API key given a model configuration.

    Args:
        config (DrafterConfig): The configuration for the model
    """
    provider = config['provider']
    if provider == 'google':      set_gemini_api_key(config.get('api_key', None))
    elif provider == 'openai':    set_openai_api_key(config.get('api_key', None))
    elif provider == 'anthropic': set_anthropic_api_key(config.get('api_key', None))
    else:
        raise ValueError(f'Unknown provider "{provider}"')


class APISpec(TypedDict):
    name: Annotated[str, 'The name of the API']
    cache_key: NotRequired[Annotated[str, 'The key used to retrieve the cached API chat. If not provided, caching will be disabled. Note: only Gemini supports caching at the moment.']]
    description: Annotated[str, 'A description of the API']
    documentation: Annotated[str, "The raw extracted text of the API's documentation"]
    model_override: NotRequired[Annotated[DrafterConfig, 'Explicit AI model to use for this API. If not provided, uses the normal model specified when creating the AdhocApi instance.']]


def validate_api_spec(spec: APISpec):
    """
    Validate an API specification by checking if it has any keys it shouldn't.

    Args:
        spec (APISpec): The API specification to validate
    """
    allowed_keys = set(APISpec.__annotations__.keys())
    spec_keys = set(spec.keys())
    if not spec_keys.issubset(allowed_keys):
        truncates_spec = {**spec, 'documentation': '<documentation omitted>'}
        raise ValueError(f'Invalid keys {spec_keys - allowed_keys} for API spec {truncates_spec}')


def count_api_tokens_for_model(spec: APISpec, config: DrafterConfig) -> tuple[int,int]:
    """
    Count how many tokens the given API spec takes up in the context window of the given model.

    Args:
        spec (APISpec): The API specification
        config (DrafterConfig): The configuration for the model
        threshold (float, optional): The fraction of the context window that the API documentation should be less than. Defaults to 0.7.

    Returns:
        tuple[int,int]: The number of tokens in the API documentation and the context window size
    """
    if config['provider'] == 'google':
        model = GeminiAgent(model=config['model'], cache_key=None, system_prompt='', cache_content='', ttl_seconds=0)
    elif config['provider'] == 'openai':
        model = OpenAIAgent(model=config['model'], system_prompt='')
    elif config['provider'] == 'anthropic':
        model = ClaudeAgent(model=config['model'], cache=False, system_prompt='')
    else:
        raise ValueError(f'Unknown provider "{config["provider"]}"')

    return model.count_tokens(DRAFTER_SYSTEM_PROMPT + spec['documentation']), model.get_context_window_size()



def select_best_model_for_api(spec: APISpec, configs: list[DrafterConfig], threshold: float=0.7) -> DrafterConfig:
    """
    Select the first suitable model for an API from a list of models.
    If a model_override is provided by the API spec, that will be used without checking.

    Args:
        spec (APISpec): The API specification
        configs (list[DrafterConfig]): A list of configurations for possible models
    """
    # if the user has explicitly specified a model for this API, use that
    if 'model_override' in spec:
        return spec['model_override']

    # find the first model that has a long enough context window for this API
    tries: dict[str, tuple[int, int]] = {}
    for config in configs:
        token_count, window_size = count_api_tokens_for_model(spec, config)
        if token_count < threshold * window_size:
            return config
        tries[config['model']] = (token_count, window_size)

    # error
    avg_token_count = int(sum(token_count for (token_count, _) in tries.values()) / len(tries))
    model_window_sizes = {model: f'{window_size:,} tokens' for model, (_, window_size) in tries.items()}
    min_window_size = int(avg_token_count / threshold)
    raise ValueError(f'No suitable model found for API "{spec["name"]}". Api length: ~{avg_token_count:,} tokens, while provided models support: {model_window_sizes}. Minimum window size (with {1-threshold:.0%} margin) is ~{min_window_size:,} tokens')

DRAFTER_SYSTEM_PROMPT = '''\
You are an assistant who is helping users to write code to interact with the {name} API.
You will be provided with the raw API documentation, and you have 2 jobs:
1. Answer questions about the API
2. Write code to perform specific tasks using the API

Each user query will include a keyword specifying which job to do: ASK_API for 1, and WRITE_CODE for 2.

When answering questions (ASK_API), please follow these rules:
- Answer in plain English
- Be concise and comprehensive
- Do not write large code blocks. If you need to provide code, keep it short and inline with the text of your response

When drafting code (WRITE_CODE), please follow these rules:
- Your output should be a single python code block. do not include any other comments or explanations in your response.
- Your code should directly solve the problem posed in the query and nothing more.
- The code should be ready to run directly as a python script.
- Assume `requests`, `numpy`, and `pandas` are installed, as well as any API specific libraries mentioned in the API documentation.
'''


def make_ask_api_query(query: str) -> str:
    return f'ASK_API: {query}'

def make_write_code_query(query: str) -> str:
    return f'WRITE_CODE: {query}'



class AdhocApi:
    """
    Toolset for interacting with external APIs in an flexible manner. 
    These tools can be used to draft code that perform requests to APIs given some goal in plain English.
    Common usage is to first list APIs to determine which to use, then draft code to perform a specific task, then run the code.
    Note that each API maintains a separate chat history, so treat each API as a separate conversation.
    """
    def __init__(self, *,
        apis: list[APISpec],
        drafter_config: DrafterConfig | list[DrafterConfig],
        logger: Logger=SimpleLogger()
    ):
        """
        Create a new AdhocApi instance.

        Args:
            apis (list[APISpec]): A list of APIs available to the tool
            drafter_config (DrafterConfig | list[DrafterConfig]): The base configuration for the drafter agent.
                If a list is provided, for each API we will automatically pick the first model from the list
                that has a long enough context window for that API.
            logger (Logger, optional): A logger to use for logging. Defaults to SimpleLogger.
        """
        self.apis: dict[str, tuple[APISpec, DrafterConfig]] = {}
        self.logger = logger

        # validate the drafter configs and set the API keys
        if not isinstance(drafter_config, list): drafter_config = [drafter_config]
        for config in drafter_config:
            validate_config(config)
            set_api_key(config)

        # validate the API specs and select the best model for each API
        for api in apis:
            validate_api_spec(api)
            config = select_best_model_for_api(api, drafter_config)
            self.apis[api['name']] = (api, config)
            self.logger.info({'api': api['name'], 'selected model': config['model']})


    def _get_api(self, api: str) -> tuple[APISpec, DrafterConfig]:
        """
        Get the API and model specs for the given API.

        Args:
            api (str): The name of the API to get the specs for

        Returns:
            tuple[APISpec, DrafterConfig]: The API and model specs
        """
        specs = self.apis.get(api)
        if specs is None:
            raise ValueError(f'API {api} not found. Please consult the list of available APIs: {[*self.apis.keys()]}')
        return specs

    @cache
    def _get_agent(self, api: str) -> UAII:
        """
        get the agent instance for the given API (make a new one if it doesn't exist)

        Args:
            api (str): The name of the API to get the agent for

        Returns:
            UAII: The agent instance
        """
        # @cache handles the case where the agent already exists

        # create a new agent if it doesn't exist
        api_spec, drafter_config = self._get_api(api)
        api_docs = api_spec['documentation']
        provider = drafter_config['provider']

        if provider == 'google':
            config: GeminiConfig = {**GEMINI_DEFAULTS, **drafter_config}
            return GeminiAgent(
                model=config['model'],
                cache_key=api_spec.get('cache_key', None),
                system_prompt=DRAFTER_SYSTEM_PROMPT.format(name=api),
                cache_content=api_docs,
                ttl_seconds=config['ttl_seconds'],
                logger=self.logger,
            )

        elif provider == 'openai':
            config: GPTConfig = {**GPT_DEFAULTS, **drafter_config}
            return OpenAIAgent(
                model=config['model'],
                system_prompt=DRAFTER_SYSTEM_PROMPT.format(name=api) + f'\n\n# API Documentation:\n{api_docs}',
            )

        elif provider == 'anthropic':
            config: ClaudeConfig = {**CLAUDE_DEFAULTS, **drafter_config}
            return ClaudeAgent(
                model=config['model'],
                cache=bool(api_spec.get('cache_key', None)),
                system_prompt=DRAFTER_SYSTEM_PROMPT + f'\n\n# API Documentation:\n{api_docs}',
            )

        else:
            raise ValueError(f'Unknown provider {provider}')

    @tool
    def list_apis(self) -> dict:
        """
        This tool lists all the APIs available to you.

        Returns:
            dict: A dict mapping from API names to their descriptions
        """
        return {
            name: {'description': api['description']}
            for name, (api, _) in self.apis.items()
        }

    @tool
    def ask_api(self, api: str, query: str) -> str:
        """
        Ask a question about the API to get more information.

        Args:
            api (str): The name of the API to ask about
            query (str): The question to ask

        Returns:
            str: The response to the query
        """
        self.logger.info({'api': api, 'ASK_API': query})
        agent = self._get_agent(api)
        query = make_ask_api_query(query)
        return agent.message(query)

    @tool
    def use_api(self, api: str, goal: str) -> str:
        """
        Draft python code for an API request given some goal in plain English.

        Args:
            api (str): The name of the API to use
            goal (str): The task to be performed by the API request (in plain English)

        Returns:
            str: The raw generated code to perform the task
        """
        self.logger.info({'api': api, 'WRITE_CODE': goal})
        agent = self._get_agent(api)
        query = make_write_code_query(goal)
        response = agent.message(query)

        # strip off any markdown syntax
        code = get_code(response)

        return code



# factory for making individual tools per API
# class AdhocApiFactory:
#     def __init__(self, api: APISpec, drafter_config: GeminiConfig | GPTConfig | ClaudeConfig):
#         self.api = api
#         self.drafter_config = drafter_config
#         self._set_api_key()




import subprocess
import tempfile
import os

class PythonTool:
    """Tool for running python code. If the user asks you to write code, you can run it here."""
    def __init__(self, sideeffect:Callable[[str, str, str, int], Any]=lambda x: None):
        """
        Set up a PythonTool instance.

        Args:
            sideeffect (Callable[[str], Any], optional): A side effect function to run when the tool is used. Defaults to do nothing.
        """
        self.sideeffect = sideeffect

    @tool
    def run(self, code: str) -> tuple[str, str, int]:
        """
        Runs python code in a python subprocess.

        The environment is not persistent between runs, so any variables created will not be available in subsequent runs.
        The only visible effects of this tool are from output to stdout/stderr. If you want to view a result, you MUST print it.

        Args:
            code (str): The code to run

        Returns:
            tuple: The stdout, stderr, and returncode from executing the code
        """

        # make a temporary file to run the code
        with tempfile.NamedTemporaryFile(suffix='.py', mode='w+') as f:
            f.write(code)
            f.flush()
            f.seek(0)

            # run the file in a separate Python process and capture the output
            try:
                result = subprocess.run(['python', f.name], capture_output=True, text=True, cwd=os.getcwd())
                stdout = result.stdout
                stderr = result.stderr or (f'No error output available. Process returned non-zero error code {result.returncode}' if result.returncode != 0 else '')
                returncode = result.returncode
            except Exception as e:
                stdout, stderr, returncode = "", str(e), 1
        
        # perform side effect
        self.sideeffect(code, stdout, stderr, returncode)


        return stdout, stderr, returncode


from .files import tree
from pathlib import Path

@tool
def view_filesystem(max_depth:int=-1, max_similar: int=25, ignore: list[str] = []) -> str:
    """
    View files and directories in the current working directory, displayed in a tree structure.

    Args:
        max_depth (int, optional): The maximum depth to traverse. Set to negative for infinite depth.
        max_similar (int, optional): The maximum number of similar files to display. When too many similar files are found, further matches will be elided. Defaults to 25.
        ignore (list, optional): List of unix filename pattern strings (e.g. '*.py', 'file?.txt', 'file[!a-c]*.txt', etc.) to skip including in output. Defaults to [].

    Returns:
        str: A string representation of the tree structure of the current working directory.
    """
    return tree(Path('.'), ignore=ignore, max_depth=max_depth, max_similar=max_similar)