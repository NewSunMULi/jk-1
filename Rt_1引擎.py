# encoding: utf-8
from typing import List
from types import FunctionType
import threading as th

import pygame as pg


class 游戏窗口:
    def __init__(self, 窗口大小: tuple = (0, 0), 是否全屏: bool = False, 窗口名字: str = "game", 图标=None):
        pg.init()
        if 是否全屏:
            self.pg = pg.display.set_mode(flags=pg.FULLSCREEN)
        else:
            self.pg = pg.display.set_mode(窗口大小)
        pg.display.set_caption(窗口名字)

    def 连接组件(self):
        return self.pg

    @staticmethod
    def 退出事件(event):
        if event.type == pg.QUIT:
            pg.quit()


class 容器异常(Exception):
    def __init__(self, why="容器错误!"):
        super().__init__()
        self.why = why

    def __str__(self):
        return self.why


class 播放异常(Exception):
    def __init__(self, why="视频播放似乎出现了点问题^_^"):
        super().__init__()
        self.why = why

    def __str__(self):
        return self.why


class 组件:
    def __init__(self):
        self.idlist = [549641]
        self.passwordlist = ["jpg114514"]

    def 开发者工具(self, id="赵靖凯孙子", password=None):
        while id not in self.idlist:
            # 输入账号的模块
            pass
        for i in range(4):
            # 输入密码的模块
            if password in self.passwordlist:
                text = "success"
                break
            if i == 3:
                text = "fail"
                break
            text = "重新输入你的密码是错的！"


class 单行文字(组件):
    def __init__(self, 文字="全世界无产者，联合起来!", 系统字体=None, 字体文件=None, 窗口=None, **kwargs):
        if 系统字体 is not None:
            self.font = pg.font.SysFont(系统字体, kwargs["字体大小"])
            self.text = self.font.render(文字, True, kwargs["字体颜色"], None)
        else:
            self.font = pg.font.Font(字体文件, kwargs["字体大小"])
            self.text = self.font.render(文字, True, kwargs["字体颜色"], None)
        self.sc = 窗口

    def 居中某组件(self, 要居中的组建对象=None, 它的x值=0, 它的y值=0):
        self.text.get_rect().center = 要居中的组建对象.get_rect().center
        self.sc.blit(self.text, (它的x值, 它的y值))

    def 有坐标展示(self, x=0, y=0):
        self.sc.blit(self.text, (x, y))


class 按钮(组件):
    def __init__(self, name="赵靖凯孙子", fg=None, text=None, x=0, y=0, 字体文件=None, zsize=50
                 , 背景图案=None, 响应图案=None, 倍数=1):
        super().__init__()
        if 字体文件 is None:
            self.ziti = pg.font.SysFont("SimSun", zsize)
        else:
            self.ziti = pg.font.Font(字体文件, zsize)
        self.text = self.ziti.render(text, True, fg, None)
        self.bd = pg.image.load(背景图案)
        self.xx = self.bd.get_rect()
        self.bd = pg.transform.scale(self.bd, ((self.xx[2] / 倍数), (self.xx[3] / 倍数)))
        self.center = self.bd.get_rect().center
        xc, yc = self.text.get_rect().center
        self.cx = x + self.center[0] - xc
        self.cy = y + self.center[1] - yc
        self.x, self.y = x, y
        self.name = name
        self.倍数 = 倍数
        if 响应图案 is not None:
            self.static = pg.image.load(响应图案)

    def 绘制(self):
        self.name.blit(self.bd, (self.x, self.y))
        self.name.blit(self.text, (self.cx, self.cy))

    def 感应(self, lan="ok"):
        self.mx, self.my = pg.mouse.get_pos()
        if (self.x <= self.mx <= self.x + self.center[0] * 2) and (self.y <= self.my <= self.y + self.center[0] * 2):
            self.bd = pg.transform.scale(self.bd, ((self.xx[2] / self.倍数 * 0.9), (self.xx[3] / self.倍数 * 0.9)))
            self.name.blit(self.bd, (self.x, self.y))
            self.name.blit(self.text, (self.cx, self.cy))
            return lan
        else:
            self.bd = pg.transform.scale(self.bd, ((self.xx[2] / self.倍数), (self.xx[3] / self.倍数)))
            self.name.blit(self.bd, (self.x, self.y))
            self.name.blit(self.text, (self.cx, self.cy))
            return "赵靖凯孙子"


class 图片插入(组件):
    def __init__(self, phname="色图.jpg", name="VRt-21th", x=None, y=None):
        super().__init__()
        self.pt = pg.image.load(phname)
        self.xy = self.pt.get_size()
        name.blit(self.pt, (x, y))
        self.x, self.y = x, y
        self.w, self.h = self.xy[0], self.xy[1]
        self.mx, self.my = pg.mouse.get_pos()
        self.phname = phname[:-5]

    def 感应(self):
        if (self.x <= self.mx <= self.x + self.w) and (self.y <= self.my <= self.y + self.h):
            return self.phname
        return "jk"

    def 大小(self):
        return self.xy


class 模型(组件):
    def __init__(self, name="孙子赵靖凯", phname="a.jpg", x=None, y=None):
        try:
            if name == "孙子赵靖凯":
                raise 容器异常("没有绘图对象咋个画图！")
        except 容器异常 as pp:
            print("name=pg.sc")
        self.mx = pg.image.load(phname)
        self.w, self.h = self.mx.get_size()
        self.x = x
        self.y = y
        self.name = name

    def 移动(self, name="赵靖凯孙子", dx=0, dy=0):
        self.x += dx
        self.y += dy
        name.blit(self.mx, (self.x, self.y))

    def 缩放(self, 倍数=1, name=None, w=0, h=0):
        if 倍数 != 1:
            self.mx = pg.transform.scale(self.mx, ((self.w / 倍数), (self.h / 倍数)))
        else:
            self.mx = pg.transform.scale(self.mx, (w, h))

    def 加载(self):
        self.name.blit(self.mx, (self.x, self.y))

    def 查看(self):
        m = "图片大小为=" + str(self.w) + "," + str(self.h)
        return m


class 视频(图片插入):
    def __init__(self, dirmv="视频区1/MV/Image", dirmu=None, name="jk", FPS=30, x=0, y=0):
        if name == "jk" or type(name) == type("jk"):
            raise 播放异常("无窗口给你放视频,name是" + name)
        self.t = pg.time.Clock()
        frame = 0
        M = True
        while M:
            try:
                self.t.tick(FPS)
                if frame == 0:
                    frame += 1
                    if dirmu is not None:
                        pg.mixer.music.load(dirmu)
                        pg.mixer.music.play()
                frame += 1
                pt = pg.image.load(dirmv + str(frame) + ".png")
                name.blit(pt, (x, y))
                for self.event in pg.event.get():
                    if self.event.type == pg.QUIT:
                        pg.quit()
                    if self.event.type == pg.KEYDOWN:
                        if self.event.key == pg.K_ESCAPE:
                            M = False
                            pg.mixer.music.stop()
                            break
                pg.display.update()
                pt = 0
            except:
                break


class 文字介绍(组件):
    def __init__(self, name=None, filename=None, fg=None, zsize=50, text="VRt-21", x=600, y=30, 每行字数=20):
        if filename is not None:
            self.jst = pg.font.Font(filename, zsize)
        else:
            self.jst = pg.font.SysFont("SimSun", zsize)
        dir1 = []
        dir2 = []
        for i in range((len(text) // 每行字数) + 2):
            if i != (len(text) // 每行字数) + 1 or len(text) % 每行字数 == 0:
                dir1.append(text[15 * (i - 1): 15 * i])
            else:
                dir1.append(text[-(len(text) % 每行字数) - 1:-1])
        for gg in dir1:
            self.js = self.jst.render(gg, True, fg, None)
            dir2.append(self.js)
        for mm in dir2:
            name.blit(mm, (x, y + zsize * dir2.index(mm)))


class 文件阅读写入(组件):
    def __init__(self, filename="ttk.txt", mode=None):
        if mode == "只写":
            m = "w"
        elif mode == "只读":
            m = "r"
        elif mode == "追加读写":
            m = "a+"
        else:
            m = "r"
        self.file = open(filename, m, encoding="utf-8")

    def 读(self):
        text = self.file.read()
        return text

    # noinspection PyBroadException
    def 写(self, text=None):
        try:
            self.file.write(text)
            return "成功"
        except:
            return "写入失败"

    def 关闭(self):
        try:
            self.file.close()
            return "关闭成功"
        except:
            return "关闭失败"

    def 隔行阅读(self):
        self.ss = self.file.readlines()
        return self.ss


class 动画效果(组件):
    def __init__(self):
        self.list1 = ['f', 'e', 'd', 'c', 'b', 'a', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']

    def 渐入(self, FP: pg.time.Clock = None, 持续时间: int = 1, FONT: pg.font = None, fps=30, 窗口=None, 坐标: tuple = (),
           text=""):
        for f in range(fps * 持续时间):
            list2 = ['f', 'e', 'd', 'c', 'b', 'a', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
            list2.reverse()
            窗口.fill("#000000")
            FP.tick(fps)
            gg = int(len(list2) / (fps * 持续时间) * f)
            R = f"#{list2[gg] * 6}"
            text2 = FONT.render(text, True, R, None)
            窗口.blit(text2, 坐标)
            pg.display.update()

    def 渐出(self, FP: pg.time.Clock = None, 持续时间: int = 1, FONT: pg.font = None, fps=30, 窗口=None, 坐标: tuple = (),
           text=""):
        for I in range(fps * 持续时间):
            窗口.fill("#000000")
            FP.tick(fps)
            g = int(len(self.list1) / (fps * 持续时间) * I)
            R = f"#{self.list1[g]}{self.list1[g]}{self.list1[g]}{self.list1[g]}{self.list1[g]}{self.list1[g]}"
            text2 = FONT.render(text, True, R, None)
            窗口.blit(text2, 坐标)
            pg.display.update()

    def 图片渐入(self, 渲染窗口: pg.Surface = None, 作用对象: pg.image.load = None, 图片路径="", x=0, y=0, 持续时间=1,
             FPS=30, 倍数=1, w=0, h=0, 并行函数=None, 条件=None):
        if 作用对象 is None:
            图片 = pg.image.load(图片路径)
        else:
            图片 = 作用对象
        w2, h2 = 图片.get_size()
        self.mx = pg.transform.scale(图片, ((w2 / 倍数), (h2 / 倍数)))
        if w != 0 and h != 0:
            self.mx = pg.transform.scale(图片, w, h)
        w1, h1 = 渲染窗口.get_rect().center
        w, h = w1 * 2, h1 * 2
        f = pg.Surface((w, h))
        time = pg.time.Clock()
        if 并行函数 is not None:
            线程 = th.Thread(target=并行函数,args=(条件[0],条件[1]))
            线程.start()
        for i in range(持续时间 * FPS):
            time.tick(FPS)
            f.set_alpha(255 - (255 / (持续时间 * FPS)) * i)
            f.fill((0, 0, 0))
            渲染窗口.blit(self.mx, (x, y))
            渲染窗口.blit(f, (0, 0))
            pg.display.update()


class 视频动画:
    def __init__(self, 窗口对象="Jk", 文字动画: List[str] = None, 图片动画: List = None, x: int = 0, y: int = 0, 字体文件="a.ttf",
                 系统字体=None, 文字对齐="居中", FPS=2, 淡出: bool = False, **kwargs):
        FP = pg.time.Clock()
        time = 0
        if 文字动画 is not None:
            for i in 文字动画:
                g = 动画效果()
                time += 1
                FP.tick(FPS)
                窗口对象.fill("#000000")
                if 字体文件 == "a.ttf":
                    self.font = pg.font.SysFont(系统字体, kwargs['字体大小'])
                else:
                    self.font = pg.font.Font(字体文件, kwargs['字体大小'])
                self.text = self.font.render(i, True, "#ffffff", None)
                self.中间位置 = self.text.get_rect().center
                self.窗口中心 = 窗口对象.get_rect().center
                居中 = (self.窗口中心[0] - self.中间位置[0], self.窗口中心[1] - self.中间位置[1])
                if 文字对齐 == "居中":
                    g.渐入(FP=FP, 持续时间=1, FONT=self.font, 窗口=窗口对象, 坐标=居中, text=i)
                    for h in range(30):
                        窗口对象.fill("#000000")
                        FP.tick(30)
                        窗口对象.blit(self.text, 居中)
                        pg.display.update()
                    g.渐出(FP=FP, 持续时间=1, FONT=self.font, 窗口=窗口对象, 坐标=居中, text=i)
                else:
                    g.渐入(FP=FP, 持续时间=1, FONT=self.font, 窗口=窗口对象, 坐标=(x,y), text=i)
                    for h in range(30):
                        窗口对象.fill("#000000")
                        FP.tick(30)
                        窗口对象.blit(self.text, (x, y))
                        pg.display.update()
                    g.渐出(FP=FP, 持续时间=1, FONT=self.font, 窗口=窗口对象, 坐标=(x,y), text=i)

        if 图片动画 is not None:
            for i in 图片动画:
                self.cartoon = pg.image.load(i)
                self.center2 = 窗口对象.blit(self.cartoon, (x, y))
                self.中间位置 = 0
                pg.display.update()


def 测试(待测试函数: FunctionType = None, 条件=(), **kwargs):
    pass


if __name__ == "__main__":
    a = 游戏窗口((600, 600), False, "测试")
    sc = a.连接组件()
    list13 = ["随着战争的开始", "旅行者借助世界之外的力量", "开始否定着这个世界", "核武器的使用正在加速着战争的进程", "在严重的核污染下，提瓦特寸草不生",
              "许多以前从未见过的怪物开始出现", "当两个世界的东西相遇，究竟会怎样呢?"]
    视频动画(sc, 文字动画=list13, 字体文件="原神字体.ttf", 字体大小=25, FPS=1)
    视频动画(sc, 文字动画=["蕉神  现代战争"], 字体文件="原神字体.ttf", 字体大小=50, FPS=0.7)
