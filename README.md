<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

xbrain 是一个智能插头

让开发者轻松将 Python 函数接入 AI 驱动的 HTTP 服务

📘[详细文档](https://xbrain.notion.site/)|🎞️[介绍视频](https://www.bilibili.com/video/BV1c52FY4E51/?share_source=copy_web&vd_source=c28e503b050f016c21660b69e391d391)|🗨[English](https://github.com/yuruotong1/xbrain/blob/master/README_EN.md)

</div>

## 🤔解决了什么问题

很多开发者在对接大模型时，面临接口调用复杂、函数接入困难的问题，开发完AI应用还需要额外开发 HTTP 服务等流程，效率低且容易出错。

xbrain 能够将任一 Python 函数通过 Tools Call 的方式接入 AI，并自动部署为 HTTP 服务，让复杂的功能即插即用，无需繁琐设置。

## 👥用户故事

- AI应用程序的接口封装：适合有独立 AI 函数的团队，通过 xbrain 一键封装成 HTTP 服务后，开发者能快速将 AI 功能接入其他系统，比如智能客服或推荐引擎。
- 原型设计与功能验证：适合产品早期开发阶段，通过将核心功能模块迅速部署为独立接口，便于团队内测试和反馈，不用搭建复杂的后端环境。
- 轻量化微服务改造：对于希望将某些 Python 脚本或独立功能微服务化的企业，xbrain 简化了脚本到 API 的过程，适用于小规模、灵活部署的场景。


## ✨特点

1. 开箱即用：在命令行一键安装，打开命令行即可使用；
2. 屏蔽了提示词，让用户专注于业务开发：用户无需编写提示词，就能开发大模型应用；
3. 用自然语言开发Tools call：通过自然语言将本地的 Python 代码接入到大模型的 Tools call；
4. 渐进式开发：无需额外修改代码就能接入 AI 驱动的 HTTP 服务。


## 📄文档

- [QuickStart](https://xbrain.notion.site/xbrain-11d42182d0a98003b272d5555c6e9448)
- [开发者文档](https://xbrain.notion.site/12842182d0a9803bb5dcdbfe71826915)
- [常见问题](https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c)

## **几个有意思的例子**

# 将任何加减操作映射成两数相加

通过xb定义一个加法函数：

```bash
I guess you want to do the following, or chat with me:

1. chat with my action
2. create a new action
3. deploy a chat server
4. integrate existing functions into xbrain

>>> 2
Please tell me, the action you want to do?
>>> 两数相加
Please wait a moment, I'm generating the code for you...
Creation successful!
file generated:  C:\Users\yuruo\Desktop\test2\add_action.py
```

add_action.py文件的内容：

```python
from xbrain import xbrain_tool
from pydantic import BaseModel, Field

class Add(BaseModel):
    """Add two numbers"""
    a: int = Field(..., description="First number")
    b: int = Field(..., description="Second number")

@xbrain_tool.Tool(model=Add)
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    return a + b
```

通过xbrain的chat mode可以实现两数相加：

```python
I guess you want to do the following, or chat with me:

1. chat with my action
2. create a new action
3. deploy a chat server
4. integrate existing functions into xbrain

>>> 1
Welcome to chat mode!
💬 1+1
run action：
 action name:  Add
 action path:  C:\Users\yuruo\Desktop\test2\add_action.py
 action arguments:  {'a': 1, 'b': 1}
 action result:  2

2
```

然而它也能实现两数相减：

```python
💬 1-1
run action：
 action name:  Add
 action path:  C:\Users\yuruo\Desktop\test2\add_action.py
 action arguments:  {'a': 1, 'b': -1}
 action result:  0

0
```

它还能实现三数相加减，虽然结果不对但我们看到了它的尝试，这也是我们优化的方向：

```python
💬 1+1+3
run action：
 action name:  Add
 action path:  C:\Users\yuruo\Desktop\test2\add_action.py
 action arguments:  {'a': 1, 'b': 1}
 action result:  2

run action：
 action name:  Add
 action path:  C:\Users\yuruo\Desktop\test2\add_action.py
 action arguments:  {'a': 1, 'b': 3}
 action result:  4

2
4
```

