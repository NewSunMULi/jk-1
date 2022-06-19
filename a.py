import pygame as pg
from 设置 import *
import sys

pg.init()
sc = pg.display.set_mode(flags=pg.FULLSCREEN)  # pg.FULLSCREEN全屏
xy = sc.get_rect()
print(xy)
color = (255, 255, 255)
pg.display.set_caption("work_1")
xxx = 1
chance = 3
模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
mm = pg.time.Clock()
daan = 0
yidong = False
shz = None
d = 0
计数君 = 3


class Game:
    模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])

    def __init__(self):
        global xxx
        global chance
        global daan
        global yidong
        global shz
        global d
        global 计数君
        if xxx == 8:
            模型(sc,"感谢.png",0,0).缩放(sc,xy[2],xy[3])
        else:
            模型(sc, "面板.jpeg", 0, 0).缩放(name=sc, w=xy[2], h=xy[3])
            if xxx == 1 and chance == 3:
                self.pd = None
                yidong = False
            else:
                self.pd = True
            if d == 1:
                chance += 4
                shz = None
                d = 0
            print(self.pd)
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
                self.gg = 按钮(sc, (114, 114, 191), (0, 0, 0), self.dn[ss], x=200 + 300 * ss, y=500, h=120)
                list3.append(self.gg)
            for gym in list3:
                self.gy = gym.感应()
                if self.gy == "ok" and chance != 0:
                    self.daan = self.dn[list3.index(gym)]
                    break
                self.daan = "5"
            daan = self.daan

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
                if self.gy == "ok" and event.type == pg.MOUSEBUTTONDOWN and chance >= 0:
                    chance -= 1
                    self.pd = True
                else:
                    daan = "5"
                if (感应1 != "ok" and 感应2 != "ok" and self.gy != "OK") and event.type == pg.MOUSEBUTTONDOWN and chance == -1:
                    d = xxx
                    xxx += 1
                    if xxx == 8:
                        self.ac = "End"
            if self.pd:
                if daan.rstrip() == self.dn[4] and daan != "5" or shz:
                    按钮(sc, (114, 114, 191), (0, 0, 0), "回答正确", x=600, y=600)
                    shz = True
                    chance = -1
                if (chance != 3 and daan.rstrip() != self.dn[4] and daan != "5") or (not shz and (shz is not None) and daan != "5"):
                    计数君 = chance
                    shz = False
                    if 计数君 == 0 or 计数君 == -1:
                        按钮(sc, (114, 114, 191), (0, 0, 0), "你三次都错，正确答案"+self.dn[4], x=xy.center[0]-300, y=600)
                        chance = -1
                    else:
                        按钮(sc, (114, 114, 191), (0, 0, 0), "回答错误", x=600, y=600)

            按钮(sc, (114, 114, 191), (0, 0, 0), str(chance), x=xy[2]-200, y=40)
        pg.display.update()


if __name__ == '__main__':
    while True:
        mm.tick(30)
        a = Game()
