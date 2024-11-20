import os
from typing import List
from pydantic import BaseModel, Field
from xbrain.plugin.agent.agent_base import AgentBase
from xbrain.utils.openai_utils import chat
from xbrain.utils.translations import _

class CodeAgent(AgentBase):
    def run(self, requirement: str):
        res = chat([{"role": "user", "content": requirement}], user_prompt=prompt, response_format=WorkflowModel) 
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, res.parsed.py_name)
        code = res.parsed.code.strip().replace("```python", "").replace("```", "")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        print(_("Creation successful!\nfile generated: "), file_path)
        return res.parsed
        

class WorkflowModel(BaseModel):
    """Response for generating an action"""
    py_name: str = Field(..., description="Python file name")
    third_party_dependencies: List[str] = Field(description="third-party dependencies")
    code: str = Field(..., description="Python code")

prompt = """
# Objective ##
You are a code assistant responsible for converting user requirements into actions. You need to do the following:

1. Fully understand the user's requirements and convert them into an action.
2. Import xbrain_tool at the top of the code, `from xbrain.core import xbrain_tool`
3. Generate a function based on the user's description, introduce the appropriate Python packages, and add the @xbrain_tool.Tool decorator to the function;
4. Generate a corresponding pydantic basemodel based on the function name, logic (or comments), and parameters.
5. Name a Python file and return it.
6. If the code has dependencies on third-party libraries, please return the libraries that need to be installed.
######

## Example ##
Input: I want to add two numbers

Output:
add_action.py

from xbrain.core import xbrain_tool
class Add(BaseModel):
    \"\"\"Add two numbers\"\"\"
    a: int = Field(..., description="First number")
    b: int = Field(..., description="Second number")

@xbrain_tool.Tool(model=Add)
def add(a: int, b: int) -> int:
    \"\"\"
    Add two numbers.
    \"\"\"
    return a + b
"""