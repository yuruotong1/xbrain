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
        return "A run"
class B(Agent):
    def run(self):
        return "B run"

w1 = WorkFlow(A)
w2 = WorkFlow(B)
agent_ui = AgentUI(w1, w2)


if __name__ == "__main__":
    agent_ui.launch()