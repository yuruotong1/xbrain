from xbrain.utils.config import Config
from openai import OpenAI


def chat(messages, user_prompt="你是一个智能助手", tools=None, response_format=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    messages = [{"role": "system", "content": user_prompt}] + messages
    res = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        **({"response_format": response_format} if response_format is not None else {}),
        **({"tools": tools} if tools is not None else {}),
      
    )
    return res.choices[0].message

    
def chat_text(user_input_text, user_prompt="你是一个智能助手", tools=None, response_format=None):
    return chat([{"role": "user", "content": user_input_text}], user_prompt, tools, response_format).content