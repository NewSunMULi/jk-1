"""tk功能区，一些快捷功能打包好就放这里
顺便说一句，从今以后函数,变量,类我尽量不用马语来命名"""
import json as 加瓦
import urllib.parse
import moviepy.editor as me
import requests as 请求
from 概率模拟_原神 import *
import os
from tkinter import messagebox, filedialog


class 窗口异常(Exception):
    def __init__(self, why):
        """
        返回窗口异常
        """
        super().__init__()
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


def 字符变量(窗口变量=None, 字符: str = None, tips特殊列表=None):
    if tips特殊列表 is None:
        tips特殊列表 = []
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


class tk_requests:
    def __init__(self, url=None, header=None, print_way=None, system_class="music"):
        if url is None:
            self.url = "https://ys.mihoyo.com"
        self.prw = print_way
        self.cls = system_class
        self.head = header


class tk爬虫_中文版(tk_requests):
    def __init__(self, print_way="tk Button Print", cls="music"):
        super().__init__(print_way=print_way, system_class=cls)

    def 音乐爬虫(self, 音乐名字: str = None, 歌手="", **额外信息):
        if self.cls == "music" or self.cls == "音乐":
            keyword = urllib.parse.quote(音乐名字)
            self.url = [
                'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(
                    keyword)]
            referer = ['https://www.kuwo.cn/search/list?key={}'.format(keyword)]
            self.head = {
                'Cookie': '_ga=GA1.2.337131840.1656857132; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1656857131,1658635516; _gid=GA1.2.992504106.1658635516; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1658636222; kw_token=KUUKU45TJK',
                'csrf': 'KUUKU45TJK',
                'Referer': '{}'.format(referer[0]),
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            }
            a = 请求.get(url=self.url[0], headers=self.head)
            list2 = 加瓦.loads(a.text)["data"]["list"]
            歌曲列表1 = []
            结果2 = []
            for name in list2:
                歌曲列表1.append({"歌曲名": name['name'], "歌手": name['artist'], "rid识别号": name['rid']})  # 爬数据
                if name['artist'] == 歌手:
                    结果2.append({"歌曲名": name['name'], "歌手": name['artist'], "rid识别号": name['rid']})
                else:
                    pass
            if 歌手 == "":
                结果2 = 歌曲列表1
            if self.prw == "Dos Print":
                x = 0
                for i in 歌曲列表1:
                    x += 1
                    print(x, i["歌曲名"], i["歌手"])
                return 结果2
            elif self.prw == "tk Button Print":
                tk_sc = 额外信息["父容器"]
                x = 0
                容器 = Frame(tk_sc, width=800, height=800)
                tk_sc.geometry(f"800x800+300+0")
                容器.place(x=40, y=180)
                for jk in 歌曲列表1:
                    x += 1
                    Label(容器, text=f"{x}.{jk['歌曲名']}--{jk['歌手']}", font=("", 8)).place(x=0, y=19 * x)
                    Button(容器, text=f"下载",
                           command=lambda 识别=jk['rid识别号'], 名字=jk['歌曲名']: self.音乐下载(识别, name=名字), bd=0,
                           font=("", 8)).place(x=660, y=19 * x)
                    Button(容器, text=f"播放",
                           command=lambda 识别=jk['rid识别号']: self.音乐播放(识别), font=("", 8)).place(x=690, y=19 * x)
                print(歌曲列表1)

    def 音乐下载(self, 识别号=0, name=None):
        try:
            b = 请求.get(f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={识别号}&type=mv',
                       headers=self.head)
            print(加瓦.loads(b.text))
            歌曲文件 = 加瓦.loads(b.text)['data']['url']
            歌曲 = 请求.get(歌曲文件, headers=self.head)  # 下载
            if name != "aaa":
                name = filedialog.asksaveasfilename(defaultextension=".mp3", initialfile="音乐", filetypes=[("MP3音乐文件", ".mp3")])
            with open("111.mp4", "wb") as f6:
                f6.write(歌曲.content)
            au = me.VideoFileClip("111.mp4")
            at = au.audio
            print(name)
            at.write_audiofile(name)
            au.close()
            os.remove("111.mp4")
        except KeyError:
            print("无MV")
            b = 请求.get(f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={识别号}',
                       headers=self.head)
            print(加瓦.loads(b.text))
            歌曲文件 = 加瓦.loads(b.text)['data']['url']
            歌曲 = 请求.get(歌曲文件, headers=self.head)  # 下载
            if name != "aaa":
                name = filedialog.asksaveasfilename(filetypes=[("MP3音乐文件", "*mp3")])
            with open(name, "wb") as f6:
                f6.write(歌曲.content)
        finally:
            pass

    def 音乐播放(self, rid1=0):
        self.音乐下载(识别号=rid1, name="aaa.mp3")
        pg.mixer.init()
        pg.mixer.music.load("aaa.mp3")
        pg.mixer.music.play()
        if not pg.mixer.music.get_busy():
            os.remove("aaa.mp3")


if __name__ == "__main__":
    print("你已经进入辐射组协议代码区")
    辐射组协议(ID="辐射组组长", PASSWORDS="z555r5555")
