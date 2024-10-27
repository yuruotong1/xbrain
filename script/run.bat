@echo off

REM 1. 在用户根目录创建xbrain文件夹
cd %HOMEPATH%
if not exist xbrain (
    mkdir xbrain
    echo xbrain folder created in the home directory.
) else (
    echo xbrain folder already exists.
)

REM 2. 检查系统Python版本是否大于3.8
for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo %PYTHON_VERSION% | findstr /r "3\.[8-9]" >nul
if errorlevel 1 (
    echo Python version is less than 3.8. Please install Python 3.8 or higher from https://www.python.org/downloads/
    exit /b 1
) else (
    echo Python version is %PYTHON_VERSION%. No need to install Python.
)

REM 3. 在xbrain文件夹中创建Python虚拟环境
cd %HOMEPATH%\xbrain
if not exist ".venv" (
    python -m venv .venv
    echo Python virtual environment created in %HOMEPATH%\xbrain\.venv.
) else (
    echo Virtual environment already exists. Skipping creation.
)

REM 4. 激活虚拟环境
call .venv\Scripts\activate
echo Virtual environment activated.

REM 5. 更新pip
pip install --upgrade pip
echo pip upgraded.

REM 6. 安装pyxbrain
pip install -U pyxbrain --default-timeout=999
echo pyxbrain installed.

REM 7. 将 pyxbrain 添加到环境变量
setx PATH "%PATH%;%HOMEPATH%\xbrain\.venv\Scripts"
echo pyxbrain added to environment variables.

REM 8. 运行xb
echo running xbrain
xb