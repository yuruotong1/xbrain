from typing import ClassVar
from pydantic import BaseModel

from xbrain.core import xbrain_tool
from xbrain.utils.input_util import get_input
from xbrain.utils.openai_utils import text_to_speech


class XBrainTextToSpeechModel(BaseModel):
    """文字转语音"""
    description: ClassVar[str] = "文字转语音"

@xbrain_tool.Tool(model=XBrainTextToSpeechModel)
def textToSpeechAction():
    text = get_input("请输入要转换的文字")
    text_to_speech(text)