<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

极简的智能体开发框架。

</div>

## ✨特性

- 装饰器一键接入 Function Call（Pydantic 模型自动生成工具描述）
- 工作流 `Agent` 管线，按指定顺序编排执行
- 结构化响应解析：可传入 `response_format`（Pydantic）强类型返回

## 🧱环境要求

- Python ≥ 3.8
- 有效的 OpenAI API Key

## 📦安装

`pip install pyxbrain`

## 🚀快速开始：接入一个工具

在你的项目目录下创建一个 `demo.py` 文件：

```python
from pydantic import BaseModel
from xbrain.core import Tool

class GenerateTag(BaseModel):
    """生成标签的工具模型"""
    topic: str
    """要生成标签的主题"""

@Tool(model=GenerateTag)
def generate_tag(topic: str):
    return f"tag: {topic}"
```

在包的 `__init__.py` 文件中导入 `demo.py`：

```python
from demo import *
```

在项目入口处配置并运行 XBrain，此时 `demo.py` 中的 `generate_tag` 被成功接入：

```python
from xbrain.core import run
from xbrain.utils.config import Config

# 配置 OpenAI 信息（配置将保存在用户主目录下的 ~/.xbrain/config.yaml 文件中）
config = Config()
config.set_openai_config(
    base_url="https://api.openai.com/v1",
    api_key="YOUR_OPENAI_API_KEY",
    model="gpt-4o-2024-08-06",
)

messages = [{"role": "user", "content": "请为主题\“Python\”生成标签"}]
res = run(messages, user_prompt="你是一个能调用工具的助手")
print(res)
```

## 📐结构化响应（可选）

如果你希望模型严格返回某个结构，可以传入 `response_format`：

```python
from pydantic import BaseModel
from xbrain.core import run

class Summary(BaseModel):
    title: str
    keywords: list[str]

messages = [{"role": "user", "content": "请总结并给出关键词"}]
res = run(messages, user_prompt="结构化助手", response_format=Summary)
print(res)  # 返回满足 Summary 的内容
```

## 🧩工作流 Agent

使用 `@Agent(name)` 装饰器定义智能体节点，并通过 `WorkFlow` 类按顺序执行：

```python
from xbrain.core import Agent, WorkFlow

@Agent
class A:
    def run(self, input):
        return f"{input} -> 处理后的数据A"

@Agent
class B:
    def run(self, input):
        return f"{input} -> 处理后的数据B"

# 创建工作流并指定执行顺序
workflow = WorkFlow([A, B])

# 执行工作流
result = workflow.run("起始输入")
print(result)  # "起始输入 -> 处理后的数据A -> 处理后的数据B"
```

## ⚙️配置文件位置

- 使用 `xbrain.utils.config.Config` 管理配置
- 配置文件写入到用户目录：`~/xbrain/config.yaml`
- 也可通过 `config.set_openai_config(base_url, api_key, model)` 动态设置并持久化

## 🤝如何贡献

你可以通过 Fork 项目、提交 PR 或在 Issue 中提出你的想法和建议。具体操作可参考 [贡献指南](https://xbrain.notion.site/12842182d0a9803bb5dcdbfe71826915)。

> 建议阅读 [《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)、[《如何向开源社区提问题》](https://github.com/seajs/seajs/issues/545)、[《如何有效地报告 Bug》](http://www.chiark.greenend.org.uk/%7Esgtatham/bugs-cn.html) 与 [《如何向开源项目提交无法解答的问题》](https://zhuanlan.zhihu.com/p/25795393)。

<a href="https://github.com/yuruotong1/xbrain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yuruotong1/xbrain" />
</a>

