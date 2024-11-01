import gradio as gr
import os
import time
import logging
from pydantic import BaseModel, Field
from typing import ClassVar, Optional, List
from xbrain.utils.translations import _
from xbrain.core.chat import run
from xbrain.core import xbrain_tool

logger = logging.getLogger(__name__)

class XBrainDemo(BaseModel):
    '''Start a Gradio demo'''
    description: ClassVar[str] = _("Start a Gradio demo")

    user_prompt: Optional[str] = Field(
        description="The system prompt for this demo, basically what this agent is made for."
    )
    
@xbrain_tool.Tool(model=XBrainDemo)
def gradio_demo(user_prompt: Optional[str] = None):    
    if user_prompt is None:
        user_prompt = "You are xbrain, an AI Agent Framework"
    
    logger.info(f"调用工具时的入参: {user_prompt}")

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox()
        file_upload = gr.File(label="Upload a file")  
        clear = gr.Button("Clear")

        def user(user_message, history: list, uploaded_file=None):
            history = history + [{"role": "user", "content": user_message}]
            if uploaded_file is not None:
                file_path = uploaded_file.name
                history[-1]["content"] += f" {file_path}"
                logger.info(history[-1])
            return "", history

        def bot(history: list):
            bot_message = run(messages=history, user_prompt=user_prompt, chat_mode=False)
            history.append({"role": "assistant", "content": ""})
            for character in bot_message:
                history[-1]['content'] += character
                time.sleep(0.05)
                yield history

        msg.submit(user, [msg, chatbot, file_upload], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)

    demo.launch()