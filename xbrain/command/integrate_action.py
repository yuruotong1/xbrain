from pydantic import BaseModel, Field
from xbrain import xbrain_tool
from xbrain.context import Type
from xbrain.utils.openai_utils import chat
import os

class XBrainIntegrate(BaseModel):
    """integrate existing functions into xbrain"""

class GenerateActionResponse(BaseModel):
    """Generate action response"""
    code: str = Field(..., description="Python code")

class Func(BaseModel):
    """Function"""
    name: str = Field(..., description="Function name")
    description: str = Field(..., description="Function description")

class ExtractFunctionResponse(BaseModel):
    """Extract function"""
    funcs: list[Func] = Field(..., description="List of functions")

@xbrain_tool.Tool(model=XBrainIntegrate, hit_condition={Type.IS_XBRAIN_PROJECT: True})
def change_to_action(current_directory: str = ""):
    if not current_directory:
        # Get current directory
        current_directory = os.getcwd()
    # Recursively list all .py files in the current directory and all subdirectories
    py_files = []
    for root, _, files in os.walk(current_directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), current_directory)
            if relative_path.startswith('.') or \
                relative_path.startswith('build\\'):
                continue
            if file.endswith('.py') and file != '__init__.py':
                py_files.append(relative_path)
                
    # Print all found .py files
    print("The following .py files were found：\n" + "\n".join([f"{index + 1}: {file}" for index, file in enumerate(py_files)]))
    file_index = input("\nWhich file would you like to operate on? \n>>> ")
    file_name = py_files[int(file_index) - 1]
    print("You have selected the file:", file_name)
    # Get file content
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
        funcs = chat([{"role": "user", "content": file_content}], user_prompt=extract_function_prompt, response_format=ExtractFunctionResponse).parsed
        func_index = input("Which function would you like to convert? \n" + \
                           "\n".join([f"{index+1}: {func.name} \"{func.description}\"" for index, func in enumerate(funcs.funcs)]) + "\n>>> ")
        chat_content = "Please convert the following code's " + \
            funcs.funcs[int(func_index) - 1].name + " function:\n\n" + \
            file_content
        res = chat([{"role": "user", "content": chat_content}], user_prompt=prompt, response_format=GenerateActionResponse)
        if res.parsed:
            code = res.parsed.code.strip().replace("```python", "").replace("```", "")
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(code)
            print("Conversion successful, file generated:", file_name)
        else:
            print("Parsing failed")

extract_function_prompt = """
## Objective ##
You are a code recognition assistant, responsible for extracting functions from the code, you need to do the following 2 things:

1. Extract functions from the code;
2. Return function name, function description.
######"""

prompt = """
## Objective ##
You are a code assistant, responsible for converting functions into actions, you need to do the following 3 things:

1. Import xbrain_tool at the top of the code, `from xbrain import xbrain_tool`
2. Add the @xbrain_tool.Tool decorator to the function specified by the user on the current page, then perform step 3;
3. Generate the corresponding pydantic basemodel based on the function name, function logic (or comments), and function parameters.
######

## Note ##
Only modify the function specified by the user.
######

## Return Result ##
Return code
######

## Example ##
Input:
```python
def add(a: int, b: int) -> int:
    \"\"\"
    Add two numbers.
    \"\"\"
    return a + b
```

Output:
```python
from xbrain import xbrain_tool
class Add(BaseModel):
    \"\"\"Add two numbers\"\"\"
    a: int = Field(..., description="The first number")
    b: int = Field(..., description="The second number")

@xbrain_tool.Tool(model=Add)
def add(a: int, b: int) -> int:
    \"\"\"
    Add two numbers.
    \"\"\"
    return a + b
"""
    
