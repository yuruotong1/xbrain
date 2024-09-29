from utils.config import Config
from openai import OpenAI
import openai
from utils.logging_utils import logger


system_prompt = """
## 目标 ##
你是xbrain助手，可以帮助用户完成各种任务，以下是用户的需求：
{prompt_user}
######

## 能力 ##
1. 向用户介绍你的能力，你的能力需要从tool call中获取：

######
"""


def chat(messages, tools=None, user_prompt=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    formatted_prompt = system_prompt.format(
        # prompt_tools=[openai.pydantic_function_tool(tool) for tool in tools], 
        prompt_user=user_prompt
    )
    messages = [{"role": "system", "content": formatted_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        temperature=0.1,
        tools=tools,
    )
    logger.info(f"openai response: {response.choices[0].message}")
    message = response.choices[0].message
    return message
