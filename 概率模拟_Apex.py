"""此处没有界面可以给你使劲抽了"""
from 算法函数 import Apex抽奖
from 统计 import 游戏统计

list2 = []
p = 0.0
num = 0
list3 = []
x = []
g = 0
f = 0
c1 = []


for i in range(1, 500001, 1):
    f += 1
    m = Apex抽奖(次数=f)
    if m[0] == 5:
        c1.append(m)
    else:
        c1.append(0)
    if m[1]:
        f = 0
        list2.append([5,5,5])
        c1[-1] = 500
    else:
        list2.append(m[0])

for i in list2:
    g += 1
    for jk in i:
        if jk == 5:
            num += 1
    p = round(num / (g*3) * 100, 3)
    list3.append(p)
    x.append(g)


游戏统计(x=x, y=list3).凯子统计法(title="Apex",频数统计=[True, [c1]], 保底位置=500)
