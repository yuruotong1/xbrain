import openai
import json
import os
from xbrain.context import context, Type, ActionRecord
tools = []

class Tool:
    def __init__(self, model, hit_condition=None):
        self.model = model
        self.hit_condition = hit_condition

    def __call__(self, func):
        # 利用 openai 官方的转换函数，提取 name
        function = openai.pydantic_function_tool(self.model)
        # 删除已经导入的工具
        for tool in tools:
            if tool["name"] == function["function"]["name"] and \
               os.path.samefile(tool["path"], func.__code__.co_filename):
                tools.remove(tool)
                break
        tools.append({
            "name": function["function"]["name"],
            "description": function["function"].get("description", ""),
            "hit_condition": self.hit_condition,
            "model": self.model,
            "func": func,
            "path": func.__code__.co_filename
        })
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result

        return wrapper

def _get_tool_by_name(name):
    for tool in tools:
        if tool["name"] == name:
            return tool
    return None

def run_tool(openai_res):
    res = []
    for tool_call in openai_res.tool_calls:
        info = _get_tool_by_name(tool_call.function.name)
        tool_func = info["func"]
        run_res = tool_func(**json.loads(tool_call.function.arguments))
        run_res = run_res if run_res is not None else ""
        print("run action：\n", 
              "action name: ", tool_call.function.name, "\n",
              "action path: ", info["path"], "\n",
              "action arguments: ", json.loads(tool_call.function.arguments), "\n", 
              "action result: ", run_res, "\n\n"
              )
        # 存储到上下文中
        context[Type.PRE_ACTIONS].append(ActionRecord(tool_call.function.name, json.loads(tool_call.function.arguments)))
        res.append(run_res)
    return res
