#!/bin/bash

# 1. 在用户根目录创建xbrain文件夹
cd ~
mkdir -p xbrain
echo "xbrain folder created in the home directory."

# 2. 检查系统Python版本是否大于3.8
PYTHON_VERSION=$(python3 -c 'import sys; print(sys.version_info[:2])' | tr -d '(), ')
if [[ "$PYTHON_VERSION" < "3 8" ]]; then
    echo "Python version is less than 3.8. Please install Python 3.8 or higher from https://www.python.org/downloads/"
    exit 1
else
    echo "Python version is $PYTHON_VERSION. No need to install Python."
fi

# 3. 在xbrain文件夹中创建Python虚拟环境
cd ~/xbrain
if [[ ! -d ".xbrain" ]]; then
    python3 -m venv .xbrain
    echo "Python virtual environment created in ~/xbrain/.xbrain."
else
    echo "Virtual environment already exists. Skipping creation."
fi

# 4. 激活虚拟环境
source .xbrain/bin/activate
echo "Virtual environment activated."

# 5. 更新pip
pip install --upgrade pip
echo "pip upgraded."

# 6. 安装pyxbrain
pip install pyxbrain
echo "pyxbrain installed."

# 7. 运行xb
echo 'running xbrain'
xb
