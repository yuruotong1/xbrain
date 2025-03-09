@REM py -m pip install --upgrade build

rd /s /q dist
rd /s /q build
python -m build
python -m twine upload dist/*
