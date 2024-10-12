<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

Chat with XBrain, and it will generate integration code for you without the need to focus on specific details.

极简agent开发框架

[🎞️]()[介绍视频](https://www.bilibili.com/video/BV1c52FY4E51/?share_source=copy_web&vd_source=c28e503b050f016c21660b69e391d391)|🗨[English](https://github.com/yuruotong1/xbrain/blob/master/README_EN.md)

</div>

## ✨特点

* 🌈自动分析已有代码，集成进AI。
* 🔍与xbrain聊天，生成代码并集成进AI。
* 📦一键部署聊天服务器。


## ⌨️谁会需要？

1. 拥有传统互联网业务的小B公司，希望通过AI扩展新业务；
2. 掌握python基础语法的开发人员，希望将功能集成进大模型。

## 🍬使用指南

使用 `pip install -U pyxbrain`安装最新版本，安装完成后，在命令行输入 `xb` 即可开启对话。

### 自动分析已有代码，集成进AI

通过在终端与xbrain进行对话，选择 `ConvertAction`，将任意一个普通的python函数转变为xbrain可识别的action。

![convert](./image/README/xbrain_convert.gif)

### 与xbrain聊天，生成代码并集成进AI

通过在终端与xbrain进行对话，选择 `CreateAction`，输入你的需求，从0到1智能生成action，自动接入xbrain。

![img](./image/README/xbrain_create.gif)

### 一键部署聊天服务器

通过在终端与xbrain进行对话，选择 `deploy`，一键部署为chat server，可通过api与之对话。

![img](./image/README/xbrain_deploy.gif)
