from xbrain.main import run
from xbrain.command.help_action import get_command_map, show_all_command
import signal
import sys

from xbrain.utils.config import Config

def signal_handler(sig, frame):
    print("\n很高兴在这里遇到您👋，期待下次再见！")
    sys.exit(0)

def check_config():
    config = Config()
    if config.OPENAI_API_KEY == "":
        print(f"xbrain依赖于 OPENAI API，请在配置文件中配置好 OPENAI 相关信息！配置文件路径：\n{config.config_path}")
        sys.exit(1)
    elif not config.OPENAI_BASE_URL.endswith("/v1"):
        print(f"base_url应该以`/v1`结尾，当前配置为`{config.OPENAI_BASE_URL}`，请修改后重新运行，配置文件地址\n{config.config_path}")
        sys.exit(1)

def main():
    check_config()
    print(" 很高兴在这里遇到您👋，我是xbrain，快和我聊聊天吧！")
    show_all_command()
    signal.signal(signal.SIGINT, signal_handler)  # 捕获 Ctrl + C 信号
    command_map = get_command_map()
    while True:
        try:
            input_str = input(">>> ")
        except EOFError:
            break
        if input_str == "exit":
            break
        elif input_str in command_map:
            command_map[input_str]()
        else:
            res = run([{"role": "user", "content": input_str}])
            print(res)
    
if __name__ == "__main__":
    main()