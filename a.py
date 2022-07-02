from tkinter import *


def 辐射组协议(ID=None, PASSWORDS="123456789"):
    def 编辑(*event):
        if ID == "2802912710" and PASSWORDS == "z555r5555":
            f1 = P.get("1.0", END)
            with open("辐射组协议.txt", "w", encoding="utf-8") as f:
                f.write(f1)
            print("编辑成功")

    def AA(*event):
        if ID == "2802912710" and PASSWORDS == "z555r5555":
            P.config(state=NORMAL)
            P.pack(expand=YES, fill=BOTH)
            print("输入锁已关闭，可以输入内容")

    def close(*event):
        if ID == "2802912710" and PASSWORDS == "z555r5555":
            P.config(state=NORMAL)
            P.pack(expand=YES, fill=BOTH)
            print("输入锁已打开，无法输入内容")

    with open("辐射组协议.txt", "r", encoding="utf-8") as f:
        text1 = f.read()
    B = Tk()
    B.title("辐射组协议")
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


if __name__ == "__main__":
    print("你已经进入辐射组协议代码区")
    辐射组协议()
