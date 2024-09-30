from xbrain.main import run
from command.help_action import get_command_map, show_all_command
import signal
import sys

def signal_handler(sig, frame):
    print("\n很高兴在这里遇到您👋，期待下次再见！")
    sys.exit(0)

def main():
    print(" 很高兴在这里遇到您👋，我是xbrain，快和我聊聊天吧！")
    res = show_all_command()
    print(res)
    
    signal.signal(signal.SIGINT, signal_handler)  # 捕获 Ctrl + C 信号
    command_map = get_command_map()
    while True:
        input_str = input(">>> ")
        if input_str == "exit":
            break
        elif input_str in command_map:
            res = command_map[input_str]()
            print(res)
        else:
            res = run([{"role": "user", "content": input_str}])
            print(res)
    
if __name__ == "__main__":
    main()