from xbrain import xbrain_tool
from pydantic import BaseModel
import os
from xbrain.context import Type
from xbrain.utils import constant

class XBrainInitAction(BaseModel):
    """init project"""
    pass

@xbrain_tool.Tool(model=XBrainInitAction, hit_condition = {Type.IS_XBRAIN_PROJECT: False})
def init_action():
    """init project"""
    project_name = input("请输入项目名称：\n>>> ")
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    if not os.path.exists(constant.CONFIG_NAME):
        with open(constant.CONFIG_NAME, "w") as file:
            file.write("# XBrain project configuration file\n")
    print(f"已成功创建项目, 已将工作空间设置为{project_name}")