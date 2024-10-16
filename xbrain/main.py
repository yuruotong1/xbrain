from xbrain import context
from xbrain.chat import run
from xbrain.command.help_action import get_command_map, show_all_command
import signal
import sys
from xbrain.utils import constant
from xbrain.utils.import_utils import import_action
from xbrain.utils.config import Config
import os

def signal_handler(sig, frame):
    print("Nice to meet you here!")
    sys.exit(0)

def check_config():
    config = Config()
    if config.OPENAI_API_KEY == "":
        print(f"XBrain relies on the OpenAI API,please config in below path:\n{config.config_path}.\n\nIf you have problem, please refer to: \nhttps://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c#f85f9774b40c4b63bc6ec28fd11a2dde")
        sys.exit(1)
    elif not config.OPENAI_BASE_URL.endswith("/v1"):
        print(f"base_url should end with `/v1`, current configuration is `{config.OPENAI_BASE_URL}`. Please modify and rerun. Configuration file path:\n{config.config_path}")
        sys.exit(1)

def update_context():
    if os.path.exists(constant.CONFIG_NAME):
        context.set_context(Type.IS_XBRAIN_PROJECT, True)
    else:
        context.set_context(Type.IS_XBRAIN_PROJECT, False)

def main():
    import_action()
    check_config()
    # 捕获 Ctrl + C 信号，进行更优雅的退出
    signal.signal(signal.SIGINT, signal_handler)
    # 将所有命令映射成数字，如果用户回复了数字且命中，则执行对应命令
    command_map = get_command_map()
    while True:
        update_context()
        show_all_command()
        try:
            input_str = input(">>> ")
        except EOFError:
            break
        if input_str in command_map:
            command_map[input_str]()
        else:
            res = run([{"role": "user", "content": input_str}], chat_model=False)
            print(res)
        
if __name__ == "__main__":
    main()