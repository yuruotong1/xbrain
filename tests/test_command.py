import os
import unittest
from xbrain.command import help_action
from xbrain.command import convert_action
from xbrain import main
from xbrain.utils.config import Config
class TestCommand(unittest.TestCase):
    def test_show_command(self):
        res = help_action.show_all_command()
        print(res)

    def test_run_command(self):
        res = main.run([{"role": "user", "content": "展示所有命令"}])
        print(res)

    def test_change_to_action(self):
        path = os.getcwd()
        res = convert_action.change_to_action(os.path.join(path, ".."))
        print(res)