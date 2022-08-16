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

'''for i in range(1, 10000001, 1):
    m += 1
    m1 = 明日方舟抽卡(相对抽奖次数=m).VC算法()
    if m1[0] == 6:
        c1.append(m)
        m = 0
    else:
        c1.append(0)
    list2.append(m1[0])'''

m2 = 明日方舟抽卡(算法选择="W-1.1").W算法(200000000000000000000000, 20000000, 10000000, "啊和森蚺卡池")

for i in m2[-1]['统计API']:
    m += 1
    x.append(m)
    if i in m2[-3]["卡池信息"][0] or i in m2[-3]["卡池信息"][1]:
        g += 1
    list3.append(round(g/m*100, 3))


游戏统计(x=x, y=list3).凯子统计法(title="明日方舟", 频数统计=[True, [m2[-2]["频率"]], None], 保底位置=100)
