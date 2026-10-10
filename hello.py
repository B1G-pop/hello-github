"""我的第一个 Git 仓库 —— 一个简单的小工具。

运行方式：
    python hello.py
    python hello.py 你的名字
"""

import sys
from datetime import datetime


def greet(name: str = "世界") -> str:
    """返回一句问候语。"""
    return f"你好，{name}！"


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "世界"
    print(greet(name))
    print(f"现在是 {datetime.now():%Y-%m-%d %H:%M:%S}")


if __name__ == "__main__":
    main()
