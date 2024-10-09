<div align="center"><aname="readme-top">

<img src="./image/README/logo.png" width="120" height="120" alt="XBrain">
<h1>XBrain</h1>

An open-source function-as-intelligence architecture.

🎞️[Introduction Video](https://www.bilibili.com/video/BV1c52FY4E51/?share_source=copy_web&vd_source=c28e503b050f016c21660b69e391d391)|🗨[Chinese](https://github.com/yuruotong1/xbrain/blob/master/README.md)

</div>

We aim to enable any developer to quickly harness large models.

We focus on building agentless architectures, similar to serverless, where developers don't need to worry about underlying Agents, and can instantly make a regular function intelligent.

## ✨Features

* 🌈 Easily make regular functions intelligent: Quickly empower your functions with AI capabilities, enhancing application performance.
* 🔍 Intelligent code generation through chat interface: Interact with the system conversationally to accelerate development.
* 📦 One-click deployment of chat server: Quickly go live, allowing users to experience your intelligent features promptly.

## 🖥 Who are the competitors?

- LangChain
- Coze
- Dify

## ⌨️ Who would need this?

**Who are the customers?**

1. Small B companies with traditional internet businesses lacking professional Agent developers, hoping to expand new businesses through AI;
2. Developers familiar with basic Python syntax who don't understand Agents but wish to leverage large models to accelerate business development.

**Customer Stories**

1. Company A ran an initial demo on Coze/LangChain and found during commercialization that the user experience was poor, and users were unwilling to pay. Unfortunately, the company lacked talent in Agents, so A could only have programmers work overtime to modify plugin code to handle each exception. As the business grew, this became increasingly common. They then used xbrain for reconstruction and discovered that the AI execution process was controllable. Developers didn't need to frequently modify plugins to provide users with an excellent experience.
2. Company B wanted to leverage AI to accelerate business requirements but lacked personnel familiar with AI. The learning cost of LangChain was high, so they adopted the xbrain framework and quickly integrated by conversing with AI.

---

## 🍬Usage Guide

Install the latest version using `pip install -U pyxbrain`. After installation, enter `xb` in the command line to start a conversation.

### Easily Make Regular Functions Intelligent

By conversing with xbrain in the terminal and selecting `ConvertAction`, you can transform any regular Python function into an action recognizable by xbrain.

![convert](./image/README/xbrain_convert.gif)

### Intelligent Code Generation Through Chat Interface

By conversing with xbrain in the terminal and selecting `CreateAction`, input your requirements to intelligently generate actions from scratch and automatically integrate them into xbrain.

![img](./image/README/xbrain_create.gif)

### One-Click Deployment of Chat Server

By conversing with xbrain in the terminal and selecting `deploy`, you can deploy a chat server with one click, which can be interacted with via API.

![img](./image/README/xbrain_deploy.gif)

## 🤝Frequently Asked Questions

1. If entering `xb` prompts: "'xb' is not recognized as an internal or external command, operable program or batch file." You need to add Python's Scripts directory to your environment variables.
