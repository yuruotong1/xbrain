@REM py -m pip install --upgrade build
rd /s /q dist
py -m build
py -m twine upload dist/*