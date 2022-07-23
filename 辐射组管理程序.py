"""辐射组管理系统的具体代码"""
import json as 嫁我
from 功能设置 import *
from 基本常量 import *
import time
from tkinter import messagebox
from 概率模拟_原神 import 概率模拟_原神

sc = Tk()
sc.geometry(f"{x}x{y}+300+125")
list1 = []
list2 = []
list3 = []
active = False
UID = 0000000000
userName = ""
image1 = PhotoImage(file="10WST.gif")
image2 = PhotoImage(file="50WST.gif")
image3 = PhotoImage(file="250WST.gif")
image4 = PhotoImage(file="1250WST.gif")
image5 = PhotoImage(file="1.28RTY.gif")
image6 = PhotoImage(file="2.56RTY.gif")
image7 = PhotoImage(file="3.28RTY.gif")
image8 = PhotoImage(file="6.48RTY.gif")
原神宣传图 = PhotoImage(file="原神.gif")
明日宣传图 = PhotoImage()


def 原神_模拟():
    概率模拟_原神()


def 辐射组logo(scname="好兄弟", up_text="放出光芒！"):
    """Logo放这好搞
    同时纪念曾经的年华，虽然它已经过去了
    We will finding your......
    """
    Label(scname, text=up_text, font=("华光钢铁直黑 可变体 Bold", 35, "italic"), fg="blue", width=20, anchor="nw").place(x=25,
                                                                                                                y=20)  # italic斜体
    Label(scname, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=70)


def 协议():
    if UID != 0:
        辐射组协议(ID=ID[user_list.index(UID)], PASSWORDS=user_password[user_list.index(UID)])
    else:
        辐射组协议()


def 账户财产(用户账号=UID):
    if 用户账号 in user_list:
        if len(list1) != 0:
            for i in list1:
                i.destroy()
        序数 = user_list.index(用户账号)
        wst = WST[序数]

        def 测试():
            user_WST.set("你的WST:" + str(wst - 9999))

        user_WST = StringVar(sc)
        WST1 = Button(sc, textvariable=user_WST, bd=0, command=氪金系统)
        user_WST.set("你的WST:" + str(wst))
        WST1.place(x=590, y=570)
        user_RTY = StringVar(sc)
        rty = RTY[序数]
        RTY2 = Button(sc, textvariable=user_RTY, bd=0, command=氪金系统, width=250, anchor="w")
        user_RTY.set("你的RTY:" + str(rty))
        RTY2.place(x=690, y=570)
        list1.append(WST1)
        list1.append(RTY2)
    else:
        if len(list1) != 0:
            for i in list1:
                i.destroy()
        序数 = None
        user_WST = StringVar(sc)
        WST1 = Button(sc, textvariable=user_WST, bd=0, command=氪金系统)
        user_WST.set("未登录无法查看")
        WST1.place(x=590, y=570)
        user_RTY = StringVar(sc)
        RTY2 = Button(sc, textvariable=user_RTY, bd=0, command=氪金系统)
        user_RTY.set("未登录无法查看")
        RTY2.place(x=690, y=570)
        list1.append(WST1)
        list1.append(RTY2)


def 氪金系统():
    def A():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 10
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def B():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 50
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def C():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 250
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def D():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 1250
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def E():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 2
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def F():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 3
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def G():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 4
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def H():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 6
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    充值界面 = Toplevel()
    充值界面.geometry(f"{x}x{y}+300+125")
    充值界面.title("充值")
    辐射组logo(充值界面, "充值入口")
    Label(充值界面, text="WTS:功能使用基础货币", font=("", 15)).place(x=30, y=120)
    aa = Button(充值界面, image=image1, bd=0, command=A)
    aa.place(x=10, y=150)
    Label(充值界面, text="10 WST ￥1", font=(华体, 17)).place(x=32, y=280)
    b = Button(充值界面, image=image2, bd=0, command=B)
    b.place(x=210, y=150)
    Label(充值界面, text="50 WST ￥5", font=(华体, 17)).place(x=229, y=280)
    c = Button(充值界面, image=image3, bd=0, command=C)
    c.place(x=410, y=150)
    Label(充值界面, text="250 WST ￥25", font=(华体, 17)).place(x=420, y=280)
    d = Button(充值界面, image=image4, bd=0, command=D)
    d.place(x=610, y=150)
    Label(充值界面, text="1250 WST ￥125", font=(华体, 17)).place(x=605, y=280)

    Label(充值界面, text="RTY:功能使用高级货币", font=("", 15)).place(x=30, y=340)
    e = Button(充值界面, image=image5, bd=0, command=E)
    e.place(x=10, y=370)
    Label(充值界面, text="1.28 RTY  ￥128", font=(华体, 17)).place(x=10, y=500)
    ff = Button(充值界面, image=image6, bd=0, command=F)
    ff.place(x=210, y=370)
    Label(充值界面, text="2.56 RTY ￥256", font=(华体, 17)).place(x=210, y=500)
    g = Button(充值界面, image=image7, bd=0, command=G)
    g.place(x=410, y=370)
    Label(充值界面, text="3.28 RTY ￥328", font=(华体, 17)).place(x=420, y=500)
    h = Button(充值界面, image=image8, bd=0, command=H)
    h.place(x=610, y=370)
    Label(充值界面, text="6.48 RTY ￥648", font=(华体, 17)).place(x=605, y=500)


def 登录和注册(scname=sc):
    global list3
    global active
    sc4 = Tk()

    def 登录():
        global list3
        global userName

        def 检测1(*EN):
            global active
            global userName
            global log
            global UID
            num = userNumber.get()
            pas = userPassword.get()
            if num in user_list:
                if pas not in user_password or user_list.index(num) != user_password.index(pas):
                    a8 = Label(sc4, text="密码错误", width=150, anchor="sw")
                    a8.place(x=375, y=420)
                elif user_list.index(num) == user_password.index(pas):
                    a8 = Label(sc4, text="登陆成功", width=150, anchor="sw")
                    active = True
                    userName = user_name[user_list.index(num)]
                    UID = num
                    log = Button(sc, text=userName, font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=退出登录, width=20,
                                 anchor="w")
                    Label(sc, text="已登录", font=("微软雅黑", 8, 斜体,), fg="green").place(x=660, y=79)
                    Label(sc, text=ID[user_list.index(num)], font=("微软雅黑", 8, 斜体,), fg="green", width=100,
                          anchor="w").place(x=715, y=79)
                    账户财产(UID)
                    log.place(x=659, y=50)
                    a8.place(x=375, y=420)
                    sc4.destroy()
            else:
                a8 = Label(sc4, text="无此账户", width=150, anchor="sw")
                a8.place(x=375, y=420)

        a1 = Label(sc4, text="VRt-21", fg="#F508F0", font=("微软雅黑", 48, 斜体))
        a1.place(x=800 / 2 - 48 * 5 / 2, y=30)
        a2 = Label(sc4, text="登录&注册", fg="#00FFF2", font=("微软雅黑", 24, 斜体))
        a2.place(x=800 / 2 - 48 * 3.75 / 2, y=100)
        a3 = Label(sc4, text="登录", fg="red", font=("微软雅黑", 20))
        a3.place(x=800 / 2 - 48 * 1.5 / 2, y=200)
        a4 = Label(sc4, text="账号(名)", font=("", 10))
        a4.place(x=280, y=250)
        a5 = Label(sc4, text="账户密码", font=("", 10))
        a5.place(x=280, y=290)
        userNumber = Entry(sc4)
        userNumber.place(x=340, y=250)
        userPassword = Entry(sc4, show="*")
        userPassword.place(x=340, y=290)
        userNumber.insert(END, "2802912710")
        userPassword.insert(END, "z555r5555")
        a6 = Button(sc4, text="登录", width=5, command=检测1)
        a6.place(x=380, y=320)
        a7 = Button(sc4, text="没有账号?注册一个", bd=0, command=注册)
        a7.place(x=350, y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.bind("<3>", 检测1)
        sc4.mainloop()

    def 注册():
        global list3

        def 检测2():
            global active
            num = userNumber.get()
            pas = userPassword.get()
            if num not in user_list and len(pas) != 0:
                a8 = Label(sc4, text="注册成功", width=150, anchor="sw")
                user_list.append(num)
                user_password.append(pas)
                user_name.append(num)
                ID.append("普通用户")
                WST.append(0)
                RTY.append(0.0)
                with open("./资料/" + num + ".jk", "w", encoding="utf-8") as f:
                    f.write(f"{num}\n")
                    f.write("N-N-N\n")
                    f.write("欢迎您的到来")
                个人资料.append("./资料/" + num + ".jk")
                a8.place(x=375, y=420)
                临时列表 = [user_list, user_password, user_name, ID, 个人资料, WST, RTY]
                for i in 检索:
                    with open(i + ".json", "w", encoding="utf-8") as f:
                        嫁我.dump(临时列表[检索.index(i)], f)
            elif len(num) != 10:
                a8 = Label(sc4, text="十位数账号", width=150, anchor="sw")
                a8.place(x=370, y=420)
            elif len(pas) == 0:
                a8 = Label(sc4, text="密码呢?", width=150, anchor="sw")
                a8.place(x=375, y=420)
            else:
                a8 = Label(sc4, text="已被注册", width=150, anchor="sw")
                a8.place(x=375, y=420)

        for i in list3:
            i.destroy()
            list3.remove(i)
        a1 = Label(sc4, text="VRt-21", fg="#F508F0", font=("微软雅黑", 48, 斜体))
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
        userPassword = Entry(sc4)
        userPassword.place(x=340, y=290)
        a6 = Button(sc4, text="注册", width=5, command=检测2)
        a6.place(x=380, y=320)
        a7 = Button(sc4, text="注册好了登录", bd=0, command=登录)
        a7.place(x=365, y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.mainloop()

    sc4.title("登录&注册")
    sc4.geometry(f"{x}x{y}+300+150")
    登录()


def 退出登录():
    global UID
    global log

    def 退出():
        global UID
        global log
        UID = 0000000000
        sc5.destroy()
        账户财产(UID)
        log = Button(sc, text="登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=登录和注册, width=300, anchor="w")
        log.place(x=659, y=50)
        Label(sc, text="             ", font=("微软雅黑", 8, 斜体,), fg="green").place(x=660, y=79)
        Label(sc, text="             ", font=("微软雅黑", 8, 斜体,), fg="green", width=100, anchor="w").place(x=720, y=79)

    sc5 = Tk()
    sc5.title("个人资料")
    sc5.geometry(大小)
    Label(sc5, text="个人主页", fg="green", font=(华体, 30, 加粗)).place(x=0, y=30)
    Label(sc5, text="头像：正在制作", font=(华体, 18)).place(x=40, y=100)
    with open(f"{个人资料[user_list.index(UID)]}", "r", encoding="utf-8") as f:
        资料信息 = f.readlines()
    for i in 资料信息:
        Label(sc5, text=f"{信息[资料信息.index(i)]}:{i}", font=(华体, 18)).place(x=40, y=150 + 资料信息.index(i) * 50)
    exit = Button(sc5, text="退出登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=退出)
    exit.pack(side=BOTTOM, anchor="s")


if active:
    log = Button(sc, text=userName, font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=退出登录)
    Label(sc, text="已登录", font=("微软雅黑", 8, 斜体,), fg="green").place(x=660, y=79)
    Label(sc, text=ID, font=("微软雅黑", 8, 斜体,), fg="green").place(x=720, y=79)
else:
    # “bold”加粗、“italic”斜体、“underline”下划线、“overstrike”删除线。
    log = Button(sc, text="登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=登录和注册)
log.place(x=659, y=50)
账户财产(UID)


class 辐射组管理程序:
    """除了概率模拟其余功能只能让辐射组成员使用"""

    def __init__(self):
        """自动运行的部分"""
        self.控件 = []

    def 首页(self):
        sc.title("辐射组管理程序--首页")
        Label(sc, text="首页", font=("华光钢铁直黑 可变体 Bold", 35, "italic"), fg="blue", width=20, anchor="sw").place(x=25,
                                                                                                             y=20)
        Label(sc, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=70)
        img1 = PhotoImage(file="概率模拟.gif")
        self.概率 = Button(sc, text="概率模拟", font=("微软雅黑", 15, 斜体), image=img1, compound=CENTER, bd=0,
                         command=self.概率模拟)  # compound图片显示与文字之哪
        self.概率.place(x=70, y=140)
        self.协议 = Button(sc, text="辐射组/合作社协议", font=("微软雅黑", 12), bd=0, command=协议)
        self.协议.pack(side=BOTTOM, anchor="center")
        self.控件.append(self.概率)
        self.控件.append(self.协议)
        sc.update()
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
                x1.append(int(input("self")))
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
        辐射组logo(sc, "概率模拟")
        self.原神 = Button(sc, text="原神概率模拟", font=(华体, 20), fg="#FF0000", image=原神宣传图, bd=0, command=原神_模拟, anchor="se",
                         compound=CENTER)
        # compound图片显示与文字之哪
        self.原神.place(x=50, y=140)
        self.控件.append(self.原神)
        sc.update()


if __name__ == "__main__":
    a = 辐射组管理程序()
    a.首页()
