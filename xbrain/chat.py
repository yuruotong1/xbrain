from xbrain.utils.import_utils import import_action
from xbrain.utils.openai_utils import chat
from xbrain.xbrain_tool import run_tool, tools


def prepare_openai_tools(messages, user_prompt, chat_model):
    openai_tools = []
    for tool in tools:
        # 如果是 chat 模式，不把内置工具加入到 openai_tools 中
        if chat_model and tool["name"].startswith("XBrain"):
            continue
        else:
            openai_tools.append(tool)
    chat_response = chat(messages, tools=[i["model"] for i in openai_tools], user_prompt=user_prompt)
    return chat_response

def process_chat_response(chat_response):
    if chat_response.content is None:
        res = run_tool(chat_response)
    else:
        res = chat_response.content
    return "\n".join(map(str, res)) if isinstance(res, list) else res

def run(messages, chat_model=True, user_prompt=None):
    if chat_model:
        import_action()
    from xbrain.xbrain_tool import tools
    print(tools)
    chat_response = prepare_openai_tools(messages, user_prompt, chat_model)
    return process_chat_response(chat_response)
