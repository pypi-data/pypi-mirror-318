from pathlib import Path
import yaml
from yaml.nodes import ScalarNode
from yaml.loader import SafeLoader
from typing import Any

from .tool import APISpec

import pdb

class LoadedFromFile(str):
    """Marker class for content loaded from files so that only unloaded text from the original yaml is interpolated."""


class YAMLFileLoader(SafeLoader):
    """Custom YAML loader with support for !load tags for loading file contents."""
    
    def __init__(self, stream):
        super().__init__(stream)
        # Store the yaml file's directory for relative paths
        self._yaml_dir = Path(stream.name).parent if hasattr(stream, 'name') else Path.cwd()

    def load_file_content(self, node: ScalarNode) -> LoadedFromFile:
        """Load content from a file specified in a !load tag."""
        path = Path(self.construct_scalar(node))
        full_path = self._yaml_dir / path
        
        if not full_path.exists():
            raise FileNotFoundError(f"File not found: {full_path}")
            
        return LoadedFromFile(full_path.read_text(encoding='utf-8'))

# Register the !load constructor
YAMLFileLoader.add_constructor('!load', YAMLFileLoader.load_file_content)


def interpolate_strings(data: Any, context: dict) -> Any:
    """Recursively interpolate strings in the data structure using the context."""
    
    # recurse into dicts and lists
    if isinstance(data, dict):
        return {k: interpolate_strings(v, context) for k, v in data.items()}
    elif isinstance(data, list):
        return [interpolate_strings(item, context) for item in data]
    
    # strings that are not LoadedFromFile are interpolated
    elif isinstance(data, str) and not isinstance(data, LoadedFromFile):
        try:
            return data.format_map(context)
        except (KeyError, ValueError):
            # Return original string if interpolation fails. issue a warning.
            # TODO: integrate this into the logger
            print(f"Warning: Failed to interpolate string: {data}")
            return data
    
    # strings that are LoadedFromFile are converted back to strings
    elif isinstance(data, LoadedFromFile):
        return str(data)
    
    # everything else is returned as is
    return data



def load_interpolated_yaml(path: Path) -> dict:
    """
    Load a YAML file, replace !load tags, and perform string interpolation.
    For example, say I have the following text file:
    
    ```text
    This is the content of template.txt
    ```
    
    And the following yaml file:
    ```yaml
    name: my_api
    description: This is {name}
    template: !load template.txt
    message: | 
      This uses loaded content: {template}
    ```

    Loading this yaml file will result in the following dictionary:
    ```python
    {
        'name': 'my_api',
        'description': 'This is my_api',
        'template': 'This is the content of template.txt',
        'message': 'This uses loaded content: This is the content of template.txt'
    }
    ```
    """    
    with path.open(encoding='utf-8') as f:
        data = yaml.load(f, YAMLFileLoader)
    
    return interpolate_strings(data, data)




def load_yaml_api(path: Path) -> APISpec:
    """
    Load an API definition from a YAML file.
    API files should have the following structure:
        ```yaml
        name: <name>
        cache_key: <cache_key> # Optional - if not provided, caching will be disabled
        description: <description>
        documentation: <documentation>
        model_override: # Optional - if not provided, uses the model specified when creating the AdhocApi instance.
            provider: <provider>
            model: <model>
        ```
    
    Additionally, content from a file can be automatically loaded via the !load tag:
    ```yaml
    name: some_api
    description: some description of the API
    documentation: !load documentation.md
    ```
    This will load the contents of `documentation.md` and insert is under the `documentation` field.

    Lastly, you can interpolate values from the yaml in the string. For example:
    ```yaml
    name: some_api
    description: some description of the API
    documentation: |
        This API is called '{name}'
        Also, we can interpolate content from files.
        for example, {loaded_from_a_file}
    loaded_from_a_file: !load some_file.txt
    ```
    The `{name}` field in documentation will be replaced with the value of `name` in the yaml file.
    The `{some_extra_field}` field will be replaced with the contents of `some_file.txt`,
    which is then interpolated into the `documentation` field.

    Note: extra fields in the yaml file will not be included in the APISpec.
    This may be useful for collecting content from files or interoperating with other sources.

    Args:
        path (Path): The path to the YAML file containing the API definition.

    Returns:
        APISpec: The API definition.
    """
    raw_spec = load_interpolated_yaml(path)
    # collect only the fields that are relevant for APISpec
    spec = {k: v for k, v in raw_spec.items() if k in APISpec.__annotations__}
    
    # validate that the required fields are present
    # TODO: would be nice if validation could be more automated based on the APISpec class
    required_fields = {'name', 'description', 'documentation'}
    missing_fields = required_fields - set(spec.keys())
    if missing_fields:
        raise ValueError(f"API definition is missing required fields: {missing_fields}")
    
    # create the APISpec
    return APISpec(**spec)



def load_multiple_apis(path: Path) -> list[APISpec]:
    """TBD what format would be best for multiple APIs"""



if __name__ == '__main__':
    here = Path(__file__).parent
    path = here / '../examples/gdc/api.yaml'
    # res = load_interpolated_yaml(path)
    api = load_yaml_api(path)
    pdb.set_trace()
    ...