from pydantic import Field, BaseModel
from typing import List, Dict, Any, Optional
from pydantic.dataclasses import dataclass

@dataclass
class Node():
    id: str = Field(
        description="Unique identifier for the node."
    )
    name: str = Field(
        description="Human-readable name of the node."
    )
    action: callable = Field(
        description="Function to be executed in the node."
    )
    inputs: Dict[str, Any] = Field(
        default_factory=dict,
        description="Dictionary of inputs specific to the node."
    )
    outputs: Dict[str, Any] = Field(
        default_factory=dict,
        description="Dictionary of output identifiers produced by the node."
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Optional metadata about the node."
    )

@dataclass
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