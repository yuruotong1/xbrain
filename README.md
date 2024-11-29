<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

让 Python 函数秒接入 AI

📘[详细文档](https://xbrain.notion.site/)|🎞️[介绍视频](https://www.bilibili.com/video/BV1c52FY4E51/?share_source=copy_web&vd_source=c28e503b050f016c21660b69e391d391)|🗨[English](https://github.com/yuruotong1/xbrain/blob/master/README_EN.md)

</div>

## 🤔解决了什么问题


如果你用LangChain开发Agent应用，需要以下四步：
1. 基础组件设置
2. 定义工具集
3. 定义Prompt模板
4. 定义输出解析器

<img src="./image/README/langchain开发步骤.png" style="background-color: white; padding: 10px;" />


如果你用swarm开发Agent应用，需要以下四步：
1. 基础组件设置
2. Agent角色定义
3. 任务协调系统
4. 工作流程实现

<img src="./image/README/swarm开发步骤.png" style="background-color: white; padding: 10px;" />


但是，如果你用xbrain开发Agent应用，一切将变得非常美好，只需要两步：
1. 在自己的函数上加入装饰器
2. 入口处配置并运行 xbrain



## 👥用户故事

- AI 接口封装： 独立 AI 函数快速封装为 HTTP 服务，便于集成到其他系统中；
- 功能验证： 早期开发阶段原型设计与测试，无需搭建复杂后端；
- 轻量化微服务改造： 适合将 Python 脚本微服务化，轻松满足小规模、灵活部署需求。


## ✨特点

- 一键安装，开箱即用： 命令行一键启动，简单易用；
- 无提示词设计： 摒弃提示词书写，用户专注于业务开发；
- 将python函数接入Tools Call： 将本地 Python 代码直接接入大模型的工具调用。

## 📄文档

- [快速开始：新手上手指南，适合第一次接触的开发者](https://xbrain.notion.site/xbrain-11d42182d0a98003b272d5555c6e9448)
- [常见问题：你想知道的答案都在这里](https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c)
- [开发者指南：欢迎加入我们](https://xbrain.notion.site/12842182d0a9803bb5dcdbfe71826915?pvs=4)

## Quick Start
在你的项目目录下创建一个`demo.py`文件，写入以下代码：
```python
from pydantic import BaseModel
from xbrain.core import xbrain_tool
class GenerateTag(BaseModel):
    """创建一个新的插件"""
    pass

@xbrain_tool.Tool(model=GenerateTag)
def generate_tag():
    print("hello")
```

在`__init__.py`文件中导入`demo.py`：

```python
from demo import *
```

在项目入口处配置并运行xbrain，此时`demo.py`中的`generate_tag`函数被成功接入了xbrain中：

```python
from xbrain.core.chat import run 
from xbrain.utils.config import Config
config = Config()
config.set_openai_config(base_url="https://api.openai-next.com/v1", api_key="xxxxx", model="gpt-4o-2024-08-06")
messages = []
messages.append({"role": "user", "content": "配置tag"})
res = run(messages, user_prompt="从文章中提炼出关键信息")
```

## 🤝 如何贡献

你可以通过 Fork 项目、提交 PR 或在 Issue 中提出你的想法和建议。具体操作可参考[贡献指南](https://xbrain.notion.site/12842182d0a9803bb5dcdbfe71826915)。


> 强烈推荐阅读 [《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)、[《如何向开源社区提问题》](https://github.com/seajs/seajs/issues/545) 和 [《如何有效地报告 Bug》](http://www.chiark.greenend.org.uk/%7Esgtatham/bugs-cn.html)、[《如何向开源项目提交无法解答的问题》](https://zhuanlan.zhihu.com/p/25795393)，更好的问题更容易获得帮助。

<a href="https://github.com/yuruotong1/xbrain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yuruotong1/xbrain" />
</a>

