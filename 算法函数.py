import random as rd
import typing as ty


class 米FA游游戏抽卡:
    def __init__(self):
        pass

    @staticmethod
    def 原神抽卡(五星角色概率: float = 0.003, 四星角色概率: float = 0.025, 五星武器概率: float = 0.003, 四星武器概率: float = 0.025,
             五星武器奖池=None,
             五星角色奖池=None,
             四星角色奖池=None,
             四星武器奖池=None,
             三星奖池=None,
             第几次=1, 增加概率=600, 增加起始位置=74, 大小保底控制=False, 是否常驻池=False,
             up五星角色="荒泷一斗", up四星角色=None, up五星武器=None, up四星武器=None,
             算法选择="VC-1.2"):
        if 算法选择 == "VC-1.2":
            if up四星角色 is None:
                up四星角色 = ["久岐忍", "烟绯", "五郎"]
            if 三星奖池 is None:
                三星奖池 = ["弹弓", '神射手之誓', '鸦羽弓', '讨龙英杰谭', '黑缨枪', '沐浴龙血的剑', '飞天御剑', '冷刃', '翡玉法球', '魔导绪论', '以理服人', '铁影阔剑',
                        '黎明神剑']
            if 五星武器奖池 is None:
                五星武器奖池 = ["天空之刃", "天空之傲", "天空之翼", "天空之卷", "天空之脊", "狼的末路", "和璞鸢", "四风原典", "狼的末路", "阿莫斯之弓", "风鹰剑"]
            if 五星角色奖池 is None:
                五星角色奖池 = ["刻晴", "琴", "迪卢克", "莫娜", "迪卢克"]
            if 四星角色奖池 is None:
                四星角色奖池 = ['云堇', '托马', '早柚', '九条裟罗', '凝光', '菲谢尔', '班尼特', '丽莎', '行秋', '迪奥娜', '安柏', '重云', '雷泽', '芭芭拉',
                          '罗莎莉亚',
                          '香菱',
                          '凯亚', '北斗', '诺艾尔', '砂糖', '辛焱']
            if 四星武器奖池 is None:
                四星武器奖池 = ["弓藏", '祭礼弓', '绝弦', '西风猎弓', '祭礼残章', '西风秘典', '匣里灭辰', '祭礼大剑', '西风大剑', '祭礼剑', '西风剑', '笛剑', '匣里龙吟',
                          '钟剑',
                          '雨裁', '西风长枪', '流浪乐章', '绝弦', '昭心']
            if 是否常驻池:
                pass
            elif up五星角色 is not None and (up五星武器 is None):
                for i in range(len(五星角色奖池)):
                    五星角色奖池.append(up五星角色)
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[0])
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[1])
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[2])
            elif up五星武器 is not None and (up五星角色 is None):
                for i in range(len(五星武器奖池)):
                    五星武器奖池.append(up五星武器)
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[0])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[1])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[2])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[3])

            if 增加起始位置 <= 第几次 < 90:
                五星角色概率 += round(增加概率 / 10000, 3) * (第几次 - 增加起始位置)
            if 第几次 == 90:
                if 大小保底控制:
                    结果 = up五星角色 if up五星角色 is not None else up五星武器
                    信号 = 5
            事件 = rd.randint(1, 10000)
            if 0 <= 事件 <= int(五星角色概率 * 10000):
                if not 大小保底控制:
                    结果 = rd.choice(五星角色奖池)
                    信号 = 5
                else:
                    结果 = up五星角色
                    信号 = 5
            elif int(五星角色概率 * 10000) < 事件 <= int((五星武器概率 + 五星角色概率) * 10000):
                if not 大小保底控制:
                    结果 = rd.choice(五星武器奖池)
                    信号 = 5
                else:
                    结果 = up五星武器
                    信号 = 5
            elif int((五星武器概率 + 五星角色概率) * 10000) < 事件 <= int((五星武器概率 + 五星角色概率 + 四星角色概率) * 10000):
                结果 = rd.choice(四星角色奖池)
                信号 = 4
            elif int((五星武器概率 + 五星角色概率 + 四星角色概率) * 10000) < 事件 <= int((五星武器概率 + 五星角色概率 + 四星角色概率 + 四星武器概率) * 10000):
                结果 = rd.choice(四星武器奖池)
                信号 = 4
            elif 第几次 % 10 == 0 and 第几次 >= 10:
                事件 = rd.randint(0, int((四星角色概率 + 四星武器概率) * 10000) - 1)
                if 事件 in range(0, int(四星角色概率 * 10000)):
                    结果 = rd.choice(四星角色奖池)
                    信号 = 4
                else:
                    结果 = rd.choice(四星武器奖池)
                    信号 = 4
            else:
                结果 = rd.choice(三星奖池)
                信号 = 3
            return 结果, 信号, 五星角色概率, 算法选择

        if 算法选择 == "W-1.0":
            pass

    @staticmethod
    def 崩坏3抽卡(概率: dict = None, 相对次数: int = 0):
        xd = 0
        p = (None, None)
        xh = False
        if 概率 is None:
            概率 = {'PS': 0.015, 'PSA': 0.0127, 'PA': 0.135, 'PAA': 0.1019, 'PB': 0.055, 'P4': 0.0046, 'P4S': 0.0073,
                  'P3': 0.075, 'P3S': 0.225}
        e3 = rd.randint(1, 10000)
        # 概率['PS'] = round(0.015 + 0.985 / 62 * (相对次数 - 1), 4)
        for i in 概率.values():
            if 相对次数 == 100:
                p = (e3, "S")
                # 概率['PS'] = 0.015
                xh = True
                break
            elif e3 in range(0 + xd, xd + int(i * 10000)):
                if int(概率["PS"] * 10000) == xd + int(i * 10000):
                    p = (e3, "S")
                    概率['PS'] = 0.015
                    xh = True
                break
            else:
                xd += int(i * 10000)
        else:
            p = (e3, "黑心")
        return 相对次数, xh, p


class 明日之后抽奖:
    def __init__(self, 第几次, 抽奖类型=None):
        self.第几次 = 第几次
        self.类型 = 抽奖类型

    def 配方机抽奖(self, 概率列表: dict = None, 奖品字典索引: dict = None):
        list1 = []
        list2 = []
        纯数字概率 = []
        if self.类型 == "配方机抽奖":
            for key in 概率列表.items():
                list1.append(key)
                纯数字概率.append(key[1])
            for key2 in 奖品字典索引.items():
                list2.append(key2)
            事件_明日之后 = rd.randint(0, 9999)
            g = -1
            x = 0
            for fuck in 纯数字概率:
                if 事件_明日之后 in range(0 + g + 1, 0 + g + int(fuck * 10000) + 1):
                    sb = [事件_明日之后, 0 + g + 1, g + int(fuck * 10000)], list(概率列表.keys())[纯数字概率.index(fuck)], \
                         rd.choice(奖品字典索引[list(概率列表.keys())[纯数字概率.index(fuck)]])
                    x += 1
                g += int(fuck * 10000)

            if x == 0:
                sb = [事件_明日之后, 0, None]
        return sb


def Apex抽奖(P传家宝=0.02, P传说=0.054, P史诗=0.174, P稀有=0.752, 组合包数=1, 奖池字典: ty.Dict[str, list] = None, 次数=1, 算法选择="VC-1.0"):
    list3 = []
    list1 = []
    if 算法选择 == "VC-1.0":
        if 次数 == 500:
            list3.append(["传家宝碎片", "传家宝碎片", "传家宝碎片"])
        for k in range(组合包数):
            if k == 499:
                list3.append(["传家宝碎片", "传家宝碎片", "传家宝碎片"])
            for i in range(3):
                f1 = rd.randint(0, 999)
                if f1 in range(0, int(P传家宝 * 1000)):
                    list1.append(rd.choice(奖池字典["传家宝"]))
                elif f1 in range(int(P传家宝 * 1000), int((P传家宝 + P传说) * 1000)):
                    list1.append(rd.choice(奖池字典["传说"]))
                elif f1 in range(int((P传家宝 + P传说) * 1000), int((P传家宝 + P传说 + P史诗) * 1000)):
                    list1.append(rd.choice(奖池字典["史诗"]))
                elif f1 in range(1000 - int(P稀有 * 1000), 1000):
                    list1.append(rd.choice(奖池字典["稀有"]))

            list3.append(list1)
            list1.clear()
        return list3

    if 算法选择 == "W-1.0":
        pass


def 明日方舟抽卡(干员字典: ty.Dict[str, list], 六星干员基础概率=0.02, 五星干员基础概率=0.08, 四星干员基础概率=0.5, 三星干员基础概率=0.4,
           相对抽奖次数=1, 算法选择="VC-1.0"):
    if 算法选择 == "VC-1.0":
        list23 = 0
        if 相对抽奖次数 > 50:
            六星干员基础概率 += round(0.02 * (相对抽奖次数 - 50))
            if 六星干员基础概率 >= 1:
                print("100% to six")
        事件_找老婆 = rd.randint(0, 99)
        if 事件_找老婆 in range(0, int(六星干员基础概率 * 100)):
            list23 = rd.choice(干员字典["六星干员"])
        if 事件_找老婆 in range(int(六星干员基础概率 * 100), int((六星干员基础概率 + 五星干员基础概率) * 100)):
            list23 = rd.choice(干员字典["五星干员"])
        if 事件_找老婆 in range(int((六星干员基础概率 + 五星干员基础概率) * 100), int((六星干员基础概率 + 五星干员基础概率 + 四星干员基础概率) * 100)):
            list23 = rd.choice(干员字典["四星干员"])
        if 事件_找老婆 in range(int((1 - 三星干员基础概率) * 100), 1000):
            list23 = rd.choice(干员字典["三星干员"])
        return list23


if __name__ == "__main__":
    f = 0
    M = 0
    times = 0
    大保底次数 = 0
    for jk in range(1, 1000001):
        f += 1
        q = 米FA游游戏抽卡().崩坏3抽卡(相对次数=f)
        if q[1]:
            M += f
            times += 1
            if f == 100:
                大保底次数 += 1
            f = 0

    Ex = M / times
    print("保底率和平均出金第次:",大保底次数/100000, Ex)
