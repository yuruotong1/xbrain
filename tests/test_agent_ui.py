import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
# 把根目录加入到 Python 搜索路径中
sys.path.insert(0, project_root)
from xbrain.core.agent_ui import AgentUI
from xbrain.core.agent import Agent, WorkFlow


     
class A(Agent):
    def run(self):
        name = self.global_context["name"]
        return name + "是一个好名字"

param = {
    "name": {
        "type": "string",
        "description": "名字",
    }
}


w1 = WorkFlow([A], "name", "判断一个人的名字是好还是坏", param, ["name"])
agent_ui = AgentUI(w1)


if __name__ == "__main__":
    agent_ui.launch()