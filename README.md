## 介绍

xbrain 是一款可解释的AI开发框架。

我们在做大模型的CT，让普通开发者都能驾驭大模型，互联网企业都能开展稳定的AI业务。

## 特点

1. 普通python函数秒变智能；
2. 0学习成本0安装，在终端与xbrain聊天为编程赋能；
3. 本地serverless，将任一函数部署为AI server。

## 使用指南

使用 `pip install -U pyxbrain`安装最新版本，安装完成后，在命令行输入 `xb`即可进入圣诞。

## 常见问题

1. 如果输入 `xb` 时提示：“'xb' 不是内部或外部命令，也不是可运行的程序或批处理文件”。你需要把python的Scripts目录设置在环境变量下。

## 开发指南

打包成 whl 文件：

```
py -m pip install --upgrade build
py -m build
```

在 `C:\Users\用户名`下的 `.pypirc`文件配置基本信息：

```
[distutils]
index-servers = pypi
[pypi]
#测试环境
repository = https://upload.pypi.org/legacy/
username = __token__
password = token
```

上传到官方：

`py -m twine upload dist/*`
