from pydantic import BaseModel
from xbrain import xbrain_tool
from xbrain.context import is_hit

class XBrainShowAllCommand(BaseModel):
    """Show all capabilities"""
    pass

@xbrain_tool.Tool(model=XBrainShowAllCommand)
def show_all_command():
    res = "I guess you want to do the following, or chat with me:\n\n"
    number = 1
    for tool in xbrain_tool.tools:
        if not is_hit(tool["hit_condition"]) or \
            tool["name"].startswith("XBrainShowAllCommand"):
            continue
        res += f"{number}. {tool['description']}\n"
        number += 1
    print(res)

def get_command_map():
    return {str(i + 1): tool['func'] for i, tool in enumerate(xbrain_tool.tools)}
