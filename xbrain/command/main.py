from xbrain.main import run
from xbrain.command.help_action import get_command_map, show_all_command
import signal
import sys

from xbrain.utils.config import Config

def signal_handler(sig, frame):
    print("\nNice to meet you here 👋, looking forward to seeing you next time!")
    sys.exit(0)

def check_config():
    config = Config()
    if config.OPENAI_API_KEY == "":
        print(f"xbrain relies on the OpenAI API, please configure the OpenAI-related information in the configuration file! Configuration file path:\n{config.config_path}")
        sys.exit(1)
    elif not config.OPENAI_BASE_URL.endswith("/v1"):
        print(f"base_url should end with `/v1`, current configuration is `{config.OPENAI_BASE_URL}`. Please modify and rerun. Configuration file path:\n{config.config_path}")
        sys.exit(1)

def main():
    check_config()
    print("Nice to meet you here 👋, I'm xbrain, let's chat!")
    show_all_command()
    signal.signal(signal.SIGINT, signal_handler)  # Capture Ctrl + C signal
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
            res = run([{"role": "user", "content": input_str}], chat_model=False)
            print(res)
        
if __name__ == "__main__":
    main()