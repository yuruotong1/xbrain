import json
from xbrain.chat import prepare_openai_tools, process_chat_response
from xbrain.command.help_action import get_command_map, show_all_command
import signal
import sys
from xbrain.context import context, ActionRecord
from xbrain.context import Type
from xbrain.utils.config import Config
from xbrain.context import update_context
from xbrain.utils.import_utils import import_action

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


def main(): 
    check_config()
    # 捕获 Ctrl + C 信号，进行更优雅的退出
    signal.signal(signal.SIGINT, signal_handler)
    import_action()
    while True:
        # 更新环境变量
        update_context()
        show_all_command()
        # 将所有命令映射成数字，如果用户回复了数字且命中，则执行对应命令
        command_map = get_command_map()
        try:
            input_str = input(">>> ")
        except EOFError:
            break
        if input_str in command_map:
            command_map[input_str]()
        else:
            chat_response = prepare_openai_tools([{"role": "user", "content": input_str}], chat_model=False)
            # 将所有工具调用记录下来，用于AI预测用户后续行为
            for tool_call in chat_response.tool_calls:
                context[Type.PRE_ACTIONS].append(ActionRecord(tool_call.function.name, json.loads(tool_call.function.arguments)))
            res = process_chat_response(chat_response)
            print(res)
        
if __name__ == "__main__":
    main()