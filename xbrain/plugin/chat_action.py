from xbrain.core import xbrain_tool
from pydantic import BaseModel
from typing import ClassVar
import signal
from xbrain.core.chat import run
from xbrain.core.context import Type
from xbrain.utils.translations import _
class XBrainChatAction(BaseModel):
    """chat with my action"""
    description: ClassVar[str] =_("chat with my action")
    pass

@xbrain_tool.Tool(model=XBrainChatAction, hit_condition={Type.IS_XBRAIN_PROJECT: True})
def chat_action():
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
        res = run([{"role": "user", "content": input_str}], user_prompt="", chat_model=True)
        print(res)

def signal_handler(sig, frame):
    print(_("\nExiting chat mode, looking forward to seeing you again!"))
    global running
    running = False