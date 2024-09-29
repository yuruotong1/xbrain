from types import FunctionType
import unittest
from pydantic import BaseModel
from xbrain.tool import Tool, tools


class Add(BaseModel):
    x: int
    y: int

# 使用装饰器
@Tool(model=Add)
def my_function(x, y):
    return x + y

class TestTool(unittest.TestCase):

    def test_tool(self):
        assert 'Add' in tools
        assert type(tools['Add']) == FunctionType
