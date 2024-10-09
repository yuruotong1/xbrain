import os
from xbrain import xbrain_tool
from pydantic import BaseModel, Field
from xbrain.utils.openai_utils import chat

class XBrainCreateAction(BaseModel):
    """Create capability"""
    pass

class GenerateActionResponse(BaseModel):
    """Response for generating an action"""
    py_name: str = Field(..., description="Python file name")
    code: str = Field(..., description="Python code")

@xbrain_tool.Tool(model=XBrainCreateAction)
def create_action():
    action_description = input("What is the action for:\n")
    print("##Generating function##")
    res = chat([{"role": "user", "content": action_description}], user_prompt=prompt, response_format=GenerateActionResponse)
    if res.parsed:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, res.parsed.py_name)
        code = res.parsed.code.strip().replace("```python", "").replace("```", "")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        print("Creation successful, file generated:", file_path)
    else:
        print("Parsing failed")



prompt = """
## Objective ##
You are a code assistant responsible for converting user requirements into actions. You need to do the following:

1. Fully understand the user's requirements and convert them into an action.
2. Import xbrain_tool at the top of the code, `from xbrain import xbrain_tool`
3. Generate a function based on the user's description, introduce the appropriate Python packages, and add the @xbrain_tool.Tool decorator to the function;
4. Generate a corresponding pydantic basemodel based on the function name, logic (or comments), and parameters.
5. Name a Python file and return it.
######

## Return Result ##
Return code
######

## Example ##
Input: I want to add two numbers

Output:
add_action.py

from xbrain import xbrain_tool
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
    
