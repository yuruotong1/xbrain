from xbrain.utils.openai_utils import chat
from enum import Enum
agents = []
class INPUT_TYPE(str, Enum):
    STR = "str"
    IMG = "img"

class Agent:
    """
    workflow 会根据 level 大小依次运行 agent，从0、1、2、3 
    """
    def __init__(self, func):
        if not hasattr(func, "level"):
            raise ValueError("func must have level attribute")
        if not hasattr(func, "run"):
            raise ValueError("func must have run method")
        agents.append(func)
        return None


def work_flow_run(input):
    first_agent = agents[0]
    res = first_agent().run(input)
    for agent in agents[1:]:
        res = agent().run(res)
    return res
