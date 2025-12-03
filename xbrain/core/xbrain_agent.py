from xbrain.utils.openai_utils import chat
agents = {}

class Agent:
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        if not hasattr(func, "run"):
            raise ValueError("func must have run method")
        if self.name in agents:
            raise ValueError("agent name already exists")
            
        agents[self.name] = func
        return None



class WorkFlow:
    """
    工作流类，用于顺序执行多个智能体。
    """
    def __init__(self, agent_names):
        self.agent_names = agent_names
        
    def run(self, input):
        """
        执行工作流，按顺序调用智能体的 run 方法。
        """
        first_agent = agents[self.agent_names[0]]
        res = first_agent().run(input)
        for agent_name in self.agent_names[1:]:
            res = agents[agent_name]().run(res)
        return res
