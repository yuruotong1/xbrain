import os
from xbrain import xbrain_tool
from pydantic import BaseModel
from typing import ClassVar
from xbrain.command import init_action
from xbrain.utils.input_util import get_input
from xbrain.utils.translations import _
class XBrainChangeWorkspaceAction(BaseModel):
    """change workspace"""
    description: ClassVar[str] = _("change workspace")
    pass

@xbrain_tool.Tool(model=XBrainChangeWorkspaceAction)
def change_workspace_action():
    path = get_input(_("please input the workspace path"))
    if path:
        os.chdir(path)
        print(_("\033[;32mcurrent workspace: {cwd}\033[0m", cwd=os.getcwd()))
        # 初始化项目为xbrain项目
        init_action()