"""基本常量"""
import json as js
from typing import List, AnyStr

# 注释死都不用马语
"""一些常量"""
列表 = List
所有字符 = AnyStr
x, y = 800, 600
信息 = ["昵称", "出生年月", "作品", "最近使用"]
检索 = ["账号", "密码", "昵称", "认证", "资料"]
斜体 = "italic"
加粗 = "bold"
大小 = f"{x}x{y}+300+150"
华体 = "华光钢铁直黑 可变体 Bold"
统一码 = "utf-8"
原神字体 = "汉仪文黑-85W Heavy"

"""一些数据"""
with open('账号.json', "r", encoding="utf-8") as f:
    user_list = js.load(f)
with open('密码.json', "r", encoding="utf-8") as f:
    user_password = js.load(f)
with open('昵称.json', "r", encoding="utf-8") as f:
    user_name = js.load(f)
with open('认证.json', "r", encoding="utf-8") as f:
    ID = js.load(f)
# with open('头像.json', "r", encoding="utf-8") as f:
# 头像: 列表[所有字符] = js.load(f)
with open('资料.json', "r", encoding="utf-8") as f:
    个人资料: 列表[所有字符] = js.load(f)
with open("WST.json","r",encoding="utf-8") as f:
    WST = js.load(f)
with open("RTY.json","r",encoding="utf-8") as f:
    RTY = js.load(f)
'''log = Button(sc, text="登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=登录和注册, width=300, anchor="w")
    log.place(self=659, y=50)
    Label(sc, text="             ", font=("微软雅黑", 8, 斜体,), fg="green").place(self=660, y=79)
    Label(sc, text="             ", font=("微软雅黑", 8, 斜体,), fg="green", width=100, anchor="w").place(self=720, y=79)'''

"""
screen = pygame.display.set_mode((1600, 900)) # 创建屏幕
 
# 省略其他与本文无关的部分
 
screen.fill(0， 0， 0)
window = pygame.Surface((800, 800))           # 创建一个窗口
window.set_alpha(1)                           # 这个值越小越透明
window.fill((255, 255, 255))  
screen.blit(window, (0, 0))

"""