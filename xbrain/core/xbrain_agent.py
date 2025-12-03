from xbrain.utils.openai_utils import chat

class Agent:
    def __init__(self, func):
        if not hasattr(func, "run"):
            raise ValueError("func must have run method")
        self.worker = func
        return None

    def run(self, *args, **kwargs):
        # 3. 【关键】当外界调用 Agent.run 时，转交给内部的 worker 去执行
        return self.worker.run(self, *args, **kwargs)


class WorkFlow:
    """
    工作流类，用于顺序执行多个智能体。
    """
    def __init__(self, agents):
        self.agents = agents
        
    def run(self, input):
        """
        执行工作流，按顺序调用智能体的 run 方法。
        """
        first_agent = self.agents[0]
        res = first_agent.run(input)
        for agent in self.agents[1:]:
            res = agent.run(res)
        return res
