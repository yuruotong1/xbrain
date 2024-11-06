from pydantic import BaseModel
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.core.context import is_hit
from xbrain.utils.translations import _

class XBrainShowAllCommand(BaseModel):
    description: ClassVar[str] = "列举所有能力"

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
    number = 1
    show_tools = get_tools()
    res = ""
    for tool in show_tools:
        res += f"{number}. {_(tool['description'])}\n"
        number += 1
    return res