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
    if not os.path.exists(constant.CONFIG_NAME):
        with open(constant.CONFIG_NAME, "w") as file:
            file.write("# XBrain project configuration file\n")
    print(f"success init xbrain project!")

