from pydantic import BaseModel
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.core.context import is_hit
from xbrain.utils.translations import _

class XBrainShowAllCommand(BaseModel):
    """Show all capabilities"""
    description: ClassVar[str] = _("Show all capabilities")
    pass

def get_tools():
    show_tools = []
    for tool in xbrain_tool.tools:
        if not tool["name"].startswith("XBrain") or \
           not is_hit(tool["hit_condition"]) or \
           tool["name"].startswith("XBrainShowAllCommand"):
            continue
        show_tools.append(tool)
    return show_tools

@xbrain_tool.Tool(model=XBrainShowAllCommand)
def show_all_command():
    res = _("I guess you want to do the following, or chat with me:\n\n")
    number = 1
    show_tools = get_tools()
    for tool in show_tools:
        res += f"{number}. {_(tool['description'])}\n"
        number += 1
    print(res)

def get_command_map():
    return {str(i + 1): tool['func'] for i, tool in enumerate(get_tools())}
