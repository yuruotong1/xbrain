from xbrain.workflow import customer_service_workflow
import unittest

class TestCustomerServiceWorkflow(unittest.TestCase):
    def test_customer_service_workflow(self):
        customer_service_workflow(r"C:\Users\yuruo\Desktop\测试文本.txt")
