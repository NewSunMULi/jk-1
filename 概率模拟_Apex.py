"""此处没有界面可以给你使劲抽了"""
from 算法函数 import Apex抽奖
from 统计 import 游戏统计

list2 = []
p = 0.0
num = 0
list3 = []
x = []
g = 0

for i in range(1, 500001, 1):
    m = Apex抽奖(次数=i)
    list2.append(m)

for i in list2:
    g += 1
    if i == 6:
        num += 1
    p = round(num / g * 100, 3)
    list3.append(p)
    x.append(g)


游戏统计(x=x, y=list3).凯子统计法(title="Apex")
