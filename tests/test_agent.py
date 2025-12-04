import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录 (即 tests 的上一级)
project_root = os.path.dirname(current_dir)
# 把根目录加入到 Python 搜索路径中
sys.path.insert(0, project_root)
from xbrain.core.xbrain_agent import Agent, WorkFlow
from xbrain.utils.openai_utils import chat,chat_video
import unittest
class TestAgent(unittest.TestCase):
    def test_agent(self):
      
        class A(Agent):
            def run(self, input):
                print("接收", input)
     
        class B(Agent):
            def run(self, input):
                print("接收", input)
                return "agent2 输出"
                
        workflow = WorkFlow([A, B])
        xbrain_res = workflow.run("test input")
        assert xbrain_res == "agent2 输出"

    def test_chat(self):
        class A(Agent):
            def run(self, input):
                res = chat([{"role": "user", "content": input}], "你是一个智能助手")
                return res
        class B(Agent): 
            def run(self, input):
                res = chat([{"role": "user", "content": input}], "你是一个智能助手")
                return res

        workflow = WorkFlow([A, B])
        xbrain_res = workflow.run("你好")
        print(xbrain_res)

    def test_global_context(self):
        class A(Agent):
            def run(self, input):
                self.global_context["a"] = "a"
                return "agent1 输出"
        class B(Agent):
            def run(self, input):
                return self.global_context["a"]
                
        workflow = WorkFlow([A, B])
        xbrain_res = workflow.run("test input")
        assert xbrain_res == "a"
