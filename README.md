<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

xbrain是一个AI漏斗，把巨量用户行为模式映射到少量特定入口。

📘[详细文档](https://xbrain.notion.site/)|🎞️[介绍视频](https://www.bilibili.com/video/BV1c52FY4E51/?share_source=copy_web&vd_source=c28e503b050f016c21660b69e391d391)|🗨[English](https://github.com/yuruotong1/xbrain/blob/master/README_EN.md)

</div>

## ✨特点

1. 开箱即用：在命令行一键安装，打开命令行即可使用；
2. 屏蔽了提示词，让用户专注于业务开发：用户无需编写提示词，就能开发大模型应用；
3. 用自然语言开发function call：通过自然语言将本地的python代码接入到openai的function call；
4. 渐进式开发：对用户代码无侵入性。


## 文档

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

