from xbrain.core import xbrain_tool
from pydantic import BaseModel
from typing import ClassVar
import signal
from xbrain.core.chat import run
from xbrain.core.context import Type
from xbrain.core import xbrain_tool
from xbrain.utils.translations import _
class XBrainChatAction(BaseModel):
    """chat with my action"""
    description: ClassVar[str] =_("chat with my action")
    pass

@xbrain_tool.Tool(model=XBrainChatAction)
def chat_action():
    # 不带工具的纯聊 GPT镜像发射器
    print(_("Welcome to chat mode!"))
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
        res = run([{"role": "user", "content": input_str}], user_prompt="", chat_mode=True)
        print(res)

def signal_handler(sig, frame):
    print(_("\nExiting chat mode, looking forward to seeing you again!"))
    global running
    running = False