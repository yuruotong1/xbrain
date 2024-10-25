import os
import importlib
import sys
from xbrain.xbrain_tool import clear_tools,tools

def import_action():
    # 清空已有模块
    clear_tools()
    # 动态导入用户模块
    current_dirs = [os.getcwd()]
    for current_dir in current_dirs:
        for root, dirs, files in os.walk(current_dir):
            if is_venv_dir(root):
                dirs[:] = []  # 清空 dirs 列表，避免进入虚拟环境目录的子目录
                continue
            for file in files:
                if file.endswith('.py') and file not in ['__init__.py', 'setup.py']:
                    module_name = file[:-3]
                    module_path = os.path.join(root, file)
                    # 如果文件中没有 @xbrain_tool.Tool'
                    with open(module_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if '@xbrain_tool.Tool' not in content:
                            continue  
                    # 动态导入模块
                    run_module(module_name, module_path)

def run_module(module_name, module_path):
     # 动态导入模块
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


def is_venv_dir(path):
    return os.path.isfile(os.path.join(path, 'pyvenv.cfg'))
