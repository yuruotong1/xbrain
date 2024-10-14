from xbrain import xbrain_tool
from pydantic import BaseModel
import signal
from xbrain.main import run
from xbrain.utils.import_utils import import_action

class XBrainChatAction(BaseModel):
    """Test capabilities"""
    pass

@xbrain_tool.Tool(model=XBrainChatAction)
def chat_action():
    print("Entering test mode, direct chat!")
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
        res = run([{"role": "user", "content": input_str}], chat_model=True)
        print("##result##\n", res)

def signal_handler(sig, frame):
    print("\nExiting chat mode, looking forward to seeing you again!")
    global running
    running = False