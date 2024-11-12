<div align="center"><a name="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>


让 Python 函数变身为 AI 驱动的 HTTP 服务

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
1. 编写工具
2. 与AI聊天部署运行

<img src="./image/README/xbrain开发步骤.png" style="background-color: white; padding: 10px;" />



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

## 几个有意思的例子

### 智能客服系统
使用 NLP 模型构建智能应答机器人，优化客服效率。
Todo 待完善。
<!-- ### 实时数据分析
使用 xbrain 快速部署数据分析模型，如实时交易数据分析，帮助金融机构监控和分析交易异常，提升风险管理能力。

### 内容推荐系统
通过 xbrain 将推荐算法封装为 HTTP 服务，快速集成到电商或媒体网站中，实现个性化内容推荐，增强用户体验。

### 健康诊断服务
医疗应用中，利用 xbrain 部署疾病诊断模型，通过 HTTP 接口提供远程诊断服务，支持医生和患者快速获取诊断结果。

### 教育与学习辅助
将教育软件中的解题或语言学习模型通过 xbrain 接入，提供实时学习支持和反馈，增强学习体验和效果。
 -->

## 🤝 如何贡献

你可以通过 Fork 项目、提交 PR 或在 Issue 中提出你的想法和建议。具体操作可参考[贡献指南](https://xbrain.notion.site/12842182d0a9803bb5dcdbfe71826915)。


> 强烈推荐阅读 [《提问的智慧》](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)、[《如何向开源社区提问题》](https://github.com/seajs/seajs/issues/545) 和 [《如何有效地报告 Bug》](http://www.chiark.greenend.org.uk/%7Esgtatham/bugs-cn.html)、[《如何向开源项目提交无法解答的问题》](https://zhuanlan.zhihu.com/p/25795393)，更好的问题更容易获得帮助。

<a href="https://github.com/yuruotong1/xbrain/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yuruotong1/xbrain" />
</a>

