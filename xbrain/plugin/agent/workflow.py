from xbrain.plugin.agent.agent_base import AgentBase
from xbrain.plugin.agent.product_agent import ProductAgent
from xbrain.plugin.agent.code_agent import CodeAgent


class WorkflowAgent(AgentBase):
    def run(self):
        requirement = ProductAgent().run()
        if requirement.is_product:
            res = CodeAgent().run(requirement.content)
            third_party_dependencies = res.third_party_dependencies
            for package in third_party_dependencies:
                print(f"Installing {package}...")
                # todo 安装第三方依赖
        else:
            print(requirement.content)
    