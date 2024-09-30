import os
import unittest
from command import command_action
from command import change_to_action
from xbrain import main
class TestCommand(unittest.TestCase):
    def test_show_command(self):
        res = command_action.show_all_command()
        print(res)

    def test_run_command(self):
        res = main.run([{"role": "user", "content": "展示所有命令"}])
        print(res)

    def test_change_to_action(self):
        path = os.getcwd()
        res = change_to_action.change_to_action(os.path.join(path, ".."))
        print(res)
