# encoding: utf-8
import sys
import pygame as pg
from 设置 import *

# 红楼梦小组--诗歌区
人物名 = ["判词", "秦可卿", "李纨", "王熙凤", "贾惜春", "贾迎春", "妙玉", "史湘云", "贾探春", "贾元春", "黛玉和宝钗"]
pg.init()
sc = pg.display.set_mode(flags=pg.FULLSCREEN)  # pg.FULLSCREEN全屏
xy = sc.get_rect()
print(xy)
color = (255, 255, 255)
pg.display.set_caption("work_1")
center = xy.center
m = 0
chance = 3
xxx = 1
视频(name=sc, dirmv="视频区1/LH/Image", FPS=30,dirmu="视频区1/music2.mp3")
daan = 0
mmb = False


class Head:
    def __init__(self):
        self.ac = True

    def RUN(self, position=False, past=1):
        global 人物名
        self.ac = "None"
        tz = None
        if position and past == 1:
            self.ji = 模型(name=sc, phname="界面.png", x=0, y=0)
            self.ji.缩放(name=sc, w=1536, h=864)
            self.aa = True

        if position and past == 2:
            if self.aa:
                self.m = 3072
                self.aa = False
            self.ji = 模型(name=sc, phname="介绍.jpeg", x=self.m, y=0)
            if self.m > 0:
                self.m -= 250
            if self.m < 0:
                self.m = 0
            self.ji.缩放(name=sc, w=1536, h=864)

        if position and past == 3:
            ttf = "字体01.ttf"
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            按钮(name=sc, bg=(0, 0, 0), fg=(0, 0, 0), text="人物目录", x=40, y=70, w=0, h=0, zsize=150, 字体文件=ttf)
            dir = []
            for i in range(11):
                if i <= 5:
                    i = 按钮(name=sc, bg=(255, 255, 255), fg=(0, 0, 0), text=人物名[i], x=40, y=280 + 60 * i, w=100,
                           h=50,
                           zsize=50,
                           字体文件=ttf)
                else:
                    i = 按钮(name=sc, bg=(255, 255, 255), fg=(0, 0, 0), text=人物名[i], x=xy[3] - 40,
                           y=280 + 60 * (i - 5 - 1),
                           w=100, h=50,
                           zsize=50,
                           字体文件=ttf)
                dir.append(i)
            for jk in dir:
                if jk.感应() == "ok":
                    tz = 人物名[dir.index(jk)]

        self.bu = 按钮(sc, (211, 105, 200), (255, 0, 0), "退出", xy[2] - 50 * 2, 0, 50, 50)
        self.enter = 按钮(sc, (211, 105, 200), (255, 0, 0), "Enter", 0, 0, 50, 50)
        感应1 = self.bu.感应()
        感应2 = self.enter.感应()
        for event in pg.event.get():
            if 感应1 == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                pg.quit()
                sys.exit()
            if 感应2 == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                self.ac = "-1"
                past -= 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F12:
                    pass
                    # 视频(name=sc, dirmu="视频区1/music.mp3")
                if event.key == pg.K_F5:
                    print("欢迎来到\"VRt-21\"开发者模式")
                if event.key == pg.K_d:
                    self.ac = "back 1"
                    past -= 1
            if (感应1 != "ok" and 感应2 != "ok") and event.type == pg.MOUSEBUTTONDOWN and past < 3:
                past += 1
            if tz is not None and event.type == pg.MOUSEBUTTONDOWN:
                self.ac = tz
        pg.display.update()
        return past, self.ac


class Text:
    def __init__(self):
        self.ac = "success to 2"
        self.ren = 人物名
        self.ren: list
        模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
        self.gy = False

    def RUN(self, pos=False, past=1):
        global chance
        global xxx
        global daan
        global mmb
        qq = 0
        self.ac = "qq"
        if 1 <past < 12:
            mm = 文件阅读写入(filename=self.ren[past - 1] + ".txt")
            text2 = mm.读()
            mm.关闭()
        if pos:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
        if pos and past == 1:
            模型(sc, "人物照片/判词.png", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            jj = 0
        elif pos and past == 2:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            xx = qq.大小()
            jj = qq.感应()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=40, text=text2, 每行字数=16, x=xx[0] + 70, y=40)
        elif pos and past == 3:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 4:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 5:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            xx = qq.大小()
            jj = qq.感应()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 6:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 7:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 8:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 9:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 10:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 11:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 102:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            qq = 图片插入(name=sc, phname="人物照片/" + self.ren[past - 1] + ".png", x=45, y=40)
            jj = qq.感应()
            xx = qq.大小()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=50, text=text2, 每行字数=16, x=xx[0] + 70)
        elif pos and past == 101:
            gm = 文件阅读写入(qq + "诗集.txt")
            te = gm.读()
            gm.关闭()
            文字介绍(name=sc, fg=(0, 0, 0), zsize=80, text=te, x=100, y=50, 每行字数=7)
        elif pos and past == 12:
            if chance != 0:
                self.dati = True
            if True:
                模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
                按钮(sc, fg=(0, 0, 0), text="欢迎来到", zsize=80, y=90)
                按钮(sc, fg=(0, 0, 0), text="猜灯谜环节", zsize=50, y=190)
                self.op = 文件阅读写入(filename="./灯谜/" + str(xxx) + ".txt")
                self.dengmi = self.op.读()
                self.op.关闭()
                self.d = 文件阅读写入(filename="./灯谜/dn" + str(xxx) + ".txt")
                self.dn = self.d.隔行阅读()
                self.d.关闭()
                文字介绍(sc, None, (0, 0, 0), text=self.dengmi, x=20, y=260, 每行字数=25, zsize=40)
                list3 = []
                for ss in range(4):
                    self.gg = 按钮(sc, (114, 114, 191), (0, 0, 0), self.dn[ss], x=200 + 300*ss, y=500,h=40)
                    list3.append(self.gg)
                for gym in list3:
                    self.gy = gym.感应()
                    if self.gy == "ok" and chance != 0:
                        daan = self.dn[list3.index(gym)]
                        break

        self.bu = 按钮(sc, (211, 105, 200), (255, 0, 0), "退出", xy[2] - 50 * 2, 0, 50, 50)
        self.enter = 按钮(sc, (211, 105, 200), (255, 0, 0), "Enter", 0, 0, 50, 50)
        感应1 = self.bu.感应()
        感应2 = self.enter.感应()
        for event in pg.event.get():
            if 感应1 == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                pg.quit()
                sys.exit()
            if 感应2 == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                self.ac = "-1"
                past -= 1
            if past < 12:
                if jj in self.ren and event.type == pg.MOUSEBUTTONDOWN:
                    past = 101
            if self.gy == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                if daan.rstrip() == self.dn[4]:
                    mmb = True
                    chance = 0
                elif daan.rstrip() != self.dn[4]:
                    chance -= 1
                    mmb = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F12:
                    pass
                    # 视频(name=sc, dirmu="视频区1/music.mp3")
                if event.key == pg.K_F5:
                    print("欢迎来到\"VRt-21\"开发者模式")
                if event.key == pg.K_d and past > 1:
                    self.ac = "back 1"
                    past -= 1
                if event.key == pg.K_F1:
                    self.ac = "x -1,past=3"
            if (感应1 != "ok" and 感应2 != "ok") and event.type == pg.MOUSEBUTTONDOWN and past < 12:
                past += 1
            if (感应1 != "ok" and 感应2 != "ok" and self.gy != "ok") and event.type == pg.MOUSEBUTTONDOWN and past == 12:
                print(xxx)
                xxx += 1
                chance = 3
                if xxx == 8:
                    self.ac = "End"
            if mmb:
                if daan.rstrip() == self.dn[4]:
                    按钮(sc, (114, 114, 191), (0, 0, 0), "回答正确", x=600, y=600)
                else:
                    按钮(sc, (114, 114, 191), (0, 0, 0), "回答错误", x=600, y=600)
        print(mmb)
        pg.display.update()
        return past, self.ac


class End:
    def __init__(self):
        视频(dirmv="视频区1/thanks/Image", dirmu="视频区/music3.mp3", name=sc)

    def RUN(self, pos=False, past=1):
        g = 模型(sc, x=0, y=0)
        self.bu = 按钮(sc, (211, 105, 200), (255, 0, 0), "退出", xy[2] - 50 * 2, 0, 50, 50)
        self.enter = 按钮(sc, (211, 105, 200), (255, 0, 0), "Enter", 0, 0, 50, 50)
        感应1 = self.bu.感应()
        感应2 = self.enter.感应()
        for event in pg.event.get():
            if 感应1 == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                pg.quit()
                sys.exit()
            if 感应2 == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                self.ac = "-1"
                past -= 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F12:
                    pass
                    # 视频(name=sc, dirmu="视频区1/music.mp3")
                if event.key == pg.K_F5:
                    print("欢迎来到\"VRt-21\"开发者模式")
                if event.key == pg.K_d and past > 1:
                    self.ac = "back 1"
                    past -= 1
                if event.key == pg.K_F1:
                    self.ac = "x -1,past=3"
            if (感应1 != "ok" and 感应2 != "ok") and event.type == pg.MOUSEBUTTONDOWN and past < 14:
                past += 1
        pg.display.update()
        return past, self.ac


if __name__ == "__main__":
    xu = [Head(), Text(), End()]
    x, y, z = 0, 1, 1
    while True:
        past, ac = xu[x].RUN(True, y)
        if past != y:
            y = past
        if ac == "x -1,past=3":
            x = 0
            y = 3
        if ac in 人物名:
            x = 1
            y = 人物名.index(ac) + 1
        if ac == "End":
            x = 2
            y = 2