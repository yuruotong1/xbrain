import sys
import os
# 一般编译器不会把 xbrain 目录加入 PYTHONPATH，所以需要手动添加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import xbrain.plugin
from xbrain.core.chat import run
import signal
from xbrain.utils.config import Config, Constants
from xbrain.core.context import update_context
from xbrain.utils.input_util import get_input
from xbrain.utils.translations import _


def signal_handler(sig, frame):
    print(_("\nNice to meet you here!"))
    sys.exit(0)

def check_config():
    config = Config()
    if config.OPENAI_API_KEY == "":
        print(_("XBrain relies on the OpenAI API,please config in below path:\n{config_path}.\n\n"
                "If you have problem, please refer to: \n"
                "https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c#f85f9774b40c4b63bc6ec28fd11a2dde", 
                config_path = config.config_path))
        sys.exit(1)


def main(): 
    check_config()
    # 捕获 Ctrl + C 信号，进行更优雅的退出
    constants = Constants()
    signal.signal(signal.SIGINT, signal_handler)
    print(f"XBrain {constants.VERSION}")
    messages = []
    while True:
        # 更新环境变量
        update_context()
        try:
            input_str = get_input("\033[;32m请输入你的需求！\033[0m")
        except EOFError:
            # 在input中输入 Ctrl + C 会触发 EOFError，这里需要捕获异常
            break
        messages.append({"role": "user", "content": input_str})
        res = run(messages)
        print(res)

if __name__ == "__main__":
    main()
  
