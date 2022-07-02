"""辐射组管理系统的具体代码"""
import threading as td
import matplotlib.pyplot as plt
from tkinter import *
import json as js
from a import 辐射组协议

sc = Tk()
x, y = 800, 600
sc.geometry(f"{x}x{y}+300+200")
user_list = ["2802912710"]
user_password = ["z555r5555"]
list1 = []
list2 = []
list3 = []
斜体 = "italic"
active = False


def 辐射组logo(scname="好兄弟", up_text="放出光芒！"):
    """Logo放这好搞
    同时纪念曾经的年华，虽然它已经过去了
    We will finding your......
    """
    Label(scname, text=up_text, font=("微软雅黑", 35, "italic"), fg="blue", width=400, anchor="nw").place(x=25,
                                                                                                      y=20)  # italic斜体
    Label(scname, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=80)


def 登录和注册(scname=sc):
    global list3
    global active
    def 登录():
        global list3
        def 检测1():
            global active
            num = userNumber.get()
            pas = userPassword.get()
            if num in user_list:
                if pas not in user_password or user_list.index(num) != user_password.index(pas):
                    a8 = Label(sc4, text="密码错误", width=150,anchor="sw")
                    a8.place(x=375, y=420)
                elif user_list.index(num) == user_password.index(pas):
                    a8 = Label(sc4,text="登陆成功",width=150,anchor="sw")
                    active = True
                    a8.place(x=375,y=420)
            else:
                a8 = Label(sc4, text="无此账户", width=150, anchor="sw")
                a8.place(x=375, y=420)
        if len(list3) != 0:
            for i in list3:
                i.destroy()
                list3.remove(i)
        a1 = Label(sc4,text="VRt-21",fg="blue",font=("微软雅黑",48,斜体))
        a1.place(x=800/2-48*5/2,y=30)
        a2 = Label(sc4,text="登录&注册",fg="#00FFF2",font=("微软雅黑",24,斜体))
        a2.place(x=800/2-48*3.75/2,y=100)
        a3 = Label(sc4,text="登录",fg="red",font=("微软雅黑",20))
        a3.place(x=800/2-48*1.5/2,y=200)
        a4 = Label(sc4,text="账号(名)",font=("",10))
        a4.place(x=280,y=250)
        a5 = Label(sc4,text="账户密码",font=("",10))
        a5.place(x=280,y=290)
        userNumber = Entry(sc4)
        userNumber.place(x=340,y=250)
        userPassword = Entry(sc4,show="J")
        userPassword.place(x=340,y=290)
        userNumber.insert(END,"2802912710")
        userPassword.insert(END,"z555r5555")
        a6 = Button(sc4,text="登录",width=5,command=检测1)
        a6.place(x=380,y=320)
        a7 = Button(sc4,text="没有账号?注册一个",bd=0,command=注册)
        a7.place(x=350,y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.mainloop()
    def 注册():
        global list3
        def 检测2():
            global active
            num = userNumber.get()
            pas = userPassword.get()
            if num not in user_list:
                a8 = Label(sc4, text="注册成功", width=150,anchor="sw")
                user_list.append(num)
                user_password.append(pas)
                a8.place(x=375, y=420)
            else:
                a8 = Label(sc4,text="已被注册",width=150,anchor="sw")
                a8.place(x=375,y=420)
        for i in list3:
            i.destroy()
            list3.remove(i)
        a1 = Label(sc4, text="VRt-21", fg="blue", font=("微软雅黑", 48, 斜体))
        a1.place(x=800 / 2 - 48 * 5 / 2, y=30)
        a2 = Label(sc4, text="登录&注册", fg="#00FFF2", font=("微软雅黑", 24, 斜体))
        a2.place(x=800 / 2 - 48 * 3.75 / 2, y=100)
        a3 = Label(sc4, text="注册", fg="red", font=("微软雅黑", 20))
        a3.place(x=800 / 2 - 48 * 1.5 / 2, y=200)
        a4 = Label(sc4, text="账号(名)", font=("", 10))
        a4.place(x=280, y=250)
        a5 = Label(sc4, text="账户密码", font=("", 10))
        a5.place(x=280, y=290)
        userNumber = Entry(sc4)
        userNumber.place(x=340, y=250)
        userPassword = Entry(sc4,show="J")
        userPassword.place(x=340, y=290)
        a6 = Button(sc4, text="注册", width=5,command=检测2)
        a6.place(x=380, y=320)
        a7 = Button(sc4, text="注册好了登录", bd=0, command=登录)
        a7.place(x=365, y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.mainloop()
    sc4 = Tk()
    sc4.geometry(f"{x}x{y}+300+200")
    登录()


class 辐射组管理程序:
    """除了概率模拟其余功能只能让辐射组成员使用"""

    def __init__(self):
        """自动运行的部分"""
        self.控件 = []

    def 首页(self):
        sc.title("辐射组管理程序--首页")
        Label(sc, text="首页", font=("微软雅黑", 35, "italic"), fg="blue").place(x=25, y=20)
        Label(sc, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=80)
        img1 = PhotoImage(file="概率模拟.gif")
        self.概率 = Button(sc, text="概率模拟", font=("微软雅黑", 15, 斜体), image=img1, compound=CENTER, bd=0,
                         command=self.概率模拟)  # compound图片显示与文字之哪
        self.概率.place(x=70, y=140)
        self.协议 = Button(sc, text="辐射组/合作社协议", font=("微软雅黑", 12), bd=0, command=辐射组协议)
        self.协议.pack(side=BOTTOM)
        self.控件.append(self.概率)
        self.控件.append(self.协议)
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
        for i in self.控件:
            i.destroy()
            self.控件.remove(i)
        辐射组logo(scname=sc, up_text="概率模拟")


登录和注册(scname=sc)
