import random

NO_S_TIMES = 0

# 8=s级女武神7=s级碎片6=A武神5=A武神碎片4=B武神/3=四星武器加圣痕2=三星武器加圣痕/1=其他材料
jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
            3,
            4, 4, 4, 4, 4, 4,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            7, 8, 8]

bd = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8]

s_bd = "健哥"
s_wu = ['健哥', '数据主宰.陈老师']
s_wusui = ['健哥碎片', '数据主宰.陈老师碎片']
a_wu = ['钢铁长城.王文健', '怒海狂涛.赵婧凯', '铁塔尚在.丁壹', '凛冬之怒.徐梓超']
a_wusui = ['钢铁长城.王文健碎片', '怒海狂涛.赵婧凯碎片', '铁塔尚在.丁壹碎片', '凛冬之怒.徐梓超碎片']
b_wu = ['友谊长存.施卓成']
san_h = ['丁壹.大剑', '丁壹重炮', '王之数据流', 'JK泳装（上）', 'JK泳装（中）', 'JK泳装（下）']
si_h = ['炮:蓝焰银隼0019', '双枪:空无之钥', '太刀:天殛之钥', '大剑:天鹅湖', '拳套:无存之钥', '镰刀:血渊之眸', '骑枪:永寂之赫勒尔',
        '冰之律者套装:安娜.沙尼亚特(上)', '冰之律者套装:安娜.沙尼亚特(中)', '冰之律者套装:安娜.沙尼亚特(下) '
        ]
qi_tq = ['三星吼里宝藏', '超小型反应炉''相转移镜面', '吼咪宝藏 ']
last_jiqngchi = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
least = 0
do_least = False
j = 0


def single2():
    global jiangchi, least, NO_S_TIMES, do_least, j
    '''if least != 0:
        a = random.randint(1, N)
        if a == 1:
            least = 0  # 触发保底机制后清除剩余的次数
        do_least = True
    else:
        least -= 1
        do_least = False'''
    least += 1
    result = None
    if NO_S_TIMES == 100:
        do_least = True
    if do_least:
        result = s_bd
        jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                    2, 2,
                    3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
                    6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8]
        do_least = False
        choices = 8
        j = NO_S_TIMES
        NO_S_TIMES = 0
        least = 0

    elif least == 10:
        choices = random.choice(bd)
        if choices == 8:
            result = random.choice(s_wu)
            j = NO_S_TIMES
            NO_S_TIMES = 0
            jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2,
                        3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
                        6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8]
            do_least = False  # 抽到s，解除保底
            least = 0

        elif choices == 6:
            result = random.choice(a_wu)
            NO_S_TIMES += 1
            least = 0

    else:
        choices = random.choice(jiangchi)
        if choices == 8:
            result = random.choice(s_wu)
            j = NO_S_TIMES
            NO_S_TIMES = 0
            jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                        2, 2,
                        3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
                        6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8]
            do_least = False  # 抽到s，解除保底

        elif choices == 7:
            result = random.choice(s_wusui)
            NO_S_TIMES += 1
            do_least = False

        elif choices == 6:
            result = random.choice(a_wu)
            NO_S_TIMES += 1

        elif choices == 5:
            result = random.choice(a_wusui)
            NO_S_TIMES += 1

        elif choices == 4:
            result = random.choice(b_wu)
            NO_S_TIMES += 1

        elif choices == 3:
            result = random.choice(si_h)
            NO_S_TIMES += 1

        elif choices == 2:
            result = random.choice(san_h)
            NO_S_TIMES += 1

        else:
            result = random.choice(qi_tq)
            NO_S_TIMES += 1

    return result, choices, NO_S_TIMES, least, j


leas = []
asq = []
for i in range(1000000):
    g = single2()
    if g[1] == 8:
        leas.append(g[1])
        asq.append(g[-1])
print(sum(asq)/leas.count(8))
