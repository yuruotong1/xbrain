import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录 (即 tests 的上一级)
project_root = os.path.dirname(current_dir)
# 把根目录加入到 Python 搜索路径中
sys.path.insert(0, project_root)
from xbrain.core.xbrain_agent import Agent, agents, work_flow_run
from xbrain.utils.openai_utils import chat,chat_video
import unittest
class TestAgent(unittest.TestCase):
    def test_agent(self):
        @Agent
        class A:
            level = 1
            def run(self, input):
                print("接收", input)
                return "agent2 输入"
        @Agent
        class B:
            level = 2
            def run(self, input):
                print("接收", input)
                return "agent2 输出"

        xbrain_res = work_flow_run("test input")
        assert xbrain_res == "agent2 输出"

    def test_chat(self):
        @Agent
        class A:
            level = 1
            def run(self, input):
                res = chat([{"role": "user", "content": input}], "你是一个智能助手")
                return res
        xbrain_res = work_flow_run("test input")
        print(xbrain_res)

    def test_vedio(self):
        res = chat_video("视频里讲了啥", r"C:\Users\yuruo\术语一致性翻译.mp4") 
        print(res)
