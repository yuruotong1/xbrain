# 记录当前用户操作的上下文，用于提供实时建议
from enum import Enum
import os

from xbrain.utils import constant
class Type(Enum):
    CURRENT_PATH = "current_path"
    PRE_ACTIONS = "pre_actions"
    CURRENT_FILE_PATH = "current_file"
    CURRENT_FILE_CONTENT = "current_file_content"
    IS_XBRAIN_PROJECT = "is_xbrain_project"


context = {
            Type.CURRENT_PATH: "",
            Type.PRE_ACTIONS: [],
            Type.CURRENT_FILE_PATH: "",
            Type.CURRENT_FILE_CONTENT: "",
            Type.IS_XBRAIN_PROJECT: False
        }

class ActionRecord:
    def __init__(self, name, context):
        self.name = name
        self.context = context

