from utils.config import Config
from openai import OpenAI
import openai
from utils.logging_utils import logger


system_prompt = """
{prompt_user}

## 上下文 ##
1. 如果用户提到当前文件/当前代码，则指以下内容为当前文件内容作为上下文；
######
"""


def chat(messages, tools=None, user_prompt=None, response_format=None):
    if tools is None:
        tools = []
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    formatted_prompt = system_prompt.format(
        prompt_user=user_prompt
    )
    messages = [{"role": "system", "content": formatted_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        temperature=0.1,
        **({"response_format": response_format} if response_format is not None else {}),
        tools=[openai.pydantic_function_tool(tool) for tool in tools],
    )
    logger.info(f"openai response: {response.choices[0].message}")
    message = response.choices[0].message
    return message
