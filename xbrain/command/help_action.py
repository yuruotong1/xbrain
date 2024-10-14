from pydantic import BaseModel
from xbrain import xbrain_tool

class XBrainShowAllCommand(BaseModel):
    """Show all capabilities"""
    pass

@xbrain_tool.Tool(model=XBrainShowAllCommand)
def show_all_command():
    res = "📜 I can provide the following support, enter the number to use directly or just tell me what you want to do:\n\n"
    number = 1
    for tool in xbrain_tool.tools:
        if not tool["name"].startswith("XBrain"):
            continue
        res += f"{number}. {tool['name'].replace('XBrain', '').strip()}: {tool['description']}\n"
        number += 1
    print(res)

def get_command_map():
    return {str(i + 1): tool['func'] for i, tool in enumerate(xbrain_tool.tools)}
