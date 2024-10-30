from xbrain import xbrain_tool
from pydantic import BaseModel
import signal
from xbrain.chat import run
from xbrain.context import Type
class XBrainChatAction(BaseModel):
    """chat with my action"""
    pass

@xbrain_tool.Tool(model=XBrainChatAction, hit_condition={Type.IS_XBRAIN_PROJECT: True})
def chat_action():
    print("Welcome to chat mode!")
    global running
    running = True
    signal.signal(signal.SIGINT, signal_handler)  # Capture Ctrl + C signal
    while running:
        try:
            input_str = input("💬 ")
        # When exiting using ctrl + c, an EOFError exception is thrown
        except EOFError:
            break
        if input_str == "exit":
            break
        res = run([{"role": "user", "content": input_str}], user_prompt="", chat_model=True)
        print(res)

def signal_handler(sig, frame):
    print("\nExiting chat mode, looking forward to seeing you again!")
    global running
    running = False