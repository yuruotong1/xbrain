from cgitb import reset
from xbrain.utils.openai_utils import chat
from pydantic import BaseModel, Field
from xbrain.core.tool import Tool

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
    def __init__(self, agent_class_list, name="", description="", parameters={}, required_parameters=[]):
        self.name = name
        self.description = description
        self.agents = []
        self.global_context = {}
        self.agent_result = {}
        self.tool_call_json = self.pack_tool_call_json(parameters, required_parameters)
        
        for agent_class in agent_class_list:
            agent = agent_class(self.global_context, self.agent_result)
            self.agents.append(agent)
    
    def pack_tool_call_json(self, parameters, required_parameters):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description, 
                "strict": True,   
                "parameters": {
                    "type": "object",
                    "properties": parameters,
                },
                "required": required_parameters
            }
        }

    def pack_agent_result(self):
        return {
            "type": "object",
            "properties": self.agent_result,
        }

    def run(self, **kwargs):
        """
        顺序执行所有智能体，首个智能体接收外部参数，后续智能体以前一结果作为输入。
        """
        self.global_context.update(kwargs)
        # 依次运行所有智能体，第一个接收外部参数，其余以前一结果作为输入
        for agent in self.agents:
            res = agent.run()
            self.agent_result[agent.__class__.__name__] = res
        return reset
