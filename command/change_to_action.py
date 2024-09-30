
from pydantic import BaseModel
from xbrain import xbrain_tool
from utils.openai_utils import chat

class ChangeToAction(BaseModel):
    """将当前页面的函数转变为action"""

@xbrain_tool.Tool(model=ChangeToAction)
def change_to_action():
    messages = [
        {"role": "user", "content": "将当前页面的函数转变为action"}
    ]
    chat(messages, user_prompt=prompt)



prompt = """
## 目标 ##
你是一个代码助手，负责将函数转换为action，你要做以下2件事：

1. 为当前页面函数添加@xbrain_tool.Tool装饰器；
2. 根据函数名称、函数逻辑（或者注释）、函数参数生成对应 pydantic 的 basemodel。
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
    
