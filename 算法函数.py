import random as rd


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
            global 结果
            if 是否常驻池:
                pass
            else:
                for i in range(len(五星角色奖池)):
                    五星角色奖池.append(up五星角色)
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[0])
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[1])
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[2])

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
    def 崩坏3抽卡():
        pass


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
                if 事件_明日之后 in range(0 + g + 1, 0 + g + int(fuck * 10000)+1):
                    sb = [事件_明日之后, 0 + g + 1, g + int(fuck * 10000)], list(概率列表.keys())[纯数字概率.index(fuck)],\
                         rd.choice(奖品字典索引[list(概率列表.keys())[纯数字概率.index(fuck)]])
                    x += 1
                g += int(fuck * 10000)

            if x == 0:
                sb = [事件_明日之后, 0, None]
        return sb


if __name__ == "__main__":
    i = 0
    f = 0
    a = 明日之后抽奖(1, "配方机抽奖")
    for i in range(1):
        g = a.配方机抽奖({"赵靖凯": 0.9, "陈老二": 0.095, "余老三": 0.005},
                    {"赵靖凯": ["寄吧", "nb"], "陈老二": ["sda", "sb", "sdadf"], "余老三": ["sdasada", "sdasdb", "sdadf"]})
        if g[2] is None:
            print(g[2])
