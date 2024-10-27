@REM @REM py -m pip install --upgrade build
@REM rd /s /q dist
@REM py -m build
@REM py -m twine upload dist/*


call .\.venv\Scripts\activate
pip install -r requirements.txt
call echo y | pyinstaller main.spec
@REM xcopy .\.venv\Lib\site-packages\litellm\*.json .\dist\autoMateServer\_internal\litellm\  /E /H /F /I /Y

