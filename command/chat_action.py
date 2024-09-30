from xbrain.main import run


def chat(input_str: str):
    print("进入对话模式，退出请输入exit")
    while True:
        input_str = input("chat ：")
        if input_str == "exit":
            break
        res = run([{"role": "user", "content": input_str}])
        print(res)
