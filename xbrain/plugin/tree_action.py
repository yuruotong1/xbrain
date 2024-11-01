from pydantic import BaseModel, Field
from typing import ClassVar, Optional, List, Dict
from xbrain.core import xbrain_tool
from xbrain.utils.translations import _
import os
import fnmatch
import logging

logger = logging.getLogger(__name__)

class XBrainTree(BaseModel):
    '''Generate a tree of a directory'''
    description: ClassVar[str] = _("Generate a tree of a directory")
    
    path: str = Field(
        description="The root directory path to start the tree from."
    )
    ignore_patterns: Optional[List[str]] = Field(
        description="A list of glob patterns to ignore during traversal. always at least include: ['*.pyc', '__pycache__', '.venv', '.*']"
    )

@xbrain_tool.Tool(model=XBrainTree)
def tree(path: Optional[str] = None,
         ignore_patterns: Optional[List[str]] = None) -> Dict:
    logger.info(f"调用工具时的入参: {path}, {ignore_patterns}")
    if path is None:
        path = '.'
    if ignore_patterns is None:
        ignore_patterns = []

    def walk_directory(current_path: str) -> Dict:
        directory_structure = {
            "path": current_path,
            "entries": []
        }
        try:
            entries = os.listdir(current_path)
        except PermissionError:
            directory_structure["error"] = "Permission Denied"
            return directory_structure
        except FileNotFoundError:
            directory_structure["error"] = "Not Found"
            return directory_structure

        entries = sorted(entries)

        for entry in entries:
            full_path = os.path.join(current_path, entry)
            # Check if entry matches any ignore patterns
            if any(fnmatch.fnmatch(entry, pattern) for pattern in ignore_patterns):
                continue  # Skip ignored entries

            if os.path.isdir(full_path):
                directory_structure["entries"].append(walk_directory(full_path))
            else:
                directory_structure["entries"].append({"name": entry, "type": "file"})

        return directory_structure
    return walk_directory(path)