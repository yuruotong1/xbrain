from xbrain.utils.openai_utils import stream_chat
import unittest

class TestCustomerServiceWorkflow(unittest.TestCase):
    def test_customer_service_workflow(self):
        res = stream_chat([{"role": "user", "content": "你好"}])
        for chunk in res:
            if chunk.choices[0].delta.content is not None:
                return chunk.choices[0].delta.content
        print("hello")
