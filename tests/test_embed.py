import unittest

from xbrain.plugin.rag.embed_csv_action import embedding_csv_action
from xbrain.plugin.rag.retrieve_csv_action import retrieve_action

class TestEmbed(unittest.TestCase):
    def test_embedding_action(self):
        embedding_csv_action(r"C:\Users\yuruo\OneDrive\Desktop\test\测试文本.txt")

    def test_retrieve_action(self):
        retrieve_action("acf5型号")
