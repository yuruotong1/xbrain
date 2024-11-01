from pydantic import BaseModel
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.plugin.agent.workflow import WorkflowAgent
from xbrain.core.context import Type
from xbrain.utils.translations import _
class XBrainCreate(BaseModel):
    """create a new action"""
    description: ClassVar[str] = _("create a new action")
    pass

@xbrain_tool.Tool(model=XBrainCreate)
def create_action():
    WorkflowAgent().run()
    
    
    
