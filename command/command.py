import argparse
from utils.openai_utils import chat


def main():
    parser = argparse.ArgumentParser(description="处理命令行参数")
    parser.add_argument('chat', help='用户的要求')
    args = parser.parse_args()
    print(args.chat)
    chat(args.chat)

    
if __name__ == "__main__":
    main()