
from pydantic import BaseModel, Field
from xbrain import xbrain_tool
from xbrain.utils.openai_utils import chat
import os

class XBrainChangeToAction(BaseModel):
    """将用户给出的函数转变为action"""

class GenerateActionResponse(BaseModel):
    """生成action的响应"""
    code: str = Field(..., description="python代码")

@xbrain_tool.Tool(model=XBrainChangeToAction)
def change_to_action(current_directory: str = ""):
    if not current_directory:
        # 获取当前目录
        current_directory = os.getcwd()
    # 列出当前目录下所有文件和目录
    all_files_and_dirs = os.listdir(current_directory)
    # 过滤出所有以.py结尾的文件
    py_files = [file for file in all_files_and_dirs if file.endswith('.py')]
    # 打印所有找到的.py文件
    print("以下是发现的.py文件，请问你想对哪个文件进行操作？回复数字即可\n", "\n".join([f"{index}: {file}" for index, file in enumerate(py_files)]))
    file_index = input("请输入文件的数字序号：")
    file_name = py_files[int(file_index)]
    print("你选择了文件：", file_name)
    # 获取文件内容
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
        res = chat([{"role": "user", "content": file_content}], user_prompt=prompt, response_format=GenerateActionResponse)
        if res.parsed:
            print("转换后的action内容如下：\n", res.parsed.code)
        else:
            print("解析失败")



prompt = """
## 目标 ##
你是一个代码助手，负责将函数转换为action，你要做以下2件事：

1. 在代码的顶部导入xbrain_tool，`from xbrain import xbrain_tool`
2. 为当前页面函数添加@xbrain_tool.Tool装饰器；
3. 根据函数名称、函数逻辑（或者注释）、函数参数生成对应 pydantic 的 basemodel。
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
    
