from xbrain import xbrain_tool
from pydantic import BaseModel
import os
from xbrain.context import Type
from xbrain.utils import constant

class XBrainInitAction(BaseModel):
    """init this directory as a xbrain project"""
    pass

@xbrain_tool.Tool(model=XBrainInitAction, hit_condition = {Type.IS_XBRAIN_PROJECT: False})
def init_action():
    """init project"""
    # 检查并创建.xbrain目录
    if not os.path.exists(constant.XBRAIN_DIR):
        os.makedirs(constant.XBRAIN_DIR)
        with open(os.path.join(constant.XBRAIN_DIR, constant.CONFIG_NAME), "w") as file:
            file.write("# XBrain project configuration file\n")  
        print(f"success init xbrain project!")
