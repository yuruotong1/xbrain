from pydantic import BaseModel, Field
from xbrain import xbrain_tool
from xbrain.utils.openai_utils import chat
import os

class XBrainChangeToAction(BaseModel):
    """将指定函数转变为action"""

class GenerateActionResponse(BaseModel):
    """生成action的响应"""
    code: str = Field(..., description="python代码")


class Func(BaseModel):
    """函数"""
    name: str = Field(..., description="函数名称")
    description: str = Field(..., description="用中文总结的函数描述")

class ExtractFunctionResponse(BaseModel):
    """提取函数"""
    funcs: list[Func] = Field(..., description="函数列表")

@xbrain_tool.Tool(model=XBrainChangeToAction)
def change_to_action(current_directory: str = ""):
    if not current_directory:
        # 获取当前目录
        current_directory = os.getcwd()
    # 递归列出当前目录及所有子目录下的.py文件
    py_files = []
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), current_directory)
            if relative_path.startswith('.') or \
                relative_path.startswith('build\\'):
                continue
            if file.endswith('.py') and file != '__init__.py':
                py_files.append(relative_path)
    # 打印所有找到的.py文件
    print("以下是发现的.py文件，请问你想对哪个文件进行操作？回复数字即可\n", "\n".join([f"{index}: {file}" for index, file in enumerate(py_files)]))
    file_index = input("请输入文件的数字序号：")
    file_name = py_files[int(file_index)]
    print("你选择了文件：", file_name)
    # 获取文件内容
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
        funcs = chat([{"role": "user", "content": file_content}], user_prompt=extract_function_prompt, response_format=ExtractFunctionResponse).parsed
        func_index = input("以下是提取到的函数，请问你想对哪个函数进行转换？回复数字即可\n" + \
                           "\n".join([f"{index}: {func.name} \"{func.description}\"" for index, func in enumerate(funcs.funcs)]) + "\n>>> ")
        chat_content = "请对以下代码的" + \
            funcs.funcs[int(func_index)].name + "函数进行转换：\n\n" + \
            file_content
        res = chat([{"role": "user", "content": chat_content}], user_prompt=prompt, response_format=GenerateActionResponse)
        if res.parsed:
            print("转换后的action内容如下：\n", res.parsed.code.strip())
        else:
            print("解析失败")

extract_function_prompt = """
## 目标 ##
你是一个代码识别助手，负责提取代码中的函数，你要做以下2件事：

1. 从代码中提取出函数；
2. 返回函数名称、函数行号、函数描述。
######
"""

prompt = """
## 目标 ##
你是一个代码助手，负责将函数转换为action，你要做以下2件事：

1. 在代码的顶部导入xbrain_tool，`from xbrain import xbrain_tool`
2. 为当前页面，用户指定的函数添加@xbrain_tool.Tool装饰器，然后对该函数执行步骤3；
3. 根据函数名称、函数逻辑（或者注释）、函数参数生成对应 pydantic 的 basemodel。
######

## 注意 ##
只修改用户指定的函数。
######

## 返回结果 ##
返回代码
######

## 案例 ##
输入：
```python
def add(a: int, b: int) -> int:
    \"\"\"
    Add two numbers.
    \"\"\"
    return a + b
```

输出：
```python
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
    
