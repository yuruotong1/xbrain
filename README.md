<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

极简的智能体开发框架。

</div>

## ✨特性

- 装饰器一键接入 Function Call（Pydantic 模型自动生成工具描述）
- 工作流 `Agent` 管线，按指定顺序编排执行
- 智能体间全局上下文共享
- 结构化响应解析：可传入 `response_format`（Pydantic）强类型返回

## 🧱环境要求

- Python ≥ 3.8
- 有效的 OpenAI API Key

## 📦安装

```bash
pip install pyxbrain
```

## 🚀快速开始：接入一个工具

### 1. 创建工具文件

在你的项目目录下创建一个 `demo.py` 文件，定义工具函数：

```python
from pydantic import BaseModel
from xbrain.core import Tool

class GenerateTag(BaseModel):
    """生成标签的工具模型"""
    topic: str
    """要生成标签的主题"""

@Tool(model=GenerateTag)
def generate_tag(topic: str):
    """生成标签的工具函数"""
    return f"tag: {topic}"
```

### 2. 配置 OpenAI

在项目入口处配置并运行 XBrain：

```python
from xbrain.core import run
from xbrain.utils.config import Config
from demo import *  # 导入工具定义

# 配置 OpenAI 信息（配置将保存在用户主目录下的 ~/.xbrain/config.yaml 文件中）
config = Config()
config.set_openai_config(
    base_url="https://api.openai.com/v1",  # 或其他兼容的 API 端点
    api_key="YOUR_OPENAI_API_KEY",
    model="gpt-4o-2024-08-06",
)

# 调用 run 函数与智能体交互
messages = [{"role": "user", "content": "请为主题\“Python\”生成标签"}]
response = run(messages, user_prompt="你是一个能调用工具的助手")
print(response)
```

## 📐结构化响应（可选）

如果你希望模型严格返回某个结构，可以传入 `response_format` 参数（Pydantic 模型）：

```python
from pydantic import BaseModel
from xbrain.core import run
from xbrain.utils.config import Config

# 配置 OpenAI（首次使用需要）
config = Config()
config.set_openai_config(
    base_url="https://api.openai.com/v1",
    api_key="YOUR_OPENAI_API_KEY",
    model="gpt-4o-2024-08-06",
)

# 定义响应结构
class Summary(BaseModel):
    title: str
    """总结的标题"""
    keywords: list[str]
    """总结的关键词列表"""

# 发送消息并指定响应格式
messages = [{"role": "user", "content": "请总结：Python 是一种广泛使用的解释型、高级和通用的编程语言。它支持多种编程范式，包括结构化、面向对象和函数式编程。Python 被设计为易于阅读和编写，具有简洁的语法。"}]
response = run(messages, user_prompt="结构化助手", response_format=Summary)
print(f"标题: {response.title}")
print(f"关键词: {response.keywords}")
```

## 🧩工作流 Agent

通过继承 `Agent` 类定义智能体节点，并通过 `WorkFlow` 类按顺序执行：

```python
from xbrain.core import Agent, WorkFlow

class A(Agent):
    def run(self, input):
        return f"{input} -> 处理后的数据A"

class B(Agent):
    def run(self, input):
        return f"{input} -> 处理后的数据B"

# 创建工作流并指定执行顺序
workflow = WorkFlow(A, B)  # 可以接受多个 Agent 类作为位置参数

# 执行工作流
result = workflow.run("起始输入")
print(result)  # {"A": "起始输入 -> 处理后的数据A", "B": "起始输入 -> 处理后的数据A -> 处理后的数据B"}
```

### 工作流的多种创建方式

WorkFlow 支持多种创建方式：

```python
from xbrain.core import Agent, WorkFlow

class A(Agent):
    def run(self, input):
        return f"{input} -> A"

class B(Agent):
    def run(self, input):
        return f"{input} -> B"

# 方式1：接受单个 Agent 类
workflow1 = WorkFlow(A)

# 方式2：接受多个 Agent 类作为位置参数
workflow2 = WorkFlow(A, B)

# 方式3：接受 Agent 类列表
workflow3 = WorkFlow([A, B])
```

### 全局上下文共享

WorkFlow 支持智能体间的全局上下文共享，通过 `self.global_context` 可以在不同智能体间传递数据：

```python
from xbrain.core import Agent, WorkFlow

class A(Agent):
    def run(self, input):
        # 在全局上下文中存储数据
        self.global_context["a"] = "a"
        return "agent1 输出"

class B(Agent):
    def run(self):
        # 从全局上下文中获取数据，不需要 input 参数
        return self.global_context["a"]

workflow = WorkFlow(A, B)
result = workflow.run("test input")
print(result)  # {"A": "agent1 输出", "B": "a"}
```

### 向工作流传递参数

你可以向 WorkFlow 的 `run` 方法传递额外参数，这些参数会被传递给第一个 Agent 的 `run` 方法：

```python
from xbrain.core import Agent, WorkFlow

class A(Agent):
    def run(self, input, arg1, arg2):
        return f"{input} {arg1} {arg2}"

class B(Agent):
    def run(self, input):
        return f"agent2 输出 {input}"

workflow = WorkFlow(A, B)
result = workflow.run("test input", "arg1", "arg2")
print(result)  # {"A": "test input arg1 arg2", "B": "agent2 输出 test input arg1 arg2"}
```

### 获取每个 Agent 的执行结果

WorkFlow.run() 方法直接返回一个字典，包含每个 Agent 的执行结果：

```python
from xbrain.core import Agent, WorkFlow

class A(Agent):
    def run(self, input):
        return f"{input} a"

class B(Agent):
    def run(self, input):
        return f"{input} b"

workflow = WorkFlow(A, B)
result = workflow.run("test input")
print(result["A"])  # "test input a"
print(result["B"])  # "test input a b"
```

### 在 Agent 中使用大模型

你可以在 Agent 中使用 `chat` 函数与大模型交互：

```python
from xbrain.core import Agent, WorkFlow
from xbrain.utils.openai_utils import chat

class A(Agent):
    def run(self, input):
        res = chat([{"role": "user", "content": input}], "你是一个智能助手")
        return res

# 创建包含单个 Agent 的工作流
workflow = WorkFlow(A)
result = workflow.run("你好")
print(result)  # {"A": "你好！有什么我可以帮助你的吗？"}

# 多个 Agent 示例
class B(Agent): 
    def run(self, input):
        res = chat([{"role": "user", "content": input}], "你是一个智能助手")
        return res

workflow2 = WorkFlow(A, B)
result2 = workflow2.run("你好")
print(result2)  # {"A": "你好！有什么我可以帮助你的吗？", "B": "你好！有什么我可以帮助你的吗？"}
```

## ⚙️配置管理

XBrain 使用 `Config` 类管理配置信息，配置将保存在用户主目录下的 `~/.xbrain/config.yaml` 文件中。

### 配置 OpenAI

```python
from xbrain.utils.config import Config

config = Config()
config.set_openai_config(
    base_url="https://api.openai.com/v1",  # API 端点
    api_key="YOUR_OPENAI_API_KEY",  # 你的 API Key
    model="gpt-4o-2024-08-06",  # 使用的模型
)
```

### 获取当前配置

```python
from xbrain.utils.config import Config

config = Config()
# 通过属性直接获取配置
print(f"当前模型: {config.OPENAI_MODEL}")
print(f"API 端点: {config.OPENAI_BASE_URL}")

# 或通过 load_config() 方法获取完整配置
full_config = config.load_config()
print(f"OpenAI 配置: {full_config['openai']}")
```

## 🤝如何贡献

你可以通过 Fork 项目、提交 PR 或在 Issue 中提出你的想法和建议。具体操作可参考 [贡献指南](https://xbrain.notion.site/12842182d0a9803bb5dcdbfe71826915)。

> 建议阅读 [《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)、[《如何向开源社区提问题》](https://github.com/seajs/seajs/issues/545)、[《如何有效地报告 Bug》](http://www.chiark.greenend.org.uk/%7Esgtatham/bugs-cn.html) 与 [《如何向开源项目提交无法解答的问题》](https://zhuanlan.zhihu.com/p/25795393)。

<a href="https://github.com/yuruotong1/xbrain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yuruotong1/xbrain" />
</a>

