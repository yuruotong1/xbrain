import os
class Config:
    def __init__(self):
        self.default_config = {
                'openai': {
                    'base_url': 'https://api.openai.com/v1',
                    'api_key': '',
                    'model': 'gpt-4o-2024-08-06'
                }
            }
        self.user_home_path = os.path.expanduser("~")  # 获取用户主目录路径
        self.config_path = os.path.join(self.user_home_path, "xbrain", "config.yaml")  # 使用用户目录下的配置文件
        self.config = self.load_config()
        self.OPENAI_BASE_URL = self.config["openai"]["base_url"]
        self.OPENAI_API_KEY = self.config["openai"]["api_key"]
        self.OPENAI_MODEL = self.config["openai"]["model"]

    def set_openai_config(self, base_url, api_key, model):
        import yaml
        self.default_config["openai"]["base_url"] = base_url
        self.default_config["openai"]["api_key"] = api_key
        self.default_config["openai"]["model"] = model
        with open(self.config_path, 'w') as f:
            yaml.dump(self.default_config, f, default_flow_style=False)

    def load_config(self):
        import yaml
        # 确保目录存在
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        if not os.path.exists(self.config_path):
            # 如果文件不存在，创建文件并写入默认配置
            with open(self.config_path, 'w') as f:
                yaml.dump(self.default_config, f, default_flow_style=False)
            return self.default_config
        else:
            # 如果文件存在，正常加载配置
            with open(self.config_path, "r") as f:
                return yaml.load(f, Loader=yaml.FullLoader)
            
class Constants:
    def __init__(self):
        self.CONFIG_NAME = "config.yaml"
        self.XBRAIN_DIR = ".xbrain"
        self.VERSION = "1.1.24"


