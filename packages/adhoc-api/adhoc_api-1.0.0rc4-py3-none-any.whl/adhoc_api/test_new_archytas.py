if __name__ == '__main__':
    from adhoc_api.uaii import GeminiAgent, ClaudeAgent, OpenAIAgent
    import pdb
    
    # # Test token counting
    # g_agent = GeminiAgent(model='gemini-1.5-pro-001', system_prompt='This is a test system prompt', cache_key=None, cache_content='', ttl_seconds=3600)
    # print(g_agent.count_tokens('This is a test message'))

    c_agent = ClaudeAgent(model='claude-3-5-sonnet-latest')
    print(c_agent.count_tokens('This is a test message'))

    o_agent = OpenAIAgent(model='gpt-4o', system_prompt='This is a test system prompt')
    print(o_agent.count_tokens('This is a test message'))
    # pdb.set_trace()


# from adhoc_api.tool import view_filesystem
# from archytas.react import ReActAgent, FailedTaskError
# from easyrepl import REPL
# import pdb
# from archytas.tool_utils import get_tool_prompt_description

# def get_agent_tool_prompts(agent) -> str:
#     parts = []
#     for toolname, tool in agent.tools.items():
#         parts.append(get_tool_prompt_description(tool))

#     return "\n\n".join(parts)

# def main():
#     tools = [view_filesystem]
#     agent = ReActAgent(model='gpt-4o', tools=tools, verbose=True)

#     print(agent.prompt, '\n\ntool prompts:\n\n')
#     print(get_agent_tool_prompts(agent))
#     pdb.set_trace()
#     for query in REPL(history_file='.chat'):
#         try:
#             answer = agent.react(query)
#             print(answer)
#         except FailedTaskError as e:
#             print(f"Error: {e}")
#         except KeyboardInterrupt:
#             agent.add_context(f'User issued KeyboardInterrupt')
#             print("KeyboardInterrupt")



# if __name__ == "__main__":
#     main()