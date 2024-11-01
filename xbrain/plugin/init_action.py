from xbrain.core import xbrain_tool
from pydantic import BaseModel
from typing import ClassVar
import os
from xbrain.core.context import Type
from xbrain.utils.config import Constants
from typing import ClassVar
from xbrain.utils.translations import _

class XBrainInitAction(BaseModel):
    """init this directory as a xbrain project"""
    description: ClassVar[str] = _("init this directory as a xbrain project")
    pass

@xbrain_tool.Tool(model=XBrainInitAction, hit_condition = {Type.IS_XBRAIN_PROJECT: False})
def init_action():
    """init project"""
    # 检查并创建.xbrain目录
    constants = Constants()
    if not os.path.exists(constants.XBRAIN_DIR):
        os.makedirs(constants.XBRAIN_DIR)
        with open(os.path.join(constants.XBRAIN_DIR, constants.CONFIG_NAME), "w") as file:
            file.write("# XBrain project configuration file\n")  
        print(_("success init xbrain project!"))
