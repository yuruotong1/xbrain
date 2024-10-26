class AgentBase:
    def __init__(self):
        self.prompt = ""

    def set_prompt(self, prompt):
        self.prompt = prompt
        
    def run(self, *args, **kwargs):
        pass
