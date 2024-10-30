from xbrain import xbrain_tool
from pydantic import BaseModel, Field

class XBrainAddTwoNumbers(BaseModel):
    """Add two numbers"""
    num1: float = Field(..., description="First number (int or float)")
    num2: float = Field(..., description="Second number (int or float)")

@xbrain_tool.Tool(model=XBrainAddTwoNumbers)
def add_two_numbers(num1: float, num2: float) -> float:
    """
    Function to add two numbers.
    :param num1: First number (int or float)
    :param num2: Second number (int or float)
    :return: Sum of num1 and num2
    """
    return num1 + num2