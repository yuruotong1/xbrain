from xbrain.utils.openai_utils import chat
from xbrain.core.xbrain_tool import run_tool
from xbrain.core.xbrain_tool import tools


def prepare_openai_tools(messages, user_prompt):
    chat_response = chat(messages, tools=[i["model"] for i in tools], system_prompt=user_prompt)
    return chat_response

def process_chat_response(chat_response):
    if chat_response.content is None:
        tool_res = run_tool(chat_response)
        tool_res_str = "\n".join(map(str, tool_res))
        chat_response = chat(messages=[{"role": "assistant", "content": tool_res_str}], tools=None, system_prompt="总结一下工具的输出")
    return chat_response.content

def run(messages, user_prompt=""):
    chat_response = prepare_openai_tools(messages, user_prompt)
    return process_chat_response(chat_response)
