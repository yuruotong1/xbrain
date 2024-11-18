from pydantic import Field, BaseModel
from typing import List, Dict, Any, Optional
from pydantic.dataclasses import dataclass

class Parameters(BaseModel):
    type: str = Field(description="type")
    properties: dict = Field(description="parameters properties")
    required: list[str] = Field(description="必填参数有哪些")



class Node(BaseModel):
    name: str = Field(
        description="Human-readable name of the node."
    )
    description: str = Field(
        description="Function description."
    )
    parameters: Parameters = Field(
        description="parameters of function"
    )

class Connection():
    source_node: str = Field(
        description="ID of the source node."
    )
    source_output: str = Field(
        description="Name of the output from the source node."
    )
    target_node: str = Field(
        description="ID of the target node."
    )
    target_input: str = Field(
        description="Name of the input on the target node."
    )

class Workflow(BaseModel):
    nodes: List[Node] = Field(
        description="List of nodes in the workflow."
    )
    connections: List[Connection] = Field(
        description="List of connections between nodes."
    )

    def validate(self):
        pass

    def execute(self):
        pass


class ConditionalNode(Node):
    condition: str = Field(
        description="Expression to evaluate for conditional execution."
    )
    true_branch: List[str] = Field(
        default_factory=list,
        description="List of node ids to execute if condition is true."
    )
    false_branch: List[str] = Field(
        default_factory=list,
        description="List of node ids to execute if condition is false."
    )