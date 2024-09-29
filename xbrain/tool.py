import openai

tools = []

class Tool:
    def __init__(self, model):
        self.model = model

    def __call__(self, func):
        # 利用 openai 官方的转换函数，提取name
        function = openai.pydantic_function_tool(self.model)
        tools.append({"name": function["function"]["name"], "model":  self.model, "func": func})
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
        res = tool_func(**tool_call.function.arguments)
        res.append(res)
    return res
