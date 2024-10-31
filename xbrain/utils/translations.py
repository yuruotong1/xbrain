translations = {
    "Welcome to chat mode!": "欢迎来到聊天模式！",
    "\nExiting chat mode, looking forward to seeing you again!": "\n退出聊天模式，祝您生活愉快！",
    "please input the workspace path": "想把xbrain用在哪个文件夹呢？请输入路径。",
    "\033[;32mcurrent workspace: {cwd}\033[0m": "\033[;32m当前所在文件夹路径: {cwd}\033[0m",
    "Service started, chat at: http://127.0.0.1:{port}/chat": 
    "服务已启动，可以通过向 http://127.0.0.1:{port}/chat 发送POST请求来对话了。",
    "I guess you want to do the following, or chat with me:\n\n": "有什么能帮到你的吗？还是随便聊聊？\n\n",
    "success init xbrain project!": "xbrain已经成功读取当前项目！",
    "The following .py files were found: \n": "找到了这些Python文件：\n",
    "\nWhich file would you like to operate on? \n>>> ": "\n想把哪个文件智能化呢？\n>>> ",
    "You have selected the file:": "被选中的文件：",
    "Which function would you like to convert? \n": "想把哪个函数智能化呢？\n",
    "Conversion successful, file generated:": "智能化成功，生成的文件在：",
    "Parsing failed": "解析失败。",
    "Creation successful!\nfile generated: ": "生成成功！\n生成的文件在这里：",
    "\nNice to meet you here!": "\n期待与您再见！",
    "init this directory as a xbrain project": "把当前文件夹读取为xbrain项目",
    "integrate existing functions into xbrain": "把已有的函数升级为xbrain智能工具",
    "Show all capabilities": "列举所有能力",
    "deploy a chat server": "部署聊天服务器",
    "change workspace": "更改工作文件夹路径",
    "chat with my action": "和已有的xbrain智能工具交流",
    "create a new action": "给xbrain增加新的智能工具",
    
    "XBrain relies on the OpenAI API,please config in below path:\n{config_path}.\n\nIf you have problem, please refer to: \n"
    "https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c#f85f9774b40c4b63bc6ec28fd11a2dde": 
    "XBrain 依赖于 OpenAI API，请在以下路径配置：\n{config_path}。\n\n如果遇到问题，请参考：\n"
    "https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c#f85f9774b40c4b63bc6ec28fd11a2dde"
}

def _(string, lang="zh", **kwargs): # lang needs to be a global in the future
    text = translations.get(string, string) if lang == "zh" else string
    return text.format(**kwargs)