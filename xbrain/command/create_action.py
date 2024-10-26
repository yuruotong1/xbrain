from pydantic import BaseModel
from xbrain import xbrain_tool
from xbrain.agent.workflow import WorkflowAgent
from xbrain.context import Type
class XBrainCreate(BaseModel):
    """create a new action"""
    pass

@xbrain_tool.Tool(model=XBrainCreate, hit_condition = {Type.IS_XBRAIN_PROJECT: True})
def create_action():
    WorkflowAgent().run()
    
    
    
