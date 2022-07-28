"""无界面操作"""
from 算法函数 import 米FA游游戏抽卡
from 统计 import 游戏统计

g = 0
l1 = []
l2 = []
x = []
m = 0
ci = []

for i in range(1500000):
    g += 1
    x.append(i + 1)
    f = 米FA游游戏抽卡().崩坏3抽卡(相对次数=g)
    if f[2][1] == "S":
        ci.append(g)
    else:
        ci.append(0)
    if f[1]:
        g = 0
    l1.append(f[2][1])

g = 0

for jk in l1:
    g += 1
    if jk == "S" or jk == "A" or jk == "B":
        m += 1
    l2.append(round(m / g * 100, 4))

游戏统计(x=x, y=l2).凯子统计法("崩坏三", 50, 频数统计=[True, [ci]], 保底位置=100)
