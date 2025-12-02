import os
from pathlib import Path
from xbrain.utils.config import Config
from openai import OpenAI
import openai

def chat(messages, user_prompt, tools=None, response_format=None):
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


def text_to_speech(text: str):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY, timeout=999)
    with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd-1106",
    voice="echo",
    input=text
    )as response:
        response.stream_to_file(os.path.join(Path.cwd(), "speech.mp3"))

