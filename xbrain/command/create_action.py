import os
from xbrain import xbrain_tool
from pydantic import BaseModel, Field
from xbrain.utils.openai_utils import chat

class XBrainCreateAction(BaseModel):
    """创建action"""
    pass

class GenerateActionResponse(BaseModel):
    """生成action的响应"""
    py_name: str = Field(..., description="py文件名称")
    code: str = Field(..., description="python代码")

@xbrain_tool.Tool(model=XBrainCreateAction)
def create_action():
    action_description = input("action是用来干什么的：")
    print("功能生成中...")
    res = chat([{"role": "user", "content": action_description}], user_prompt=prompt, response_format=GenerateActionResponse)
    if res.parsed:
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, res.parsed.py_name)
        code = res.parsed.code.strip().replace("```python", "").replace("```", "")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(code)
        print("创建成功，已生成文件：", file_path)
    else:
        print("解析失败")



prompt = """
## 目标 ##
你是一个代码助手，负责将用户的需求转换为action，你要做以下2件事：

1. 充分理解用户的需求，并将其转换为action
1. 在代码的顶部导入xbrain_tool，`from xbrain import xbrain_tool`
2. 根据用户的描述生成一个函数，并引入适当的python包，为该函数添加@xbrain_tool.Tool装饰器；
3. 根据函数名称、函数逻辑（或者注释）、函数参数生成对应 pydantic 的 basemodel。
4. 起一个py文件的名称并返回。
######

## 返回结果 ##
返回代码
######

## 案例 ##
输入：我两个数相加

输出：
add_action.py

from xbrain import xbrain_tool
class Add(BaseModel):
    \"\"\"将两个数相加\"\"\"
    a: int = Field(..., description="第一个数")
    b: int = Field(..., description="第二个数")

@xbrain_tool.Tool(model=Add)
def add(a: int, b: int) -> int:
    \"\"\"
    Add two numbers.
    \"\"\"
    return a + b
"""
    
