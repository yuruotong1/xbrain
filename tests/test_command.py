import os
import unittest
from xbrain.plugin import help_action
from xbrain.plugin import integrate_action
from xbrain.core import chat
from xbrain.utils.config import Config
class TestCommand(unittest.TestCase):
    def test_show_command(self):
        res = help_action.show_all_command()
        print(res)

    def test_run_command(self):
        res = chat.run([{"role": "user", "content": "展示所有命令"}])
        print(res)

    def test_change_to_action(self):
        path = os.getcwd()
        res = integrate_action.change_to_action(os.path.join(path, ".."))
        print(res)