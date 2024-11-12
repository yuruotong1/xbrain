# todo，需要改成变量，这样无法知道哪些被引用了哪些没被引用（相关代码被删除了）
translations = {
    "\033[;32mcurrent workspace: {cwd}\033[0m": "\033[;32m当前所在文件夹路径: {cwd}\033[0m",
    "I guess you want to do the following, or chat with me:\n\n": "有什么能帮到你的吗？还是随便聊聊？\n\n",
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
    "create a new action": "给xbrain增加新的智能工具",
    "Generate a tree of a directory": "为文件夹生成树形结构",
    "extract a file to structured JSON": "把文件内容提取为JSON格式",
    "XBrain relies on the OpenAI API,please config in below path:\n{config_path}.\n\nIf you have problem, please refer to: \n"
    "https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c#f85f9774b40c4b63bc6ec28fd11a2dde": 
    "XBrain 依赖于 OpenAI API，请在以下路径配置：\n{config_path} \n\n如果遇到问题，请参考：\n"
    "https://xbrain.notion.site/b274c33d808a4ddea32244c3fd41719c#f85f9774b40c4b63bc6ec28fd11a2dde",
    "Start a chat with xbrain": "部署网页版交互界面",
    "Stores embedding of text into vectorstore database": "把文档存入向量数据库",
    "Return top 3 matched text results based on query embedding": "返回向量数据库的查询结果"

}

def _(string, lang="zh", **kwargs): # lang needs to be a global in the future
    text = translations.get(string, string) if lang == "zh" else string
    return text.format(**kwargs)