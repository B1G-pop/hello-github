"""我的第一个 Git 仓库 —— 一个简单的小工具。

运行方式：
    python hello.py
    python hello.py 你的名字
    python hello.py 小明 小红 小刚
"""

import sys
from datetime import datetime


def greet(name: str = "世界") -> str:
    """返回一句问候语。"""
    return f"哈喽，{name}！我是 B1G-pop，这是我的第一个 Git 项目 🎉"


def main() -> None:
    # 支持一次传多个名字：python hello.py 小明 小红
    names = sys.argv[1:] or ["世界"]
    for name in names:
        print(greet(name))
    print(f"现在是 {datetime.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    main()
