import os
import yaml


class Config:
    def __init__(self):
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))
        self.config = self.load_config()
        self.OPENAI_BASE_URL = self.config["openai"]["base_url"]
        self.OPENAI_API_KEY = self.config["openai"]["api_key"]
        self.OPENAI_MODEL = self.config["openai"]["model"]


    def load_config(self):
        with open(os.path.join(self.current_file_path, "..", "config.yaml"), "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)