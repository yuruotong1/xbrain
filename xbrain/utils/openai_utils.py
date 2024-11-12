import json
import os
from pathlib import Path
from pydantic import Field
import requests
from xbrain.utils.config import Config
from pydantic import BaseModel
from openai import OpenAI
import openai

from xbrain.utils.input_util import get_input


system_prompt = """
{prompt_user}
"""
config = Config()
client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)


def chat(messages, tools=None, 
         system_prompt="You are a helpful assistant", response_format=None):
    formatted_prompt = system_prompt.format(
        prompt_user=system_prompt
    )
    messages = [{"role": "system", "content": formatted_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        temperature=0.1,
        **({"response_format": response_format} if response_format is not None else {}),
        **({"tools": [openai.pydantic_function_tool(tool) for tool in tools] if tools else None} if tools else {}),
    )
    message = response.choices[0].message
    return message

def text_to_speech(text: str):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY, timeout=999)
    with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd-1106",
    voice="echo",
    input=text
    )as response:
        response.stream_to_file(os.path.join(Path.cwd(), "speech.mp3"))


def text_to_image(text: str):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY, timeout=999)

    with client.images.with_streaming_response.generate(prompt=text, model="dall-e-3", n=1, size="1024x1024") as response:
        json_content = json.loads(response.read().decode('utf-8'))
        image_data = requests.get(json_content['data'][0]['url']).content
        with open("image.webp", "wb") as file:
            file.write(image_data)


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
    

def generate_embedding(text):
    """Generate embeddings for the given text."""
    response = client.embeddings.create(input=text, model="text-embedding-ada-002")
    embedding = response.data[0].embedding
    return embedding
