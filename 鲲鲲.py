import tkinter as tk
import tkinter.filedialog as tf
import tkinter.messagebox as ms
import requests as rt
import re
from moviepy.editor import *
import threading as th
import os
import time
import pygame.mixer as mm
import tqdm as td
from 基本常量 import *

mm.init()
url1 = []
url2 = []
MP42 = None
head = {
    'referer': 'https://www.bilibili.com/video',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
}


class 音效:
    def __init__(self):
        pass

    @staticmethod
    def 下载完成():
        mm.music.load("音效.mp3")
        mm.music.play()
        time.sleep(25)
        mm.music.stop()

    @staticmethod
    def 遇到错误():
        mm.music.load("你干嘛.mp3")
        mm.music.play()
        time.sleep(4)
        mm.music.stop()


def 运行时长():
    seconds = 0
    minters = 0
    hours = 0
    aa = can.create_text(480, 30, text=f"运行时间:{hours}h {minters}m {seconds}s", font=(原神字体, 15, 加粗), fill="green")
    while True:
        time.sleep(1)
        seconds += 1
        if seconds == 60:
            minters += 1
            seconds -= 60
        if minters == 60:
            hours += 1
            minters -= 60
        can.itemconfig(aa, text=f"运行时间:{hours}h {minters}m {seconds}s")


def 辐射组账号模块():
    sc4 = tk.Toplevel(sc)
    global active, userName, UID, name

    def 登录():
        global active
        global userName
        global log
        global UID
        global list3, name

        def 检测1(*EN):
            global active
            global userName
            global log
            global UID
            global list3, name
            num = userNumber.get()
            pas = userPassword.get()
            if num in user_list:
                if pas not in user_password or user_list.index(num) != user_password.index(pas):
                    a8 = tk.Label(sc4, text="密码错误", width=150, anchor="sw")
                    a8.place(x=375, y=420)
                    active = False
                elif user_list.index(num) == user_password.index(pas):
                    a8 = tk.Label(sc4, text="登陆成功", width=150, anchor="sw")
                    active = True
                    name = user_name[user_list.index(num)]
                    can.itemconfig(d12, text=name)
                    UID = num
                    a8.place(x=375, y=420)
                    sc4.destroy()
            else:
                a8 = tk.Label(sc4, text="无此账户", width=150, anchor="sw")
                active = False
                a8.place(x=375, y=420)

        active = False
        a1 = tk.Label(sc4, text="VRt-21", fg="#F508F0", font=("微软雅黑", 48, 斜体))
        a1.place(x=800 / 2 - 48 * 5 / 2, y=30)
        a2 = tk.Label(sc4, text="登录&注册", fg="#00FFF2", font=("微软雅黑", 24, 斜体))
        a2.place(x=800 / 2 - 48 * 3.75 / 2, y=100)
        a3 = tk.Label(sc4, text="登录", fg="red", font=("微软雅黑", 20))
        a3.place(x=800 / 2 - 48 * 1.5 / 2, y=200)
        a4 = tk.Label(sc4, text="账号(名)", font=("", 10))
        a4.place(x=280, y=250)
        a5 = tk.Label(sc4, text="账户密码", font=("", 10))
        a5.place(x=280, y=290)
        userNumber = tk.Entry(sc4)
        userNumber.place(x=340, y=250)
        userPassword = tk.Entry(sc4, show="*")
        userPassword.place(x=340, y=290)
        userNumber.insert(tk.END, "2802912710")
        userPassword.insert(tk.END, "z555r5555")
        a6 = tk.Button(sc4, text="登录", width=5, command=检测1)
        a6.place(x=380, y=320)
        a7 = tk.Button(sc4, text="没有账号?注册一个", bd=0, command=注册)
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
                a8 = tk.Label(sc4, text="注册成功", width=150, anchor="sw")
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
                        js.dump(临时列表[检索.index(i)], f)
            elif len(num) != 10:
                a8 = tk.Label(sc4, text="十位数账号", width=150, anchor="sw")
                a8.place(x=370, y=420)
            elif len(pas) == 0:
                a8 = tk.Label(sc4, text="密码呢?", width=150, anchor="sw")
                a8.place(x=375, y=420)
            else:
                a8 = tk.Label(sc4, text="已被注册", width=150, anchor="sw")
                a8.place(x=375, y=420)

        for i in list3:
            i.destroy()
            list3.remove(i)
        a1 = tk.Label(sc4, text="VRt-21", fg="#F508F0", font=("微软雅黑", 48, 斜体))
        a1.place(x=800 / 2 - 48 * 5 / 2, y=30)
        a2 = tk.Label(sc4, text="登录&注册", fg="#00FFF2", font=("微软雅黑", 24, 斜体))
        a2.place(x=800 / 2 - 48 * 3.75 / 2, y=100)
        a3 = tk.Label(sc4, text="注册", fg="red", font=("微软雅黑", 20))
        a3.place(x=800 / 2 - 48 * 1.5 / 2, y=200)
        a4 = tk.Label(sc4, text="账号(名)", font=("", 10))
        a4.place(x=280, y=250)
        a5 = tk.Label(sc4, text="账户密码", font=("", 10))
        a5.place(x=280, y=290)
        userNumber = tk.Entry(sc4)
        userNumber.place(x=340, y=250)
        userPassword = tk.Entry(sc4)
        userPassword.place(x=340, y=290)
        a6 = tk.Button(sc4, text="注册", width=5, command=检测2)
        a6.place(x=380, y=320)
        a7 = tk.Button(sc4, text="注册好了登录", bd=0, command=登录)
        a7.place(x=365, y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.mainloop()

    sc4.title("登录&注册")
    sc4.geometry(f"{x}x{y}+300+150")
    登录()


def 信息展示(url):
    try:
        if url[0] != "B":
            bi = rt.get(url, headers=head)
        else:
            bi = rt.get(f"https://bilibili.com/video/{url}", headers=head)
        title = re.findall('<meta data-vue-meta="true" itemprop="name" name="title" content=(.*?)>', bi.text)
        anchor = re.findall('<meta data-vue-meta="true" itemprop="author" name="author" content=(.*?)>', bi.text)
        title = title[0][-len(title[0]) + 1:-15]
        anchor = anchor[0][-len(title[0]) + 2:-1]
        res = re.findall("<script>window\.__playinfo__=(.*?)</script>", bi.text)[0]
        data = js.loads(res)
        time = data['data']['timelength']
        for i in range(3):
            try:
                url1.append(data['data']['dash']['audio'][i]['baseUrl'])
                url2.append(data['data']['dash']['video'][i * 3]['base_url'])
            except IndexError:
                pass
        return url2, title, anchor, time
    except Exception as f2:
        th.Thread(target=音效.遇到错误).start()
        ms.showwarning("警告", f"代码错误:{f2}")


def 视频爬取(url_list=None, 文件名称=None, 额外信息=None):
    global MP42
    if 文件名称 is not None or 文件名称 != "":
        if 额外信息 == "只要音频":
            s = rt.get(url_list, headers=head)
            total = int(s.headers.get("content-length", 0))
            with open(文件名称 + ".mp3", 'wb') as file, td.tqdm(
                    desc=文件名称 + ".mp3",  # 文件名
                    total=total,  # 进度
                    unit='B',  # 单位
                    unit_scale=True,  # 认不得
                    unit_divisor=1024,  # 进制
            ) as bar:
                for data in s.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            url1.clear()
            url2.clear()
            can.itemconfig(d9, text="音频已完全下载")
            th.Thread(target=音效.下载完成).start()
            ms.showinfo("来自鲲鲲的提示", "小黑子，视频已完全下载完，食不食油饼?")

        elif 额外信息 == "只要视频":
            s = rt.get(url_list, headers=head, stream=True)  # stream 开启用流来获取数据
            total = int(s.headers.get('content-length', 0))
            # 打开当前目录的fname文件(名字你来传入)
            # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
            with open(文件名称 + ".mp4", 'wb') as file, td.tqdm(
                    desc=文件名称 + ".mp4",  # 文件名
                    total=total,  # 进度
                    unit='B',  # 单位
                    unit_scale=True,  # 认不得
                    unit_divisor=1024,  # 进制
            ) as bar:
                for data in s.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            url1.clear()
            url2.clear()
            can.itemconfig(d9, text="无声视频已完全下载")
            th.Thread(target=音效.下载完成).start()
            ms.showinfo("来自鲲鲲的提示", "小黑子，视频已完全下载完，食不食油饼?")

        else:
            s = rt.get(url_list[0], headers=head)
            total = int(s.headers.get("content-length", 0))
            print(total)
            with open(文件名称[:-3] + ".mp3", 'wb') as file, td.tqdm(
                    desc=文件名称[:-3] + ".mp3",  # 文件名
                    total=total,  # 进度
                    unit='B',  # 单位
                    unit_scale=True,  # 认不得
                    unit_divisor=1024,  # 进制
            ) as bar:
                for data in s.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)

            s = rt.get(url_list[1], headers=head, stream=True)  # stream 开启用流来获取数据
            total = int(s.headers.get('content-length', 0))
            # 打开当前目录的fname文件(名字你来传入)
            # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
            with open(文件名称[:-3] + ".mp4", 'wb') as file, td.tqdm(
                    desc=文件名称[:-3] + ".mp4",  # 文件名
                    total=total,  # 进度
                    unit='B',  # 单位
                    unit_scale=True,  # 认不得
                    unit_divisor=1024,  # 进制
            ) as bar:
                for data in s.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            ad = AudioFileClip(文件名称[:-3] + ".mp3")
            vd = VideoFileClip(文件名称[:-3] + ".mp4")

            def da(mp3=ad, MP4: VideoFileClip = vd):
                global MP42
                MP42 = MP4.set_audio(mp3)
                MP42.write_videofile(f'{文件名称}.mp4')
                can.itemconfig(d9, text="视频已完全下载")
                try:
                    os.remove(文件名称[:-3] + ".mp3")
                    os.remove(文件名称[:-3] + ".mp4")
                except:
                    time.sleep(10)
                    os.remove(文件名称[:-3] + ".mp3")
                    os.remove(文件名称[:-3] + ".mp4")
                url1.clear()
                url2.clear()
                th.Thread(target=音效.下载完成).start()
                ms.showinfo("来自鲲鲲的提示", "小黑子，视频已完全下载完，食不食油饼?")

            sc.update()
            th.Thread(target=da).start()
    else:
        pass


sc = tk.Tk()
sc.title("鲲鲲V0.2测试版")
sc.geometry("960x540+230+80")
sc.attributes("-alpha", 0.95)  # 透明度设置
try:
    with open("pictor.json", "r", encoding="utf-8") as f:
        w = tk.PhotoImage(file=js.load(f))
except FileNotFoundError:
    w = tk.PhotoImage(file="蔡徐坤2.png")
w2 = tk.PhotoImage(file="logo_kk.png")
w2 = w2.subsample(2, 2)
if w.height() == 1080:
    w = w.subsample(2, 2)
else:
    pass
name = "未登陆你的辐射组账号"
视频名字 = ""
can = tk.Canvas(sc, highlightthickness=0, width=960, height=540)  # 创建画布
can.place(x=0, y=0)  # 大小
img = can.create_image(480, 270, image=w)  # 添加图片
img2 = can.create_image(480, 110, image=w2)
search = can.create_text(366, 230 - 40, text="在此输入你要下载的视频的BV号或具体网址:", fill="blue", font=("微软雅黑", 13))
d = can.create_rectangle(480 + 220, 270 - 20 - 40, 480 + 320, 270 - 40)
d2 = can.create_text((480 + 220 + 50), 260 - 40, text="搜索", fill="green", font=("微软雅黑", 12))
can.create_text(480 + 120, 110 + 35, text="V 0.2.1", fill="#ff00ff", font=("汉仪文黑-85W Heavy", 15))
a = tk.Entry(sc, bd=0, width=70)
a.place(x=200, y=250 - 40)
g = can.create_text(480, 270 + 65, text="")
d3 = can.create_rectangle(200-30, 450, 350-30, 470, outline="yellow")
d4 = can.create_text(275-30, 460, text="最高画质", fill="#FF00FF", font=("微软雅黑", 12))
d5 = can.create_rectangle(360-30, 450, 510-30, 470, outline="yellow")
d6 = can.create_text(435-30, 460, text="中等画质", fill="#FF00FF", font=("微软雅黑", 12))
d7 = can.create_rectangle(520-30, 450, 670-30, 470, outline="yellow")
d8 = can.create_text(595-30, 460, text="最低画质", fill="#FF00FF", font=("微软雅黑", 12))
d10 = can.create_rectangle(20, 20, 120, 50, outline="#FF00FF")
d14 = can.create_text(760-30, 460, text="只要音频", fill="#FF00FF", font=("微软雅黑", 12))
d15 = can.create_rectangle(680-30, 450, 830-30, 470, outline="yellow")
d16 = can.create_text(435-30, 430, text="只要无声视频", fill="#FF00FF", font=("微软雅黑", 12))
d17 = can.create_rectangle(360-30, 420, 510-30, 440, outline="yellow")
d11 = can.create_text(70, 35, text="更改图片", fill="#FF0000", font=("微软雅黑", 12))
d12 = can.create_text(960 - 90, 35, text=name, fill="red", font=("微软雅黑", 12))
d13 = can.create_text(480, 520, text="关于我们", fill="red", font=("微软雅黑", 12))
d9 = can.create_text(480, 480, text="无额外信息", fill="#FF00FF", font=("微软雅黑", 12, "bold"))
组件 = [search, d, d2, d3, d4, d5, d6, d7, d8, d9, d10, g]
can.bind("<Button-1>", lambda jk: 点击事件(jk))
can.bind("<Motion>", lambda jk: 经过事件(jk))
LOGO = tk.PhotoImage(file="辐射组Logo2.png")
LOGO = LOGO.subsample(2, 2)
tiem = th.Thread(target=运行时长)
tiem.setDaemon(True)
tiem.start()


def 点击事件(event):
    global name, 视频名字
    url22 = str(a.get())
    if 480 + 220 < event.x < 480 + 220 + 100 and 250 - 40 < event.y < 270 - 40:
        can.itemconfig(d, outline="yellow")
        can.itemconfig(d2, text="处理中", fill="red")
        if url22 is None or url22 == "":
            th.Thread(target=音效.遇到错误).start()
            ms.showwarning("警告", "您的信息是空的！")
        elif url22[:5] != "https" and url22[:2] != "BV":
            print(url22[:2])
            th.Thread(target=音效.遇到错误).start()
            ms.showwarning("警告", "您输入的信息不合规格")
        else:
            f = 信息展示(url=url22)
            try:
                can.itemconfig(g,
                               text="视频信息:\n名字:" + f[1] + f"\n作者:{f[2]}\n播放时长{f[3] // 60000}min {f[3] // 1000 % 60}s",
                               fill="black", font=("微软雅黑", 15))
                视频名字 = f[1]

            except TypeError:
                pass
    elif 960 - 140 < event.x < 960 and 20 < event.y < 50:
        if name == "未登陆你的辐射组账号":
            can.itemconfig(d12, text="正在处理", fill="red")
            辐射组账号模块()
        else:
            name = "未登陆你的辐射组账号"
            can.itemconfig(d12, text=name)
    elif 20 < event.x < 120 and 20 < event.y < 50:
        can.itemconfig(d10, outline="yellow")
        can.itemconfig(d11, text="正在处理", fill="red")
        设置()
    elif 200-30 < event.x < 350-30 and 450 < event.y < 470 and len(url2) >= 1:
        na = tf.asksaveasfilename(initialfile=视频名字, filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[0], url2[0]), 文件名称=na)
    elif 360-30 < event.x < 510-30 and 450 < event.y < 470 and len(url2) >= 2:
        na = tf.asksaveasfilename(initialfile=视频名字, filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[1], url2[1]), 文件名称=na)
    elif 520-30 < event.x < 670-30 and 450 < event.y < 470 and len(url2) >= 3:
        na = tf.asksaveasfilename(initialfile=视频名字, filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[2], url2[2]), 文件名称=na)
    elif 680 - 30 < event.x < 830 - 30 and 450 < event.y < 470 and len(url1) != 0:
        na = tf.asksaveasfilename(initialfile=视频名字, filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[0]), 文件名称=na, 额外信息="只要音频")
    elif 360 - 30 < event.x < 510 - 30 and 420 < event.y < 440 and len(url1) != 0:
        na = tf.asksaveasfilename(initialfile=视频名字, filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url2[0]), 文件名称=na, 额外信息="只要视频")
    elif 440 < event.x < 520 and 509 < event.y < 529:
        about()

    else:
        can.itemconfig(d, outline="black")
        can.itemconfig(d2, text="搜索", fill="green")


def 经过事件(event):
    if 480 + 220 < event.x < 480 + 220 + 100 and 250 - 40 < event.y < 270 - 40:
        can.config(cursor="hand2")  # 更改光标形状
        can.itemconfig(d, outline="yellow")
        can.itemconfig(d2, text="点击", fill="red")
        can.itemconfig(d9, text="可以找到视频并下载", fill="red")
    elif 20 < event.x < 120 and 20 < event.y < 50:
        can.config(cursor="hand2")
        can.itemconfig(d10, outline="yellow")
        can.itemconfig(d11, text="点击", fill="red")
        can.itemconfig(d9, text="可以更改你的背景图片", fill="red")
    elif 960 - 140 < event.x < 960 and 20 < event.y < 50:
        can.config(cursor="hand2")
        if name == "未登陆你的辐射组账号":
            can.itemconfig(d12, text="点[只因]此处登陆", fill="red")
            can.itemconfig(d9, text="登录辐射组账号，享受更多功能！", fill="#00FFFE")
        else:
            can.itemconfig(d9, text="你可以享受更多功能了同志，点击你的名字可退出登录", fill="#00FFFE")
    elif 200 - 30 < event.x < 350 - 30 and 450 < event.y < 470 and len(url2) >= 1:
        can.config(cursor="hand2")
        can.itemconfig(d3, outline="red")
        can.itemconfig(d4, text="高清", fill="red")
        can.itemconfig(d9, text="此视频bilibili网站所支持的最高画质[1080P/720P]", fill="red")
    elif 360 - 30 < event.x < 510 - 30 and 450 < event.y < 470 and len(url2) >= 2:
        can.config(cursor="hand2")
        can.itemconfig(d5, outline="red")
        can.itemconfig(d6, text="标清", fill="red")
        can.itemconfig(d9, text="此视频bilibili网站所支持的中等画质[720P/480P]", fill="red")
    elif 520 - 30 < event.x < 670 - 30 and 450 < event.y < 470 and len(url2) >= 3:
        can.config(cursor="hand2")
        can.itemconfig(d7, outline="red")
        can.itemconfig(d8, text="模糊", fill="red")
        can.itemconfig(d9, text="此视频bilibili网站所支持的较低画质[480P/360P]", fill="red")
    elif 440 < event.x < 520 and 509 < event.y < 529:
        can.config(cursor="hand2")
        can.itemconfig(d13, fill="#0000FF")
    elif 680 - 30 < event.x < 830 - 30 and 450 < event.y < 470 and len(url1) != 0:
        can.config(cursor="hand2")
        can.itemconfig(d15, outline="red")
        can.itemconfig(d14, text="音频", fill="red")
        can.itemconfig(d9, text="只下载音频，只要鬼畜乐曲的建议尝试", fill="red")
    elif 360 - 30 < event.x < 510 - 30 and 420 < event.y < 440 and len(url1) != 0:
        can.config(cursor="hand2")
        can.itemconfig(d17, outline="red")
        can.itemconfig(d16, text="无声视频", fill="red")
        can.itemconfig(d9, text="没有声音的视频，免除去音烦恼", fill="red")
    else:
        can.config(cursor="arrow")
        can.itemconfig(d, outline="black")
        can.itemconfig(d2, text="搜索", fill="green")
        can.itemconfig(d3, outline="yellow")
        can.itemconfig(d4, text="最高画质", fill="#FF00FF")
        can.itemconfig(d5, outline="yellow")
        can.itemconfig(d6, text="中等画质", fill="#FF00FF")
        can.itemconfig(d7, outline="yellow")
        can.itemconfig(d8, text="最低画质", fill="#FF00FF")
        can.itemconfig(d10, outline="#FF00FF")
        can.itemconfig(d11, text="更改图片", fill="#FFFF00")
        can.itemconfig(d12, text=name, fill="red")
        can.itemconfig(d13, fill="red")
        can.itemconfig(d15, outline="yellow")
        can.itemconfig(d14, text="只要音频", fill="#FF00FF")
        can.itemconfig(d16, text="只要视频", fill="#FF00FF")
        can.itemconfig(d17, outline="yellow")


def 设置():
    global w
    filename = tf.askopenfilename(filetypes=[("图片", "*.png")])
    with open("pictor.json", "w", encoding="utf-8") as f2:
        js.dump(filename, f2)
    if filename != "":
        w = tk.PhotoImage(file=filename)
        if w.height() == 1080:
            w = w.subsample(2, 2)
            can.itemconfig(img, image=w)
        else:
            can.itemconfig(img, image=w)
        sc.update()
    else:
        pass


def about():
    ab = tk.Toplevel(sc)
    ab.title("鲲鲲V0.2 测试版 关于我们")
    ab.geometry("960x540+230+80")
    can = tk.Canvas(ab, highlightthickness=0, width=960, height=540)  # 创建画布
    can.place(x=0, y=0)  # 大小
    img3 = can.create_image(480, 270, image=w)  # 添加图片
    can.create_text(480, 140, text="关于我们\n制作者:VRt-21th 辐射组\n编写语言:Python\n代码地址:https://github.com/NewSunMUli/jk-1\n更新:0.1 -> 0.2\n可以自定义背景和登录辐射组账号了！"
                                   "\n下一版本:将会添加更多设置和下载进度条",
                    font=(原神字体, 20, 加粗), fill="#00FAFF")
    can.create_image(480, 420, image=LOGO)


sc.mainloop()
