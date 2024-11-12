from typing import ClassVar
from pydantic import BaseModel, Field

from xbrain.core import xbrain_tool
from xbrain.utils.input_util import get_input
from xbrain.utils.openai_utils import text_to_image


class XBrainTextToImageModel(BaseModel):
    """文字转图片"""
    description: ClassVar[str] = "文字转图片"
    text: str = Field(description="要转换的文字")

@xbrain_tool.Tool(model=XBrainTextToImageModel)
def textToImageAction(text: str):
    text_to_image(text)