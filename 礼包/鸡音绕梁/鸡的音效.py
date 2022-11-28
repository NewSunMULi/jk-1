from tkinter import *
from random import choice
from pygame.mixer import init, music
import time

init()
list_暗号 = ["JNTM", "ngm"]
str_input = ""


def 随机播放(event):
    list888 = ['1.mp3', '2.mp3']
    music.load(choice(list888))
    music.play()


def 音效(event):
    global str_input
    music.load("音效.mp3")
    if len(str_input) >= 4:
        str_input = ""
    if event.char == "M" and str_input == "JNT":
        str_input = ""
        music.play(start=1.1)
        can.itemconfig(d2, text="鸡你太美")
    elif event.char == "m" and str_input == "ng":
        music.load("你干嘛.mp3")
        str_input = ""
        music.play(start=1.2)
        music.fadeout(2400)
        can.itemconfig(d2, text="你干嘛哎嗨哟")
    elif event.char in "JNTM":
        if event.char == "M":
            music.play(start=1.1)
        elif event.char == "J":
            music.play(start=0.2)
        elif event.char == "N":
            music.play(start=0.5)
        elif event.char == "T":
            music.play(start=0.8)
        music.fadeout(300)
        str_input += event.char
        can.itemconfig(d2, text=str_input)
    else:
        music.load("你干嘛.mp3")
        if event.char == "n":
            music.play(start=0.38)
            music.fadeout(300)
        elif event.char == "g":
            music.play(start=0.8)
            music.fadeout(350)
        elif event.char == "m":
            music.play(start=1.2)
            music.fadeout(350)
        str_input += event.char
        can.itemconfig(d2, text=str_input)
    screen.update()


def 组合音效(event2):
    global str_input
    if str_input == list_暗号[0] and event2.keysym == "S":
        music.load("D:/提交/jk-1/音效.mp3")
        music.play()
        time.sleep(1.4)
        music.stop()
        str_input = ""


def 停止(event3):
    music.stop()


def 说明(event):
    sc = Toplevel(screen)
    sc.geometry("960x540+210+150")
    can2 = Canvas(sc, highlightthickness=0, width=960, height=540)
    can2.place(x=0, y=0)
    can2.create_text(480, 270, text="大写字母状态下按J N T M 可以放 鸡 你 太 美，如果按顺序按J N T M则会出现惊喜！\n小写字母状态下按n g m你懂得\nF1播放随机鬼畜乐曲")


if __name__ == "__main__":
    screen = Tk()
    screen.geometry("960x540+210+150")
    can = Canvas(screen, highlightthickness=0, width=960, height=540)
    can.place(x=0, y=0)
    w = PhotoImage(file="蔡徐坤2.png")
    d1 = can.create_image(480, 270, image=w)
    d2 = can.create_text(480, 270, text=str_input, font=("", 50), fill="red")
    can.create_text(480, 350, text="按F2.5可看操作说明", font=("", 30), fill="yellow")
    screen.bind("<KeyPress-S>", 组合音效)
    screen.bind("<KeyPress>", 音效)
    screen.bind("<KeyPress-A>", 停止)
    screen.bind("<F2>", 说明)
    screen.bind("<F1>", 随机播放)
    screen.mainloop()
