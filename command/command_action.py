from pydantic import BaseModel, Field
from xbrain import tool
import os



def create_action():
    pass

def create_bot(tool_name):
    pass

def deploy(tool_name):
    pass

class InitMode(BaseModel):
    project_name: str = Field(..., description="项目名称，尽量使用英文") 

@tool.Tool(model=InitMode)
def init(project_name: str):
    os.makedirs(project_name, exist_ok=True)
    os.makedirs(os.path.join(project_name, "actions"))
    os.makedirs(os.path.join(project_name, "actions", "demo_aciton.py"))
    os.makedirs(os.path.join(project_name, "main.py"))
    os.makedirs(os.path.join(project_name, "requirements.txt"))
    os.makedirs(os.path.join(project_name, "README.md"))

def login(username, password):
    pass


