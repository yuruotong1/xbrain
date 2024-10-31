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

## 几个有意思的例子

### 智能客服系统
利用 xbrain 将自然语言处理模型接入为服务，创建智能应答机器人，用于自动化客服回答，提高响应速度和质量。


### 实时数据分析
使用 xbrain 快速部署数据分析模型，如实时交易数据分析，帮助金融机构监控和分析交易异常，提升风险管理能力。

### 内容推荐系统
通过 xbrain 将推荐算法封装为 HTTP 服务，快速集成到电商或媒体网站中，实现个性化内容推荐，增强用户体验。

### 健康诊断服务
医疗应用中，利用 xbrain 部署疾病诊断模型，通过 HTTP 接口提供远程诊断服务，支持医生和患者快速获取诊断结果。

### 教育与学习辅助
将教育软件中的解题或语言学习模型通过 xbrain 接入，提供实时学习支持和反馈，增强学习体验和效果。

