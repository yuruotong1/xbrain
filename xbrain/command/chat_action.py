from xbrain import xbrain_tool
from pydantic import BaseModel, Field
import signal
from xbrain.main import run

class XBrainChatAction(BaseModel):
    """进入对话模式"""
    pass

@xbrain_tool.Tool(model=XBrainChatAction)
def chat_action():
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

def signal_handler(sig, frame):
    print("\n退出对话模式，期待下次再见！")
    global running
    running = False