from xbrain import xbrain_tool
from pydantic import BaseModel, Field
import signal
from xbrain.main import run
import glob
import os
import importlib
import sys

class XBrainChatAction(BaseModel):
    """进入对话模式"""
    pass

@xbrain_tool.Tool(model=XBrainChatAction)
def chat_action():
    dynamic_import()
    print("进入对话模式！")
    global running
    running = True
    signal.signal(signal.SIGINT, signal_handler)  # 捕获 Ctrl + C 信号
    while running:
        try:
            input_str = input("💬 ")
        # 当使用 ctrl + c 退出时，会抛出 EOFError 异常
        except EOFError:
            break
        if input_str == "exit":
            break
        res = run([{"role": "user", "content": input_str}], chat_model=True)
        print(res)


def dynamic_import():
    current_dir = os.getcwd()
    print(current_dir)
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                module_name = file[:-3]
                module_path = os.path.join(root, file)
                # 动态导入模块
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)


def signal_handler(sig, frame):
    print("\n退出对话模式，期待下次再见！")
    global running
    running = False