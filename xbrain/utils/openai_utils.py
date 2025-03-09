import os
from pathlib import Path
from pydantic import Field
from xbrain.utils.config import Config
from pydantic import BaseModel
from openai import OpenAI
import openai

from xbrain.utils.input_util import get_input

def chat(messages, tools=None, 
         user_prompt="You are a helpful assistant", response_format=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    messages = [{"role": "system", "content": user_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        **({"response_format": response_format} if response_format is not None else {}),
        **({"tools": [openai.pydantic_function_tool(tool) for tool in tools] if tools else None} if tools else {}),
    )
    return response.choices[0].message

def stream_chat(messages, 
         user_prompt="You are a helpful assistant"):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    messages = [{"role": "system", "content": user_prompt}] + messages
    response = client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=messages,
        stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content

def text_to_speech(text: str):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY, timeout=999)
    with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd-1106",
    voice="echo",
    input=text
    )as response:
        response.stream_to_file(os.path.join(Path.cwd(), "speech.mp3"))



# 与用户进行多轮对话，直到没有问题为止
def multiple_rounds_chat(is_complete_description, content_description, question_description, system_prompt, messages=[], tools=None):
    class MultiChatModel(BaseModel):
        is_complete: bool = Field(description=is_complete_description)
        content: str = Field(description=content_description)
        question: str = Field(description=question_description)
    
    if messages:
        messages.append({"role": "user", "content": get_input(messages[0]["content"])})
    
    while True:
        res = chat(messages, tools, system_prompt, MultiChatModel)
        if res.parsed.is_complete:
            return res.parsed.content
        else:
            messages.append({"role": "assistant", "content": res.parsed.content})
            user_input = get_input(res.parsed.question)
            messages.append({"role": "user", "content": user_input})