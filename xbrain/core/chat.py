from xbrain.utils.import_utils import import_action
from xbrain.utils.openai_utils import chat
from xbrain.core.xbrain_tool import run_tool
import xbrain.core.xbrain_tool as xb_tool


def prepare_openai_tools(messages, user_prompt, chat_mode):
    openai_tools = []
    for tool in xb_tool.tools:
        # 如果是 chat 模式，不把内置工具加入到 openai_tools 中
        if chat_mode and tool["name"].startswith("XBrain"):
            continue
        else:
            openai_tools.append(tool)
    chat_response = chat(messages, tools=[i["model"] for i in openai_tools], system_prompt=user_prompt)
    return chat_response

def process_chat_response(chat_response):
    if chat_response.content is None:
        tool_res = run_tool(chat_response)
        tool_res_str = "\n".join(map(str, tool_res))
        chat_response = chat(messages=[{"role": "assistant", "content": tool_res_str}], tools=None, system_prompt="总结一下工具的输出")
    return chat_response.content

def run(messages, chat_mode=True, user_prompt=""):
    if chat_mode: # chat mode 到底是指什么
        import_action()
    chat_response = prepare_openai_tools(messages, user_prompt, chat_mode)
    return process_chat_response(chat_response)
