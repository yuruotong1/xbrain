@REM py -m pip install --upgrade build
rd /s /q dist
rd /s /q build
python -m build
python -m twine upload dist/*


@REM call .\.venv\Scripts\activate
@REM pip install -r requirements.txt
@REM call echo y | pyinstaller main.spec
@REM @REM xcopy .\.venv\Lib\site-packages\litellm\*.json .\dist\autoMateServer\_internal\litellm\  /E /H /F /I /Y

