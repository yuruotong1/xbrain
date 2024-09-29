from config import Config
from openai import OpenAI
from utils.logging_utils import logger

def chat(messages, response_format=None, tools=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    response =  client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        response_format=response_format,
        temperature=0.1,
        tools=tools
    )
    logger.info(f"openai response: {response.choices[0].message}")
    message = response.choices[0].message
    return message
