import json
from xbrain.core.workflow_schema import Node, Connection, Workflow

embed_node = Node(
    id="node_1",
    cls="XBrainEmbed",
    name="Embed Text",
    description="",
    inputs=["xbrain/README_EN.md"],
    outputs=[],
    parameters={},
    metadata={}
)

chat_node = Node(
    id="node_2",
    cls="",
    name="Start Chat",
    description="",
    inputs=[],
    outputs=[],
    parameters={},
    metadata={}
)

# Connections
connection1 = Connection(
    id="conn_1",
    source_node="node_1",
    source_output="embedded_text",
    target_node="node_2",
    target_input="embedded_text"
)

# Workflow
workflow = Workflow(
    nodes=[embed_node, chat_node],
    connections=[connection1]
)

test_workflow = Workflow(
    nodes=[chat_node],
    connections=[]
)

def execute_workflow(workflow: Workflow):
    print((workflow.model_dump_json()))



execute_workflow(workflow=workflow)