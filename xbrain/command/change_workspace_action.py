import os
from xbrain import xbrain_tool
from pydantic import BaseModel
from xbrain.command import init_action
from xbrain.utils.input_util import get_input
class XBrainChangeWorkspaceAction(BaseModel):
    """change workspace"""
    pass

@xbrain_tool.Tool(model=XBrainChangeWorkspaceAction)
def change_workspace_action():
    path = get_input("please input the workspace path")
    if path:
        os.chdir(path)
        print(f"\033[;32mcurrent workspace: {os.getcwd()}\033[0m")
        # 初始化项目为xbrain项目
        init_action()