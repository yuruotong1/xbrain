from pydantic import BaseModel
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.plugin.agent.workflow import WorkflowAgent
from xbrain.core.context import Type
from xbrain.utils.translations import _
class XBrainCreate(BaseModel):
    """创建一个新的插件"""
    pass

@xbrain_tool.Tool(model=XBrainCreate)
def create_action():
    WorkflowAgent().run()
    
    
    
