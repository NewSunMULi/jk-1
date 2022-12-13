import pynput as put
from pygame.mixer import init, music
import threading as th

str_input = ""


def 播放(event):
    try:
        global str_input
        init()
        event = event
        music.load("音效.mp3")
        if event.char == "m":
            music.play(start=1.05)
        elif event.char == "j":
            music.play(start=0.2)
        elif event.char == "n":
            music.play(start=0.5)
        elif event.char == "t":
            music.play(start=0.8)
        music.fadeout(300)
    except AttributeError:
        pass


def 线程(event):
    th.Thread(target=lambda g=event: 播放(g)).start()


try:
    f = put.keyboard.Listener(on_press=播放)
    f.start()
    f.join()
except AttributeError:
    pass
