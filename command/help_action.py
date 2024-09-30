from pydantic import BaseModel
from xbrain import xbrain_tool

class ShowAllCommand(BaseModel):
    """展示所有命令"""
    pass

@xbrain_tool.Tool(model=ShowAllCommand)
def show_all_command():
    res = "📜 我能够提供以下支持:\n\n"
    number = 1
    for tool in xbrain_tool.tools:
        res += f"{number}. {tool['name']}: {tool['description']}\n"
        number += 1
    return res
