from typing import ClassVar
from pydantic import BaseModel
import sys

from xbrain.core import xbrain_tool
from xbrain.utils.input_util import get_input
from xbrain.utils.openai_utils import text_to_speech


class XBrainExitModel(BaseModel):
    """退出xbrain"""
    description: ClassVar[str] = "退出xbrain"

@xbrain_tool.Tool(model=XBrainExitModel)
def exitAction():
    print(("\nNice to meet you here!"))
    sys.exit(0)