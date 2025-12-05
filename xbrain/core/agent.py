from xbrain.utils.openai_utils import chat

class Agent:
    def __init__(self, global_context, agent_result):
        self.global_context = global_context
        self.agent_result = agent_result


    def run(self, *args, **kwargs):
        raise NotImplementedError("Agent.run must be implemented")



class WorkFlow:
    """
    工作流类，用于顺序执行多个智能体。
    """
    def __init__(self, *agent_class_list):
        self.agents = []
        self.global_context = {}
        self.agent_result = {}
        
        for agent_class in agent_class_list:
            agent = agent_class(self.global_context, self.agent_result)
            self.agents.append(agent)
        
    def run(self, *args, **kwargs):
        """
        顺序执行所有智能体，首个智能体接收外部参数，后续智能体以前一结果作为输入。
        """
        # 依次运行所有智能体，第一个接收外部参数，其余以前一结果作为输入
        for agent in self.agents:
            if agent is self.agents[0]:
                res = agent.run(*args, **kwargs)
            else:
                res = agent.run()
            self.agent_result[agent.__class__.__name__] = res
        return self.agent_result
