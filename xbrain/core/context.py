# 记录当前用户操作的上下文，用于提供实时建议
from enum import Enum
import os
from xbrain.utils.config import Constants

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

# 判断是否命中条件
def is_hit(hit_condition):
    if hit_condition is None:
        return True
    for condition in hit_condition:
        if context[condition] != hit_condition[condition]:
            return False
    return True

class ActionRecord:
    def __init__(self, name, params):
        self.name = name
        self.params = params

def update_context():
    constants = Constants()
    context[Type.CURRENT_PATH] = os.getcwd()
    context[Type.IS_XBRAIN_PROJECT] = os.path.exists(constants.XBRAIN_DIR)
