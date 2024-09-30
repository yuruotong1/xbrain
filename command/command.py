from xbrain.main import run
from command.command_action import show_all_command
def main():
    print(" 很高兴在这里遇到您👋，我是xbrain，快和我聊聊天吧！")
    res = show_all_command()
    print(res)
    
    while True:
        input_str = input(">>> ")
        res = run([{"role": "user", "content": input_str}])
        print(res)
    
if __name__ == "__main__":
    main()