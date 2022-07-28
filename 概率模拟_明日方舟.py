"""此处没有界面可以给你使劲抽了"""
from 算法函数 import 明日方舟抽卡
from 统计 import 游戏统计

list2 = []
p = 0.0
num = 0
list3 = []
x = []
g = 0
m = 0
c1 = []

for i in range(1, 1000001, 1):
    m += 1
    m1 = 明日方舟抽卡(相对抽奖次数=m)
    if m1[0] == 6:
        c1.append(m)
    else:
        c1.append(0)
    if m1[1]:
        m = 0
    list2.append(m1[0])

for i in list2:
    g += 1
    if i == 6:
        num += 1
    p = round(num / g * 100, 3)
    list3.append(p)
    x.append(g)


游戏统计(x=x, y=list3).凯子统计法(title="明日方舟", 频数统计=[True, [c1]], 保底位置=100)