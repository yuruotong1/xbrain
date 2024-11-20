from pydantic import BaseModel, Field
from xbrain.core import xbrain_tool
import os
import importlib
import sys

class XBrainLoadUserPluginModel(BaseModel):
    """加载用户插件"""
    plugin_path: str = Field(description="插件路径")

@xbrain_tool.Tool(model=XBrainLoadUserPluginModel)
def load_user_plugin(plugin_path: str):
    import_action(plugin_path)



def import_action(current_dir):
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
    print(f"成功加载插件: {module_name}")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)


def is_venv_dir(path):
    return os.path.isfile(os.path.join(path, 'pyvenv.cfg'))