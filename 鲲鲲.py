import tkinter as tk
import tkinter.filedialog as tf
import tkinter.messagebox as ms
import requests as rt
import re
import json as js
from moviepy.editor import *
import threading as th
import os
import time
import pygame.mixer as mm

url1 = []
url2 = []
MP42 = None
head = {
    'referer': 'https://www.bilibili.com/video',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
}


def 信息展示(url):
    try:
        if url[0] != "B":
            bi = rt.get(url, headers=head)
        else:
            bi = rt.get(f"https://bilibili.com/video/{url}", headers=head)
        清晰度 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        系数 = 0
        刻度 = 0
        title = re.findall('<meta data-vue-meta="true" itemprop="name" name="title" content=(.*?)>', bi.text)
        anchor = re.findall('<meta data-vue-meta="true" itemprop="author" name="author" content=(.*?)>', bi.text)
        title = title[0][-len(title[0]) + 1:-15]
        anchor = anchor[0][-len(title[0]) + 2:-1]
        res = re.findall("<script>window\.__playinfo__=(.*?)</script>", bi.text)[0]
        data = js.loads(res)
        time = data['data']['timelength']
        for i in range(3):
            url1.append(data['data']['dash']['audio'][i]['baseUrl'])
            url2.append(data['data']['dash']['video'][i * 3]['base_url'])
        return url2, title, anchor, time
    except:
        ms.showwarning("警告", "网络呢？被狗吃了？")


def 视频爬取(url_list=None, name=None):
    global MP42
    s = rt.get(url_list[0], headers=head)
    with open(name[:-3] + ".mp3", "wb") as f:
        sc.update()
        can.itemconfig(d9, text=f"文件大小{len(s.content) / 1000}KB,已在下载")
        f.write(s.content)
    s = rt.get(url_list[1], headers=head)
    with open(name[:-3] + ".mp4", "wb") as f:
        f.write(s.content)
    ad = AudioFileClip(name[:-3] + ".mp3")
    vd = VideoFileClip(name[:-3] + ".mp4")

    def da(mp3=ad, MP4: VideoFileClip = vd):
        global MP42
        MP42 = MP4.set_audio(mp3)
        MP42.write_videofile(f'{name}.mp4')
        can.itemconfig(d9, text="视频已完全下载")
        try:
            os.remove(name[:-3] + ".mp3")
            os.remove(name[:-3] + ".mp4")
        except:
            time.sleep(10)
            os.remove(name[:-3] + ".mp3")
            os.remove(name[:-3] + ".mp4")
        mm.init()
        mm.music.load("音效.mp3")
        ms.showinfo("来自鲲鲲的提示", "小黑子，视频已完全下载完，食不食油饼?")
        mm.music.play()
        time.sleep(6)
        mm.music.stop()
        url1.clear()
        url2.clear()

    sc.update()
    th.Thread(target=da).start()


sc = tk.Tk()
sc.title("鲲鲲V0.1试行版")
sc.geometry("960x540+230+80")
sc.attributes("-alpha", 0.9)  # 透明度设置
w = tk.PhotoImage(file="老婆.png")
w = w.subsample(2, 2)
can = tk.Canvas(sc, highlightthickness=0, width=960, height=540)  # 创建画布
can.place(x=0, y=0)  # 大小
can.create_image(480, 270, image=w)  # 添加图片
can.create_text(480, 50, text="鲲鲲 试行版", fill="black", font=("微软雅黑", 35))
can.create_text(366, 230 - 40, text="在此输入你要下载的视频的BV号或具体网址:", fill="blue", font=("微软雅黑", 13))
d = can.create_rectangle(480 + 220, 270 - 20 - 40, 480 + 320, 270 - 40)
d2 = can.create_text((480 + 220 + 50), 260 - 40, text="搜索", fill="green", font=("微软雅黑", 12))
a = tk.Entry(sc, bd=0, width=70)
a.place(x=200, y=250 - 40)
g = can.create_text(366, 270 + 65, text="")
d3 = can.create_rectangle(200, 450, 350, 470, outline="yellow")
d4 = can.create_text(275, 460, text="下载视频 720p", fill="green", font=("微软雅黑", 12))
d5 = can.create_rectangle(360, 450, 510, 470, outline="yellow")
d6 = can.create_text(435, 460, text="下载视频 480p", fill="green", font=("微软雅黑", 12))
d7 = can.create_rectangle(520, 450, 670, 470, outline="yellow")
d8 = can.create_text(595, 460, text="下载视频 360p", fill="green", font=("微软雅黑", 12))
d9 = can.create_text(480, 480, text="无额外信息", fill="green", font=("微软雅黑", 12))
can.bind("<Button-1>", lambda jk: 点击事件(jk))
can.bind("<Motion>", lambda jk: 经过事件(jk))


def 点击事件(event):
    url22 = str(a.get())
    if 480 + 220 < event.x < 480 + 220 + 100 and 250 - 40 < event.y < 270 - 40:
        can.itemconfig(d, outline="yellow")
        can.itemconfig(d2, text="处理中", fill="red")
        if url22 is None or url22 == "":
            ms.showwarning("警告", "您的信息是空的！")
        elif url22[:5] != "https" and url22[:2] != "BV":
            print(url22[:2])
            ms.showwarning("警告", "您输入的信息不合规格")
        else:
            f = 信息展示(url=url22)
            try:
                can.itemconfig(g, text="视频信息:\n名字:" + f[1] + f"\n作者:{f[2]}\n播放时长{f[3] // 60000}min {f[3] // 1000 % 60}s",
                           fill="black", font=("微软雅黑", 15))
            except TypeError:
                pass
    elif 200 < event.x < 350 and 450 < event.y < 470 and len(url1) != 0:
        na = tf.asksaveasfilename(initialfile="视频", filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[0], url2[0]), name=na)
    elif 360 < event.x < 510 and 450 < event.y < 470 and len(url1) != 0:
        na = tf.asksaveasfilename(initialfile="视频", filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[1], url2[1]), name=na)
    elif 520 < event.x < 670 and 450 < event.y < 470 and len(url1) != 0:
        na = tf.asksaveasfilename(initialfile="视频", filetypes=[("只是个名字", "*any")])
        视频爬取(url_list=(url1[2], url2[2]), name=na)

    else:
        can.itemconfig(d, outline="black")
        can.itemconfig(d2, text="搜索", fill="green")


def 经过事件(event):
    if 480 + 220 < event.x < 480 + 220 + 100 and 250 - 40 < event.y < 270 - 40:
        can.itemconfig(d, outline="yellow")
        can.itemconfig(d2, text="点击", fill="red")
    elif 200 < event.x < 350 and 450 < event.y < 470 and len(url1) != 0:
        can.itemconfig(d3, outline="red")
        can.itemconfig(d4, text="高清", fill="red")
    elif 360 < event.x < 510 and 450 < event.y < 470 and len(url1) != 0:
        can.itemconfig(d5, outline="red")
        can.itemconfig(d6, text="标清", fill="red")
    elif 520 < event.x < 670 and 450 < event.y < 470 and len(url1) != 0:
        can.itemconfig(d7, outline="red")
        can.itemconfig(d8, text="模糊", fill="red")
    else:
        can.itemconfig(d, outline="black")
        can.itemconfig(d2, text="搜索", fill="green")
        can.itemconfig(d3, outline="yellow")
        can.itemconfig(d4, text="下载视频 720p", fill="green")
        can.itemconfig(d5, outline="yellow")
        can.itemconfig(d6, text="下载视频 480p", fill="green")
        can.itemconfig(d7, outline="yellow")
        can.itemconfig(d8, text="下载视频 360p", fill="green")


sc.mainloop()
