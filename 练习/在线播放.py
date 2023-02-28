import requests as rt
import pygame
import tempfile as tf


a = rt.get("https://other-web-ri01-sycdn.kuwo.cn/7845d45120932a05679a5bb75d66d16c/63901d3b/resource/n1/87/57/3082041059.mp3")
fp = tf.TemporaryFile(mode="w+b")
# noinspection PyTypeChecker
fp.write(a.content)
fp.seek(0)
pygame.mixer.init()
pygame.mixer.music.load(fp)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass

fp.close()
