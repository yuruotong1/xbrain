import sys
import os
# 一般编译器不会把 xbrain 目录加入 PYTHONPATH，所以需要手动添加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
from xbrain.core.chat import prepare_openai_tools, process_chat_response
from xbrain.plugin.help_action import get_command_map, show_all_command
import signal
from xbrain.core.context import context, ActionRecord
from xbrain.core.context import Type
from xbrain.utils.config import Config, Constants
from xbrain.core.context import update_context
from xbrain.utils.import_utils import import_action
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
    # todo 在 home 目录下创建 .xbrain 目录，用于存放代码、yaml
    constants = Constants()
    signal.signal(signal.SIGINT, signal_handler)
    print(f"XBrain {constants.VERSION}")
    import_action()
    while True:
        print(f"\033[;32mcurrent workspace: {os.getcwd()}\033[0m\n-------\n\n")
        # 更新环境变量
        update_context()
        show_all_command()
        # 将所有命令映射成数字，如果用户回复了数字且命中，则执行对应命令
        command_map = get_command_map()
        try:
            input_str = get_input()
        except EOFError:
            # 为什么这里要抓EOF？
            break
        if input_str in command_map:
            command_map[input_str]()
        else: # 说是随便聊聊 但是其实这里开的是全部功能
            # 这里xbrain就知道自己是谁了
            # 说实话有点奇怪
            chat_response = prepare_openai_tools(
                [{"role": "user", "content": input_str}], 
                user_prompt="You are xbrain, a powerful AI agent framework.", 
                chat_mode=False)
            # 将所有工具调用记录下来，用于AI预测用户后续行为
            for tool_call in chat_response.tool_calls:
                context[Type.PRE_ACTIONS].append(ActionRecord(tool_call.function.name, json.loads(tool_call.function.arguments)))
            res = process_chat_response(chat_response)
            print(res)
        
if __name__ == "__main__":
    main()
  
