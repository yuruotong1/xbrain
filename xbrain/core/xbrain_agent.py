from xbrain.utils.openai_utils import chat

class Agent:
    def __init__(self, global_context):
        self.global_context = global_context


    def run(self, *args, **kwargs):
        raise NotImplementedError("Agent.run must be implemented")



class WorkFlow:
    """
    工作流类，用于顺序执行多个智能体。
    """
    def __init__(self, agent_class_list):
        self.agents = []
        self.global_context = {}
        for agent_class in agent_class_list:
            agent = agent_class(self.global_context)
            self.agents.append(agent)
        
    def run(self, input):
        """
        执行工作流，按顺序调用智能体的 run 方法。
        """
        first_agent = self.agents[0]
        res = first_agent.run(input)
        for agent in self.agents[1:]:
            res = agent.run(res)
        return res
