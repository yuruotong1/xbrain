from textify4llm import process_file
from pydantic import BaseModel, Field
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.utils.translations import _
import logging

logger = logging.getLogger(__name__)

class XBrainFile(BaseModel):
    '''extract a file to structured JSON'''
    description: ClassVar[str] = _("extract a file to structured JSON")
    
    path: str = Field(
        description="path to the target file"
    )

@xbrain_tool.Tool(model=XBrainFile)
def xbrain_file_wrapper(path: str) -> str:

    logger.info(f"调用工具时的入参: {path}")

    return(process_file(path))
