#!/usr/bin/env bash
. ./.venv/bin/activate
pip install -r requirements.txt
echo y | pyinstaller main.spec