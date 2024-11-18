import json
from xbrain.utils.openai_utils import chat
from xbrain.core.xbrain_tool import run_tool
from xbrain.core import xbrain_tool
from xbrain.utils.import_utils import import_action

# 向openai发送消息，并返回response
def prepare_openai_tools(messages, user_prompt):
    import_action()
    chat_response = chat(messages, tools=[i["model"] for i in xbrain_tool.tools], system_prompt=user_prompt)
    return chat_response

# 如果有工具调用，则执行工具调用，并返回response
def process_chat_response(messages, chat_response):
    if chat_response.content is None:
        messages.append(chat_response)
        tool_res = run_tool(chat_response)
        tool_res_str = "\n".join(map(str, tool_res))
        messages.append({
            "role": "tool",
            "content": tool_res_str,
            "tool_call_id": chat_response.tool_calls[0].id
        })
        res = chat(messages=messages)

    else:
        messages.append({"role": "assistant", "content": chat_response.content})
        res = chat_response
    return res.content

def run(messages, user_prompt=""):
    chat_response = prepare_openai_tools(messages, user_prompt)
    return process_chat_response(messages, chat_response)
