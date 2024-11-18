from pydantic import BaseModel, Field
from xbrain.core import xbrain_tool
from xbrain.plugin.embed_csv_action import embedding_csv_action
from xbrain.plugin.retrieve_csv_action import retrieve_action
import gradio as gr

class XBrainCustomerServiceWorkflow(BaseModel):
    """智能客服工作流"""
    path: str = Field(description="要embedding的文件地址")

@xbrain_tool.Tool(model=XBrainCustomerServiceWorkflow)
def customer_service_workflow(path: str):
    embedding_csv_action(path)
    demo = gr.ChatInterface(random_response, type="messages")
    demo.launch()



def random_response(message, history):
    print(message, history)
    res = retrieve_action(message)
    return res

