import os
from pathlib import Path
from xbrain.utils.config import Config
from openai import OpenAI
import openai
import base64
from pathlib import Path

def chat(messages, user_prompt="你是一个智能助手", tools=None, response_format=None):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY)
    messages = [{"role": "system", "content": user_prompt}] + messages
    response = client.beta.chat.completions.parse(
        model=config.OPENAI_MODEL,
        messages=messages,
        **({"response_format": response_format} if response_format is not None else {}),
        **({"tools": [openai.pydantic_function_tool(tool) for tool in tools] if tools else None} if tools else {}),
    )
    return response.choices[0].message.content

def chat_text(user_input_text, user_prompt="你是一个智能助手", tools=None, response_format=None):
    return chat([{"role": "user", "content": user_input_text}], user_prompt, tools, response_format)

def chat_image(user_input_text, image_path, user_prompt="你是一个智能助手", tools=None, response_format=None):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        data_url = f"data:image/jpeg;base64,{base64_image}"
        messages = [{"role": "user", "content": [{"type": "text", "text": user_input_text}, {"type": "image_url", "image_url": {"url": data_url}}]}] 
        return chat(messages, user_prompt, tools, response_format)

def chat_video(user_input_text, video_path, user_prompt="你是一个智能助手", tools=None, response_format=None):
    with open(video_path, "rb") as video_file:
        base64_video = base64.b64encode(video_file.read()).decode('utf-8')
        data_url = f"data:video/mp4;base64,{base64_video}"
        return chat([{"role": "user", "content": 
        [{"type": "text", "text": user_input_text}, 
        {"type": "video_url", "video_url": {"url": data_url}}]}], 
        user_prompt, tools, response_format)


def text_to_speech(text: str):
    config = Config()
    client = OpenAI(base_url=config.OPENAI_BASE_URL, api_key=config.OPENAI_API_KEY, timeout=999)
    with client.audio.speech.with_streaming_response.create(
    model="tts-1-hd-1106",
    voice="echo",
    input=text
    )as response:
        response.stream_to_file(os.path.join(Path.cwd(), "speech.mp3"))

