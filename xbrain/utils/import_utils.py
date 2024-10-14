import os
import importlib
import sys

def import_action():
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        if is_venv_dir(root):
            dirs[:] = []  # 清空 dirs 列表，避免进入虚拟环境目录的子目录
            continue
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                module_name = file[:-3]
                module_path = os.path.join(root, file)
                # 动态导入模块
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

def is_venv_dir(path):
    return os.path.isfile(os.path.join(path, 'pyvenv.cfg'))
