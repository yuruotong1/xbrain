from pydantic import BaseModel, Field
from xbrain import xbrain_tool
import os



def create_action():
    pass

def create_bot(tool_name):
    pass

def deploy(tool_name):
    pass

class InitMode(BaseModel):
    """初始化项目"""
    project_name: str = Field(..., description="项目名称，尽量使用英文") 

@xbrain_tool.Tool(model=InitMode)
def init(project_name: str):
    os.makedirs(project_name, exist_ok=True)
    os.makedirs(os.path.join(project_name, "actions"))
    os.makedirs(os.path.join(project_name, "actions", "demo_aciton.py"))
    os.makedirs(os.path.join(project_name, "main.py"))
    os.makedirs(os.path.join(project_name, "requirements.txt"))
    os.makedirs(os.path.join(project_name, "README.md"))


class ShowAllCommand(BaseModel):
    """展示所有命令"""
    pass

@xbrain_tool.Tool(model=ShowAllCommand)
def show_all_command():
    res = "我能够提供以下命令:\n\n"
    number = 1
    for tool in xbrain_tool.tools:
        res += f"{number}. {tool['name']}: {tool['description']}\n"
        number += 1
    return res

def login(username, password):
    pass


