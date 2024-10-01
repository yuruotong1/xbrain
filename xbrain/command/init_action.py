import os
from pydantic import BaseModel, Field
from xbrain import xbrain_tool

class XBrainInitMode(BaseModel):
    """初始化项目"""
    project_name: str = Field(..., description="项目名称，尽量使用英文") 

@xbrain_tool.Tool(model=XBrainInitMode)
def init(project_name: str):
    os.makedirs(project_name, exist_ok=True)
    os.makedirs(os.path.join(project_name, "actions"))
    os.makedirs(os.path.join(project_name, "actions", "demo_aciton.py"))
    os.makedirs(os.path.join(project_name, "main.py"))
    os.makedirs(os.path.join(project_name, "requirements.txt"))
    os.makedirs(os.path.join(project_name, "README.md"))
