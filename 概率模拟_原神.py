from tkinter import *
from Rt_1引擎 import *
from 算法函数 import 原神抽卡

cl = pg.time.Clock()
抽奖相对次数 = 0
总次数 = 0
五星概率 = 0.006
四星概率 = 0.031
概率增幅系数 = 30
增幅起始位置 = 74
保底控制 = False
储存列表 = []
临时列表 = []
保底角色 = "荒泷一斗"


def 概率修改器():
    global 五星概率
    global 四星概率
    global 概率增幅系数

    def 提交():
        global 五星概率
        global 四星概率
        global 概率增幅系数
        五星概率 = float(SSR.get())
        四星概率 = float(SR.get())
        概率增幅系数 = int(up.get())
        发 = Label(f, text="提交成功")
        发.place(x=0, y=300)
        f.after(2000, 发.destroy)

    f = Tk()
    f.geometry("400x400+300+125")
    Label(f, text="概率修改器", font=("汉仪文黑-85W Heavy", 20)).place(x=0, y=0)
    Label(f, text="五星概率", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=50)
    Label(f, text="四星概率", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=100)
    Label(f, text="五星概率增幅系数", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=150)
    SSR = Entry(f)
    SR = Entry(f)
    SSR.place(x=100, y=53)
    SR.place(x=100, y=103)
    up = Entry(f)
    up.place(x=170, y=153)
    SSR.insert(END, 五星概率)
    SR.insert(END, 四星概率)
    up.insert(END, 概率增幅系数)
    提交 = Button(f, text="修改好了提交", bd=1, font=("汉仪文黑-85W Heavy", 15), command=提交)
    提交.pack(side=BOTTOM)
    f.mainloop()


def 概率模拟_原神():
    global 五星概率
    global 四星概率
    global 概率增幅系数
    pg.init()
    界面 = pg.display.set_mode((int(852), int(480)))
    pg.display.set_caption("原神抽卡模拟器")
    x = 0
    yd = 模型(界面, "./概率模拟-原神/一斗.png", 180, 50)
    yd.缩放(倍数=3, name=界面)
    f = 按钮(界面, fg="#000000", text="来一发", x=650, y=430, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/抽奖按钮.png'
           , 倍数=1.7)
    f10 = 按钮(界面, fg="#000000", text="来十发", x=500, y=430, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/抽奖按钮.png'
             , 倍数=1.7)
    概率修改 = 按钮(界面, fg="#000000", text="更改概率", x=40, y=435, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/兑换按钮.png'
              , 倍数=1.5)

    # 视频动画(窗口对象=界面, 文字动画=["昆十二中数学建模小组 制作", "前端 陈玄", "算法 陈玄,王文健", "后台统计 赵靖凯", "素材 原神官方和b站up主"],
    # 字体文件="原神字体.ttf", 文字对齐="居中", FPS=1, 淡出=True, 字体大小=35)

    def 统计():
        global 五星概率
        global 四星概率
        global 概率增幅系数
        pass

    def 抽奖动画(次数=1):
        global 五星概率
        global 四星概率
        global 概率增幅系数
        global 抽奖相对次数
        global 总次数
        global 保底控制

        print("相对次数")
        if 次数 == 1:
            if 次数 == 1:
                抽奖相对次数 += 1
                总次数 += 1
                g = 原神抽卡(第几次=抽奖相对次数, 大小保底控制=保底控制)
                储存列表.append(g[0])
                print("您获得了", g, 保底控制)
                if 抽奖相对次数 == 90:
                    抽奖相对次数 = 0
                if g[1] == 5:
                    视频(dirmv=f"./概率模拟-原神/单抽出金/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                    抽奖相对次数 = 0
                    if 保底角色 == g[1]:
                        保底控制 = False
                    else:
                        保底控制 = True
                elif g[1] == 4:
                    视频(dirmv=f"./概率模拟-原神/单抽出紫/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                else:
                    视频(dirmv=f"./概率模拟-原神/单抽出蓝/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)

        if 次数 == 10:
            for i in range(1, 11, 1):
                抽奖相对次数 += 1
                总次数 += 1
                g = 原神抽卡(第几次=抽奖相对次数, 大小保底控制=保底控制)
                临时列表.append(g[1])
                储存列表.append(g[0])
                print("您获得了：", g, 保底控制)
            if 抽奖相对次数 == 90:
                抽奖相对次数 = 0
            if 5 in 临时列表:
                视频(dirmv=f"./概率模拟-原神/十连出金/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                抽奖相对次数 = 0
                if 保底角色 in 储存列表[-10:-1]:
                    保底控制 = False
                else:
                    保底控制 = True
                临时列表.clear()
            else:
                视频(dirmv=f"./概率模拟-原神/十连出紫/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                临时列表.clear()

    while True:
        cl.tick(60)
        界面.fill("#000000")
        x += 1
        图片插入(f"./概率模拟-原神/背景壁纸/image{x}.png", 界面, 0, 0)
        单行文字("祈愿", 字体文件="原神字体.ttf", 窗口=界面, 字体大小=30, 字体颜色="#00FFFF").有坐标展示(10, 10)
        单行文字(f"次数:{总次数}", 字体文件="原神字体.ttf", 窗口=界面, 字体大小=30, 字体颜色="#00FFFF").有坐标展示(10, 40)
        yd.加载()
        xh = f.感应()
        sh = f10.感应()
        fh = 概率修改.感应()
        if x == 1142:
            x = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if xh == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                抽奖动画()
            if sh == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                抽奖动画(10)
            if fh == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                概率修改器()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1:
                    抽奖动画(10)
                if event.key == pg.K_F2:
                    抽奖动画(1)
        pg.display.update()


if __name__ == "__main__":
    概率模拟_原神()
