class WorkFlowBase:
    def main(self, params):
        pass

    # 对main函数的输入和输出进行规范化
    def run(self, params: dict = {}):
        res = self.main()
        return res