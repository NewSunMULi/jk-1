"""tk功能区，一些快捷功能打包好就放这里
顺便说一句，从今以后函数,变量,类我尽量不用马语来命名"""
from tkinter import *
from typing import List, AnyStr


class 窗口异常(Exception):
    def __init__(self, why):
        """
        返回窗口异常
        """
        super.__init__()
        self.why = why

    def __str__(self):
        return self.why


def 文件快速生成(name: list):
    for n in name:
        with open(f"./资料/{n}.jk", "w", encoding="utf-8") as f:
            pass


def 辐射组协议(ID=None, PASSWORDS="123456789"):
    def 编辑(*event):
        if (ID == "辐射组管理员" or ID == "辐射组组长") and PASSWORDS == "z555r5555":
            f1 = P.get("1.0", END)
            with open("辐射组协议.txt", "w", encoding="utf-8") as f:
                f.write(f1)
            B.title("辐射组协议--管理者--" + "保存成功")

    def AA(*event):
        if (ID == "辐射组管理员" or ID == "辐射组组长") and PASSWORDS == "z555r5555":
            P.config(state=NORMAL)
            P.pack(expand=YES, fill=BOTH)
            B.title("辐射组协议--管理者--" + "可输入")

    def close(*event):
        if (ID == "辐射组管理员" or ID == "辐射组组长") and PASSWORDS == "z555r5555":
            P.config(state=DISABLED)
            P.pack(expand=YES, fill=BOTH)
            B.title("辐射组协议--管理者--" + "无法输入")

    with open("辐射组协议.txt", "r", encoding="utf-8") as f:
        text1 = f.read()
    B = Tk()
    if ID == "辐射组管理员" or ID == "辐射组组长":
        B.title("辐射组协议--管理者--无法输入")
    else:
        B.title("辐射组协议--普通用户--无法更改协议内容")
    B.geometry("600x600")
    P = Text(B)
    P.insert("1.0", text1)
    P = Text(B)
    P.insert("1.0", text1)
    P.config(state=DISABLED)
    P.pack(expand=YES, fill=BOTH)
    B.bind("<F1>", 编辑)
    B.bind("<F2>", AA)
    B.bind("<F3>", close)
    B.mainloop()


def 复数(实部: int = 0, 虚部: int = 0):
    # 返回一个复数
    return 实部 + 虚部 * 1j


def 字符变量(窗口变量=None, 字符: str = None, tips特殊列表: List[str] = []):
    listM = []
    if 窗口变量 is None:
        raise 窗口异常(why="你没给窗口我怎么干")
    elif (tips特殊列表 is None) and (字符 is None):
        raise TypeError("没有输入字符串或字符串列表")
    if tips特殊列表 is None:
        tips = StringVar(窗口变量, 字符)
        return tips
    elif 字符 is None:
        for i in tips特殊列表:
            i = StringVar(窗口变量, i)
            listM.append(i)
        return listM


if __name__ == "__main__":
    print("你已经进入辐射组协议代码区")
    辐射组协议(ID="辐射组组长", PASSWORDS="z555r5555")
