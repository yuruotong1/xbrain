from pydantic import BaseModel
from xbrain import xbrain_tool

class XBrainShowAllCommand(BaseModel):
    """展示所有能力"""
    pass

@xbrain_tool.Tool(model=XBrainShowAllCommand)
def show_all_command():
    res = "📜 我能够提供以下支持，输入数字直接使用或者直接告诉我你想做什么:\n\n"
    number = 1
    for tool in xbrain_tool.tools:
        res += f"{number}. {tool['name'].replace('XBrain', '').strip()}: {tool['description']}\n"
        number += 1
    print(res)

def get_command_map():
    return {str(i + 1): tool['func'] for i, tool in enumerate(xbrain_tool.tools)}
