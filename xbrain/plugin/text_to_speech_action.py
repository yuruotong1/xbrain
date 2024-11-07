from typing import ClassVar
from pydantic import BaseModel, Field

from xbrain.core import xbrain_tool
from xbrain.utils.input_util import get_input
from xbrain.utils.openai_utils import text_to_speech


class XBrainTextToSpeechModel(BaseModel):
    """文字转语音"""
    description: ClassVar[str] = "文字转语音"
    text: str = Field(description="要转换的文字")

@xbrain_tool.Tool(model=XBrainTextToSpeechModel)
def textToSpeechAction(text: str):
    text_to_speech(text)