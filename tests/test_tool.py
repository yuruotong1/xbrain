from types import FunctionType
import unittest
from pydantic import BaseModel
from xbrain.tool import Tool, tools
from xbrain.main import run

class Add(BaseModel):
    x: int
    y: int

# 使用装饰器
@Tool(model=Add)
def my_function(x, y):
    return x + y

class TestTool(unittest.TestCase):
    def test_tool(self):
        assert tools[0]['name'] == 'Add'
        assert type(tools[0]['func']) == FunctionType

    def test_run_tool(self):
        res = run([{"role": "user", "content": "你有什么能力？"}])
        print(res)


