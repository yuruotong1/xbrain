from pydantic import BaseModel, Field
from typing import ClassVar
from xbrain.core import xbrain_tool
from xbrain.core.context import Type
from xbrain.utils.openai_utils import chat
import os
from xbrain.utils.translations import _
from xbrain.utils.input_util import get_input
class XBrainIntegrate(BaseModel):
    """integrate existing functions into xbrain"""
    description: ClassVar[str] = _("integrate existing functions into xbrain")

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
    current_directory = current_directory or os.getcwd()
    
    # 获取所有 .py 文件
    py_files = [
        os.path.relpath(os.path.join(root, file), current_directory)
        for root, _, files in os.walk(current_directory)
        for file in files
        if not (os.path.relpath(os.path.join(root, file), current_directory).startswith('.') or
                os.path.relpath(os.path.join(root, file), current_directory).startswith('build\\')) and
           file.endswith('.py') and file != '__init__.py'
    ]
    
    # 打印找到的 .py 文件
    print(_("The following .py files were found: \n") + "\n".join([f"{index + 1}: {file}" for index, file in enumerate(py_files)]))
    file_index = int(get_input(_("\nWhich file would you like to operate on?"))) - 1
    file_name = py_files[file_index]
    print(_("You have selected the file:"), file_name)
    
    # 读取文件内容
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    # 提取函数，并让用户确认
    funcs = chat([{"role": "user", "content": file_content}], system_prompt=extract_function_prompt, response_format=ExtractFunctionResponse).parsed
    func_index = int(get_input(_("Which function would you like to convert? \n") + 
                               "\n".join([f"{index+1}: {func.name} \"{func.description}\"" for index, func in enumerate(funcs.funcs)]))) - 1
    
    # 转换函数
    chat_content = f"Please convert the following code's {funcs.funcs[func_index].name} function:\n\n{file_content}"
    res = chat([{"role": "user", "content": chat_content}], system_prompt=prompt, response_format=GenerateActionResponse)
    
    if res.parsed:
        code = res.parsed.code.strip().replace("```python", "").replace("```", "")
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(code)
        print(_("Conversion successful, file generated:"), file_name)
    else:
        print(_("Parsing failed"))

extract_function_prompt = """
## 目标 ##
您是一个代码识别助手，负责从代码中提取函数，您需要完成以下两件事：

1. 从代码中提取函数；

2. 返回函数名称，函数描述。

######"""

prompt = """
## 目标 ##

您是一个代码助手，负责将函数转换为动作，您需要完成以下三件事：

1. 在代码顶部导入 xbrain_tool，`from xbrain import xbrain_tool`
2. 在用户指定的当前页面的函数上添加 @xbrain_tool.Tool 装饰器
3. 根据函数名称、函数逻辑（或注释）和函数参数生成相应的 pydantic basemodel。

######

## 注意 ##
仅修改用户指定的函数。
######

## 返回结果 ##
返回代码
######


## 示例 ##
输入:

```python
def add(a: int, b: int) -> int:
    \"\"\"

    Add two numbers.

    \"\"\"
    return a + b

```

输出:

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
    
