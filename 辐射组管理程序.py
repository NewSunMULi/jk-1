"""辐射组管理系统的具体代码"""
import threading as td
from tkinter import *
import random as rs
import matplotlib.pyplot as plt
from pygame import event, display, mixer
from a import 辐射组协议

sc = Tk()
x, y = 800, 600
sc.geometry(f"{x}x{y}+300+250")
user_list = ["2802912710"]
user_password = ["z555r5555"]
斜体 = "italic"


def 辐射组logo(scname="好兄弟", up_text="放出光芒！"):
    """Logo放这好搞
    同时纪念曾经的年华，虽然它已经过去了
    We will finding your......
    """
    Label(scname, text=up_text, font=("微软雅黑", 35, "italic"), fg="blue").place(x=25, y=20)  # italic斜体
    Label(scname, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=80)


class 辐射组管理程序:
    """除了概率模拟其余功能只能让辐射组成员使用"""

    def __init__(self):
        """自动运行的部分"""
        pass

    def 首页(self):
        sc.title("辐射组管理程序--首页")
        Label(sc, text="首页", font=("微软雅黑", 35, "italic"), fg="blue").place(x=25, y=20)
        Label(sc, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=80)
        img1 = PhotoImage(file="概率模拟.gif")
        概率模拟 = Button(sc, text="概率模拟", font=("微软雅黑", 15, 斜体), image=img1, compound=CENTER, bd=0)  # compound图片显示与文字之哪
        概率模拟.place(x=70, y=140)
        协议 = Button(sc, text="辐射组/合作社协议", font=("微软雅黑", 12), bd=0, command=辐射组协议)
        协议.pack(side=BOTTOM)
        sc.mainloop()

    def 开发者模式(self):
        list1 = []
        x1 = []
        y1 = []
        text = []
        sc3 = Tk()

        def 编辑界面(*event):
            sc3.destroy()
            sc1 = Tk()
            sc1.title("窗口编辑")
            sc1.geometry(f"{x}x{y}+300+250")
            qq = PhotoImage(file="tk模板.png")
            Label(sc1, image=qq).place(x=0, y=0)

            def 显示(event1):
                m = Label(sc1, text=str(event1.x) + "," + str(event1.y), width=300, anchor="w")
                m.place(x=700, y=560)
                sc1.after(5000, m.destroy)

            def 组件管理():
                gl = Tk()
                gl.title("组件管理")
                gl.geometry("400x400")
                for i in list1:
                    num = list1.index(i)
                    Label(gl, text="组件信息:" + i["text"] + "(" + str(x1[num]) + "," + str(y1[num]) + ")").pack(anchor="w")
                    i.place(x=x1[num], y=y1[num])
                gl.mainloop()

            def 标签():
                x1.append(int(input("x")))
                y1.append(int(input("y")))
                text1 = input("text")
                text.append(text1)
                list1.append(Label(sc1, text=text1))

            def 按钮():
                pass

            def 单行输入框():
                pass

            菜单 = Menu(sc1)  # 菜单组件
            文件 = Menu(sc1)
            组件 = Menu(菜单, tearoff=0)
            组件.add_command(label="标签", command=标签)  # 普通菜单
            组件.add_command(label="组件管理", command=组件管理)
            菜单.add_cascade(label="文件")
            菜单.add_cascade(label="组件", menu=组件)  # 瀑布式菜单
            sc1['menu'] = 菜单  # 菜单显示在窗口上
            m = Label(sc1)
            sc1.bind("<Motion>", 显示)
            sc1.mainloop()

        def 检测():
            user = self.sr.get()
            p = False
            password = self.password.get()
            if user in user_list and password in user_password:
                if user_list.index(user) == user_password.index(password):
                    Label(sc3, text="登陆成功", width=200, anchor="w").place(x=100, y=140)
                    p = True
                else:
                    Label(sc3, text="用户名或密码错误", width=200, anchor="w").place(x=100, y=140)
                    p = False
            else:
                Label(sc3, text="无此用户", width=200, anchor="w").place(x=100, y=140)
            if p:
                编辑界面()

        sc3.title("管理程序--开发者模式")
        sc3.geometry("300x200+300+250")
        Label(sc3, text="登录", font=("宋体", 30)).place(x=0, y=0)
        self.m = Label(sc3, text="用户名", font=("宋体", 20))
        self.m.place(x=0, y=50)
        self.sr = Entry(sc3)
        self.sr.place(x=100, y=55)
        self.mm = Label(sc3, text="密码", font=("宋体", 20))
        self.mm.place(x=0, y=100)
        self.password = Entry(sc3, show="♂")
        self.password.place(x=100, y=105)
        self.log = Button(sc3, text="登录", bd=1, font=("", 15), command=检测)
        self.log.place(x=0, y=140)
        sc3.bind("<ButtonPress-3>", 编辑界面)
        sc3.mainloop()

    def 概率模拟(self):
        辐射组logo(scname=sc,up_text="概率模拟")


a = 辐射组管理程序()
a.首页()
