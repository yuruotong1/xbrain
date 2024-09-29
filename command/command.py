from xbrain.main import run

def main():
    while True:
        input_str = input("请输入你的需求：")
        run([{"role": "user", "content": input_str}])
    
if __name__ == "__main__":
    main()