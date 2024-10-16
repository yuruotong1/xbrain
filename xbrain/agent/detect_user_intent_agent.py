from xbrain import xbrain_tool
from xbrain.utils.openai_utils import chat
from pydantic import BaseModel, Field
from typing import List
# 根据上下文预测用户接下来的行为
def run():
    res = "📜 I can provide the following support:\n\n"
    number = 1
    chat_response = chat([{"role": "user", "content": "hello"}], tools=None, user_prompt=prompt, response_format=None)
    for tool in xbrain_tool.tools:
        res += f"{number}. {tool['name']}: {tool['description']}\n"
        number += 1
    print(res)

def get_command_map():
    return {str(i + 1): tool['func'] for i, tool in enumerate(xbrain_tool.tools)}

prompt = """
###目标###
根据用户上下文中的pre_actions，预测其余字段可能发生了什么变化，返回变化的上下文。
###上下文###
{context}
###例子###
上下文
{  
    "current_path": "/Users/yuanhang/work/xbrain",
    "is_xbrain_project": True,
    "current_file_path": "/Users/yuanhang/work/xbrain/xbrain/main.py"   
}
    
输入：
[{"name": "create_action", "context": {"name": "test", "description": "test"}}]

输出：    
{
    "intent": "创建一个test.py文件后，用户可能要对这个文件做操作",
    "context": [
        {
            "name": "current_file_path",
            "value": "/Users/yuanhang/work/xbrain/test.py"
        }
    ]
}

"""

class ContextModel(BaseModel):
    """
    当前环境变量
    """
    name: str = Field(..., description="环境变量名称")
    value: str = Field(..., description="变化后的值")

class ResponseModel(BaseModel):
    """
    用户可能的行为
    """
    intent: str = Field(..., description="用户可能的行为")
    context: List[ContextModel] = Field(..., description="可能发生变化的环境变量")


