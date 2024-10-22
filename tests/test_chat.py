import unittest
import os
from xbrain.utils.openai_utils import chat

class TestChatFunction(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create the dummy.txt file with some information
        os.makedirs("test", exist_ok=True)
        with open("test/dummy.txt", "w") as f:
            f.write("This is a dummy file for testing purposes.")

    def test_chat_without_file(self):
        response = chat(messages=[{"role": "user", "content": "Hello!"}], tools=None, user_prompt="How can I assist you today?")
        
        self.assertIsNotNone(response)
        print("Response without file:", response)

    def test_chat_with_file(self):
        response = chat(messages=[{"role": "user", "content": "Upload this file"}], tools=None, user_prompt="This is a file test.", file="test/dummy.txt")
        
        self.assertIsNotNone(response)
        print("Response with file:", response)

    @classmethod
    def tearDownClass(cls):
        # Remove the dummy.txt file after testing
        os.remove("test/dummy.txt")
        os.rmdir("test")

if __name__ == '__main__':
    unittest.main()
