from pydantic import BaseModel
from typing import ClassVar
from xbrain import xbrain_tool
from xbrain.agent.workflow import WorkflowAgent
from xbrain.context import Type
from xbrain.utils.translations import _
class XBrainCreate(BaseModel):
    """create a new action"""
    description: ClassVar[str] = _("create a new action")
    pass

@xbrain_tool.Tool(model=XBrainCreate, hit_condition = {Type.IS_XBRAIN_PROJECT: True})
def create_action():
    WorkflowAgent().run()
    
    
    
