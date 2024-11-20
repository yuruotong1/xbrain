from pydantic import BaseModel, Field
from xbrain.plugin.agent.agent_base import AgentBase
from xbrain.utils.openai_utils import chat, multiple_rounds_chat

class ProductAgent(AgentBase):
    def run(self, *args, **kwargs):
        requirement = multiple_rounds_chat(
            is_complete_description="是否清楚完整地了解用户的真实需求", 
            content_description="目前了解的用户的需求",
            question_description="还需要追问的问题", 
            messages=[{"role": "assistant", "content": "please tell me your requirements?"}],
            system_prompt=workflow1_prompt)

        design = chat(
            messages=[{"role": "user", "content": requirement}],
            user_prompt=workflow2_prompt,
            response_format=Workflow2Model
            )
        
        return design.parsed
   


workflow1_prompt = """
### 目标 ###
你是一名产品经理，你的工作是不断挖掘用户需求的细节，直到清楚完整地了解用户的真实需求为止，你的工作流程是：
1. 判断是否清楚完整地了解了用户的真实需求
2. 如果第一步返回False，则根据用户的需求，不断追问细节，不要急于给出结论、不要猜测；
3. 如果第一步返回True，则给出目前了解的用户的需求；
4. 重复1-3步，直到清楚完整地了解用户的真实需求为止。
"""

class Workflow2Model(BaseModel):
    is_product: bool = Field(description="是否可以用python完成")
    content: str = Field(description="设计出的产品或操作流程")

workflow2_prompt = """
### 目标 ###
你是一名产品经理，你的工作是根据用户的需求，设计出合适的产品。你的工作流程是：
1. 判断用户的需求是否可以用python完成；
2. 如果可以用python完成，则给出产品设计方案；
3. 如果不可以用python完成，则给出操作建议。
"""