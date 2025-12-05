import chainlit as cl
import subprocess
import sys
import os

class AgentUI:
    def __init__(self, *workflow_list):
        """
        初始化 UI 框架
        :param workflow_list: 你的业务逻辑实例，或者是需要传递的数据
        """
        self.workflow_list = workflow_list
        
        # === 核心魔法 1: 注册回调 ===
        # 只有当代码被 Chainlit 加载时，这些注册才真正生效
        cl.on_message(self.process_message)
        cl.on_chat_start(self.on_chat_start)

    async def on_chat_start(self):
        """聊天开始时的逻辑"""
        # 注意：这里 self.workflow_list 是你在 init 传入的
        workflows_name = [str(w.__class__.__name__) for w in self.workflow_list]
        commands = [{"id": w.__class__.__name__, "icon": "play", "description": f"运行 {w.__class__.__name__}"} for w in self.workflow_list]
        # 注册命令
        await cl.context.emitter.set_commands(commands)
        await cl.Message(
            content=f"👋 欢迎！框架已启动，检测到 {len(self.workflow_list)} 个工作流。\n列表: {workflows_name}"
        ).send()

    async def process_message(self, message: cl.Message):
        """处理消息的主逻辑"""
        user_input = message.content
        # 模拟调用
        print(cl.chat_context.to_openai())
        res = self.workflow_list[0].run()
        await cl.Message(
            content=f"{res}",
        ).send()

    # === 核心魔法 2: 启动器 ===
    def launch(self):
        """
        让用户可以直接运行 Python 文件，而不需要输入 chainlit run
        """
        # 获取当前运行的脚本路径
        file_path = sys.argv[0]
        
        # 检查是否已经在 Chainlit 环境中运行（避免死循环）
        # Chainlit 运行时会设置特定的环境变量，或者通过 sys.argv 也能判断
        if "chainlit" in sys.modules and os.environ.get("CHAINLIT_PORT"):
            # 如果已经在 Chainlit 环境下，什么都不做，单纯只是初始化类
            return
        
        print(f"🚀 正在启动 Chainlit 服务: {file_path} ...")
        
        # 构建命令行指令：chainlit run your_script.py -w
        # -w 表示 watch 模式（代码修改自动重载），不需要可以去掉
        cmd = ["chainlit", "run", file_path, "-w", "--port", "8000"]
        
        try:
            # 调用系统的 chainlit 命令
            subprocess.run(cmd)
        except KeyboardInterrupt:
            print("已停止服务")