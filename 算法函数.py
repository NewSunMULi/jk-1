import random as rd
import typing as ty
import threading as th


class 游戏货币不足错误(Exception):
    def __init__(self, 提示="穷鬼，啥都没有抽什么卡"):
        super().__init__()
        self.error = 提示

    def __str__(self):
        return self.error


class 米FA游游戏抽卡:
    def __init__(self):
        pass

    @staticmethod
    def 原神抽卡(五星角色概率: float = 0.003, 四星角色概率: float = 0.025, 五星武器概率: float = 0.003, 四星武器概率: float = 0.025,
             五星武器奖池=None, 五星角色奖池=None, 四星角色奖池=None, 四星武器奖池=None, 三星奖池=None, 自定义奖池名字=None,
             第几次=1, 增加概率=600, 增加起始位置=74, 大小保底控制=False, 是否常驻池=False,
             up五星角色=None, up四星角色=None, up五星武器=None, up四星武器=None,
             算法选择="VC-1.4"):
        if 算法选择 == "VC-1.4":
            if 自定义奖池名字 == "原神-现代战争":
                # 原神-现代战争卡池
                up五星角色 = None
                up五星武器 = ["VOLT战机", "萝莉装赵靖凯"]
                up四星武器 = ["泳装jk", "弹簧刀典藏版", "M4轻机枪", "A2突榴枪典藏版"]
                五星角色奖池 = ["阿列克谢大叔", "谢菲尔德", "幽灵(西蒙莱利)", "坎巴拉飞行大师jeb", "大卫汉斯", "普瘦(普莱斯)"]
                五星武器奖池 = ["AMD-8导弹", "CNMD防御系统", "战斗飞斧", 'J-20/F-35战机', "A-10飞机", "X-5空对地导弹"]
                四星武器奖池 = ["M416突击步枪", "毒刺防空导弹", 'X-25突击步枪', 'AMR狙击枪', 'M4轻机枪']
                四星角色奖池 = ["小强", "肥皂", "bill", "尤里", "范利肯"]
                三星奖池 = ["m1911手枪", "jk用过的小刀", "板砖"]

            else:
                # 官方卡池
                if up四星角色 is None:
                    up四星角色 = ["久岐忍", "烟绯", "五郎"]
                if 三星奖池 is None:
                    三星奖池 = ["弹弓", '神射手之誓', '鸦羽弓', '讨龙英杰谭', '黑缨枪', '沐浴龙血的剑', '飞天御剑', '冷刃', '翡玉法球', '魔导绪论', '以理服人',
                            '铁影阔剑',
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
                    四星武器奖池 = ["弓藏", '祭礼弓', '绝弦', '西风猎弓', '祭礼残章', '西风秘典', '匣里灭辰', '祭礼大剑', '西风大剑', '祭礼剑', '西风剑', '笛剑',
                              '匣里龙吟',
                              '钟剑',
                              '雨裁', '西风长枪', '流浪乐章', '绝弦', '昭心']
            if 是否常驻池:
                pass
            elif up五星角色 is not None and (up五星武器 is None):
                五星角色概率 += 五星角色概率
                五星武器概率 = 0
                四星角色概率 += 四星角色概率
                四星武器概率 = 0
                for i in range(len(五星角色奖池)):
                    五星角色奖池.append(up五星角色)
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[0])
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[1])
                for i in range(int(len(四星角色奖池) / 3)):
                    四星角色奖池.append(up四星角色[2])
            elif up五星武器 is not None and (up五星角色 is None):
                五星武器概率 += 五星武器概率
                五星角色概率 = 0
                四星角色概率 = 0
                四星武器概率 += 四星武器概率
                for i in range(int(len(五星武器奖池) / 2)):
                    五星武器奖池.append(up五星武器[0])
                for i in range(int(len(五星武器奖池) / 2)):
                    五星武器奖池.append(up五星武器[1])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[0])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[1])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[2])
                for i in range(int(len(四星武器奖池) / 4)):
                    四星武器奖池.append(up四星武器[3])

            if 增加起始位置 <= 第几次 < 90:
                if 五星角色概率 != 0 and 五星武器概率 == 0:
                    五星角色概率 += round(round(增加概率 / 10000, 3) * (第几次 - 增加起始位置 + 1), 3)
                elif 五星武器概率 != 0 and 五星角色概率 == 0:
                    五星武器概率 += round(round(增加概率 / 10000, 3) * (第几次 - 增加起始位置 + 1), 3)
                else:
                    五星角色概率 += round(round(增加概率 / 2 / 10000, 3) * (第几次 - 增加起始位置 + 1), 3)
                    五星武器概率 += round(round(增加概率 / 2 / 10000, 3) * (第几次 - 增加起始位置 + 1), 3)
            if 第几次 == 90:
                if 大小保底控制:
                    结果 = up五星角色 if up五星角色 is not None else up五星武器
                    信号 = 5
            事件 = rd.randint(1, 10000)
            if 0 <= 事件 <= int(五星角色概率 * 10000) and up五星角色 is not None:
                if not 大小保底控制:
                    结果 = rd.choice(五星角色奖池)
                    信号 = 5
                else:
                    结果 = up五星角色
                    信号 = 5
            elif int(五星角色概率 * 10000) < 事件 <= int((五星武器概率 + 五星角色概率) * 10000) and up五星武器 is not None:
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
            return 结果, 信号, 五星角色概率, 算法选择, 五星武器概率, 四星武器概率, 四星角色概率

        if 算法选择 == "W-1.0":
            pass

    @staticmethod
    def 崩坏3抽卡(概率: dict = None, 相对次数: int = 0, 算法选择="VC-1.3", 卡池类型="家园补给", 奖池=None):
        if 算法选择 == "VC-1.3":
            xd = 0
            p = (None, None)
            xh = False
            if 概率 is None and 奖池 is None:
                if 卡池类型 == "家园补给":
                    # 家园补给
                    概率 = {'PS': 0.015, 'PSA': 0.0127, 'PA': 0.135, 'PAA': 0.1019, 'PB': 0.055, 'P4': 0.0046,
                          'P4S': 0.0073, 'P3': 0.075, 'P3S': 0.225}
                    奖池 = {'S': ["S"], 'A': ["A"], 'B': ["B"], '4': ["4"], '4S': ['4S'], '3': ['3'], '3S': ['3S'],
                          "else": ["你干嘛，哎嗨哟"],
                          "SA": ["SA"],
                          "AA": ["AA"]}
                elif 卡池类型 == "扩充补给":
                    # 扩充补给
                    概率 = {'PS': 0.015, 'PA1': 0.045, 'PA2': 0.03, 'PA3': 0.03, 'PA4': 0.03}
                    奖池 = {'S': ['S'], 'A1': ['A1'], 'A2': ['A2'], 'A3': ['A3'], 'A4': ['A4'], 'else': ["吉你抬煤"]}
            e3 = rd.randint(0, 9999)
            m = 0
            for i in 概率.values():
                if 相对次数 == 100:
                    xh = True
                if e3 in range(0 + xd, xd + int(i * 10000)):
                    if int(概率["PS"] * 10000) + xd == xd + int(i * 10000):
                        xh = True
                        p = (e3, "S")
                    else:
                        p = (e3, 奖池[list(概率.keys())[m][1:]][0])
                    break
                else:
                    xd += int(i * 10000)
                    m += 1
            else:
                p = (e3, "只因")
            return 相对次数, xh, p

        elif 算法选择 == "W-1.0":
            NO_S_TIMES = 0
            # 8=s级女武神7=s级碎片6=A武神5=A武神碎片4=B武神/3=四星武器加圣痕2=三星武器加圣痕/1=其他材料
            jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1,
                        1,
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
            '''if least != 0:
                a = rd.randint(1, N)
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
                jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1,
                            1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                            2,
                            2, 2,
                            3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
                            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8]
                do_least = False
                choices = 8
                j = NO_S_TIMES
                NO_S_TIMES = 0
                least = 0

            elif least == 10:
                choices = rd.choice(bd)
                if choices == 8:
                    result = rd.choice(s_wu)
                    j = NO_S_TIMES
                    NO_S_TIMES = 0
                    jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1,
                                1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                2, 2, 2,
                                2, 2,
                                3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
                                6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8]
                    do_least = False  # 抽到s，解除保底
                    least = 0

                elif choices == 6:
                    result = rd.choice(a_wu)
                    NO_S_TIMES += 1
                    least = 0

            else:
                choices = rd.choice(jiangchi)
                if choices == 8:
                    result = rd.choice(s_wu)
                    j = NO_S_TIMES
                    NO_S_TIMES = 0
                    jiangchi = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                1, 1, 1,
                                1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                                2, 2, 2,
                                2, 2,
                                3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6,
                                6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8]
                    do_least = False  # 抽到s，解除保底

                elif choices == 7:
                    result = rd.choice(s_wusui)
                    NO_S_TIMES += 1
                    do_least = False

                elif choices == 6:
                    result = rd.choice(a_wu)
                    NO_S_TIMES += 1

                elif choices == 5:
                    result = rd.choice(a_wusui)
                    NO_S_TIMES += 1

                elif choices == 4:
                    result = rd.choice(b_wu)
                    NO_S_TIMES += 1

                elif choices == 3:
                    result = rd.choice(si_h)
                    NO_S_TIMES += 1

                elif choices == 2:
                    result = rd.choice(san_h)
                    NO_S_TIMES += 1

                else:
                    result = rd.choice(qi_tq)
                    NO_S_TIMES += 1

            return result, choices, NO_S_TIMES, least, j


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
    list1 = []
    pp = False
    if 算法选择 == "VC-1.0":
        if 次数 == 500:
            list1.append(["传家宝碎片", "传家宝碎片", "传家宝碎片"])
            pp = True
        else:
            for i in range(3):
                f1 = rd.randint(0, 999)
                if f1 in range(0, int(P传家宝 * 1000)):
                    list1.append(5)
                elif f1 in range(int(P传家宝 * 1000), int((P传家宝 + P传说) * 1000)):
                    list1.append(4)
                elif f1 in range(int((P传家宝 + P传说) * 1000), int((P传家宝 + P传说 + P史诗) * 1000)):
                    list1.append(3)
                elif f1 in range(1000 - int(P稀有 * 1000), 1000):
                    list1.append(2)
                else:
                    list1.append(1)
            pp = False

        return list1, pp

    if 算法选择 == "W-1.0":
        pass


class 明日方舟抽卡:
    def __init__(self, 干员字典: ty.Dict[str, list] = None, 相对抽奖次数=1, 算法选择="VC-1.0"):
        self.times = 相对抽奖次数
        self.way = 算法选择
        self.dict = 干员字典
        test = {
            'description': '无',
            'six_up': ['Aup', 0],
            'five_up': ['Bup', 0],
            'six_stars': ['A1', 'A2', 'A3'],
            'five_stars': ['B1', 'B2', 'B3'],
            'four_stars': ['C1', 'C2', 'C3', 'C4'],
            'three_stars': ['D1', 'D2', 'D3', 'D4', 'D5'],
        }
        # 池子
        test2 = {
            'description': '这个池子没有up！',
            'six_up': [0],
            'five_up': [0],
            'six_stars': ['能天使', '黑', '安洁莉娜', '银灰', '莫斯提马', '夜莺', '星熊', '陈',
                          '阿', '煌', '麦哲伦', '赫拉格', '斯卡蒂', '塞雷娅', '闪灵', '艾雅法拉', '伊芙利特',
                          '推进之王', '刻俄柏', '风笛', '傀影', '温蒂', '早露', '铃兰', '棘刺', '森蚺',
                          '史尔特尔', '瑕光', '泥岩', '山', '空弦', '嵯峨', '异客', '凯尔希', '夕', '年',
                          'W', '迷迭香', '浊心斯卡蒂'],
            'five_stars': ['狮蝎', '食铁兽', '蓝毒', '拉普兰德', '幽灵鲨', '德克萨斯', '槐琥',
                           '赫默', '红', '白面鸮', '空', '吽', '灰喉', '布洛卡', '苇草', '送葬人', '星极',
                           '格劳克斯', '诗怀雅', '夜魔', '真理', '初雪', '崖心', '守林人', '普罗旺斯', '可颂',
                           '雷蛇', '临光', '华法琳', '梅尔', '天火', '陨星', '白金', '芙兰卡', '凛冬', '惊蛰',
                           '慑砂', '巫恋', '极境', '石棉', '月禾', '莱恩哈特', '断崖', '蜜蜡', '贾维', '安哲拉',
                           '燧石', '四月', '奥斯塔', '絮雨', '卡夫卡', '爱丽丝', '乌有', '熔泉', '赤冬'],
            'four_stars': ['安比尔', '梅', '红云', '桃金娘', '苏苏洛', '格雷伊', '猎蜂', '阿消',
                           '地灵', '深海色', '古米', '蛇屠箱', '角峰', '调香师', '末药', '暗索', '砾', '慕斯',
                           '霜叶', '缠丸', '杜宾', '红豆', '清道夫', '白雪', '流星', '杰西卡', '远山', '夜烟',
                           '宴', '刻刀', '波登可', '卡达', '孑', '酸糖', '芳汀', '泡泡', '杰克', '松果', '豆苗'],
            'three_stars': ['芬', '炎熔', '月见夜', '香草', '史都华德', '卡缇', '米格鲁', '斑点',
                            '空爆', '梓兰', '芙蓉', '克洛丝', '玫兰莎', '翎羽', '泡普卡', '安赛尔'],
        }
        # '浊心斯卡蒂'和'凯尔希'占六星出率的70%，'W'在剩余出率中以5倍权值出率提升
        #  '赤冬'占五星出率的50%
        self.shengdao = {
            'description': "'浊心斯卡蒂'和'凯尔希'占六星出率的70%，" +
                           "'W'在剩余出率中以5倍权值出率提升;\n" +
                           "'赤冬'占五星出率的50%",
            'six_up': ['浊心斯卡蒂', '凯尔希', '浊心斯卡蒂', '凯尔希', '浊心斯卡蒂', '凯尔希',
                       '浊心斯卡蒂', '凯尔希', '浊心斯卡蒂', '凯尔希', '浊心斯卡蒂', '凯尔希',
                       '浊心斯卡蒂', '凯尔希',
                       0, 0, 0, 0, 0, 0],
            'five_up': ['赤冬', 0],
            'six_stars': ['能天使', '推进之王', '伊芙利特', '艾雅法拉', '安洁莉娜', '闪灵',
                          '夜莺', '星熊', '塞雷娅', '银灰', '斯卡蒂', '陈', '黑', '赫拉格', '麦哲伦',
                          '莫斯提马', '煌', '阿', '刻俄柏', '风笛', '傀影', '温蒂', '早露', '铃兰', '棘刺',
                          '森蚺', '史尔特尔', '瑕光', '泥岩', '山', '空弦', '嵯峨', '异客',
                          'W', 'W', 'W', 'W', 'W'],
            'five_stars': ['白面鸮', '凛冬', '德克萨斯', '芙兰卡', '拉普兰德', '幽灵鲨', '蓝毒',
                           '白金', '陨星', '天火', '梅尔', '赫默', '华法琳', '临光', '红', '雷蛇', '可颂',
                           '普罗旺斯', '守林人', '崖心', '初雪', '真理', '空', '狮竭', '食铁兽', '夜魔',
                           '诗怀雅', '格劳克斯', '星极', '送葬人', '槐琥', '苇草', '布洛卡', '灰喉', '吽',
                           '惊蛰', '慑砂', '巫恋', '极境', '石棉', '月禾', '莱恩哈特', '断崖', '蜜蜡', '贾维',
                           '安哲拉', '燧石', '四月', '奥斯塔', '絮雨', '卡夫卡', '爱丽丝', '乌有', '熔泉'],
            'four_stars': ['夜烟', '远山', '杰西卡', '流星', '白雪', '清道夫', '红豆', '杜宾',
                           '缠丸', '霜叶', '慕斯', '砾', '暗索', '末药', '调香师', '角峰', '蛇屠箱', '古米',
                           '深海色', '地灵', '阿消', '猎蜂', '格雷伊', '苏苏洛', '桃金娘', '红云', '梅',
                           '安比尔', '宴', '刻刀', '波登可', '卡达', '孑', '酸糖', '芳汀', '泡泡', '杰克',
                           '松果', '豆苗'],
            'three_stars': ['芬', '香草', '翎羽', '玫兰莎', '卡缇', '米格鲁', '克洛丝', '炎熔',
                            '芙蓉', '安赛尔', '史都华德', '梓兰', '空爆', '月见夜', '班点', '泡普卡'],
        }
        self.啊和森蚺卡池 = {
            'description': "'阿'和'森蚺'占六星出率的50%;\n" +
                           "'白面鸮'、'蓝毒'和'真理'占五星出率的50%",
            'six_up': ['阿', '森蚺', 0, 0],
            'five_up': ['白面鸮', '蓝毒', '真理', 0, 0, 0],
            'six_stars': ['能天使', '黑', '安洁莉娜', '银灰', '莫斯提马', '夜莺', '星熊', '陈',
                          '阿', '煌', '麦哲伦', '赫拉格', '斯卡蒂', '塞雷娅', '闪灵', '艾雅法拉', '伊芙利特',
                          '推进之王', '刻俄柏', '风笛', '傀影', '温蒂', '早露', '铃兰', '棘刺', '森蚺',
                          '史尔特尔', '瑕光', '泥岩', '山', '空弦', '嵯峨', '异客', '凯尔希'],
            'five_stars': ['狮蝎', '食铁兽', '蓝毒', '拉普兰德', '幽灵鲨', '德克萨斯', '槐琥',
                           '赫默', '红', '白面鸮', '空', '吽', '灰喉', '布洛卡', '苇草', '送葬人', '星极',
                           '格劳克斯', '诗怀雅', '夜魔', '真理', '初雪', '崖心', '守林人', '普罗旺斯', '可颂',
                           '雷蛇', '临光', '华法琳', '梅尔', '天火', '陨星', '白金', '芙兰卡', '凛冬', '惊蛰',
                           '慑砂', '巫恋', '极境', '石棉', '月禾', '莱恩哈特', '断崖', '蜜蜡', '贾维', '安哲拉',
                           '燧石', '四月', '奥斯塔', '絮雨', '卡夫卡', '爱丽丝', '乌有', '熔泉', '赤冬'],
            'four_stars': ['安比尔', '梅', '红云', '桃金娘', '苏苏洛', '格雷伊', '猎蜂', '阿消',
                           '地灵', '深海色', '古米', '蛇屠箱', '角峰', '调香师', '末药', '暗索', '砾', '慕斯',
                           '霜叶', '缠丸', '杜宾', '红豆', '清道夫', '白雪', '流星', '杰西卡', '远山', '夜烟',
                           '宴', '刻刀', '波登可', '卡达', '孑', '酸糖', '芳汀', '泡泡', '杰克', '松果', '豆苗'],
            'three_stars': ['芬', '炎熔', '月见夜', '香草', '史都华德', '卡缇', '米格鲁', '斑点',
                            '空爆', '梓兰', '芙蓉', '克洛丝', '玫兰莎', '翎羽', '泡普卡', '安赛尔'],
        }
        self.联合行动 = {
            'description': '特选干员定向寻访',
            'six_up': [0],
            'five_up': [0],
            'six_stars': ['夜莺', '温蒂', '铃兰', '棘刺'],
            'five_stars': ['芙兰卡', '赫默', '临光', '极境', '莱恩哈特', '安哲拉'],
            'four_stars': ['安比尔', '梅', '红云', '桃金娘', '苏苏洛', '格雷伊', '猎蜂', '阿消',
                           '地灵', '深海色', '古米', '蛇屠箱', '角峰', '调香师', '末药', '暗索', '砾', '慕斯',
                           '霜叶', '缠丸', '杜宾', '红豆', '清道夫', '白雪', '流星', '杰西卡', '远山', '夜烟',
                           '宴', '刻刀', '波登可', '卡达', '孑', '酸糖', '芳汀', '泡泡', '杰克', '松果', '豆苗'],
            'three_stars': ['芬', '炎熔', '月见夜', '香草', '史都华德', '卡缇', '米格鲁', '斑点',
                            '空爆', '梓兰', '芙蓉', '克洛丝', '玫兰莎', '翎羽', '泡普卡', '安赛尔'],
        }
        self.艾雅法拉和史尔特尔 = {
            'description': "'艾雅法拉'和'史尔特尔'占六星出率的50%;\n" +
                           "'凛冬'、'槐琥'和'华法琳'占五星出率的50%",
            'six_up': ['艾雅法拉', '史尔特尔', 0, 0],
            'five_up': ['凛冬', '槐琥', '华法琳', 0, 0, 0],
            'six_stars': ['能天使', '黑', '安洁莉娜', '银灰', '莫斯提马', '夜莺', '星熊', '陈',
                          '阿', '煌', '麦哲伦', '赫拉格', '斯卡蒂', '塞雷娅', '闪灵', '艾雅法拉', '伊芙利特',
                          '推进之王', '刻俄柏', '风笛', '傀影', '温蒂', '早露', '铃兰', '棘刺', '森蚺',
                          '史尔特尔', '瑕光', '泥岩', '山', '空弦', '嵯峨', '异客', '凯尔希'],
            'five_stars': ['狮蝎', '食铁兽', '蓝毒', '拉普兰德', '幽灵鲨', '德克萨斯', '槐琥',
                           '赫默', '红', '白面鸮', '空', '吽', '灰喉', '布洛卡', '苇草', '送葬人', '星极',
                           '格劳克斯', '诗怀雅', '夜魔', '真理', '初雪', '崖心', '守林人', '普罗旺斯', '可颂',
                           '雷蛇', '临光', '华法琳', '梅尔', '天火', '陨星', '白金', '芙兰卡', '凛冬', '惊蛰',
                           '慑砂', '巫恋', '极境', '石棉', '月禾', '莱恩哈特', '断崖', '蜜蜡', '贾维', '安哲拉',
                           '燧石', '四月', '奥斯塔', '絮雨', '卡夫卡', '爱丽丝', '乌有', '熔泉', '赤冬'],
            'four_stars': ['安比尔', '梅', '红云', '桃金娘', '苏苏洛', '格雷伊', '猎蜂', '阿消',
                           '地灵', '深海色', '古米', '蛇屠箱', '角峰', '调香师', '末药', '暗索', '砾', '慕斯',
                           '霜叶', '缠丸', '杜宾', '红豆', '清道夫', '白雪', '流星', '杰西卡', '远山', '夜烟',
                           '宴', '刻刀', '波登可', '卡达', '孑', '酸糖', '芳汀', '泡泡', '杰克', '松果', '豆苗'],
            'three_stars': ['芬', '炎熔', '月见夜', '香草', '史都华德', '卡缇', '米格鲁', '斑点',
                            '空爆', '梓兰', '芙蓉', '克洛丝', '玫兰莎', '翎羽', '泡普卡', '安赛尔'],
        }

    def VC算法(self, 六星干员基础概率=0.02, 五星干员基础概率=0.08, 四星干员基础概率=0.5):
        if self.way == "VC-1.0":
            list23 = 0
            t = False
            if self.times > 50:
                六星干员基础概率 += round(0.02 * (self.times - 50), 2)
            else:
                pass

            if 六星干员基础概率 >= 1:
                list23 = 6
                t = True
            else:
                事件_找老婆 = rd.randint(0, 99)
                if 事件_找老婆 in range(0, int(六星干员基础概率 * 100)):
                    # list23 = rd.choice(干员字典["六星干员"])
                    list23 = 6
                    t = True
                elif 事件_找老婆 in range(int(六星干员基础概率 * 100), int((六星干员基础概率 + 五星干员基础概率) * 100)):
                    # list23 = rd.choice(干员字典["五星干员"])
                    list23 = 5
                elif 事件_找老婆 in range(int((六星干员基础概率 + 五星干员基础概率) * 100), int((六星干员基础概率 + 五星干员基础概率 + 四星干员基础概率) * 100)):
                    # list23 = rd.choice(干员字典["四星干员"])
                    list23 = 4
                else:
                    # list23 = rd.choice(干员字典["三星干员"])
                    list23 = 3
            return list23, t
        else:
            return "算法和函数不匹配!"

    def W算法(self, 初始源石数=0, 初始合成玉数=0, 共计抽奖次数=1, 卡池名字="女装赵JK系列卡池"):
        if self.way == "W-1.1":
            卡池字典 = eval(f"self.{卡池名字}")
            while True:
                if 初始合成玉数 >= 600 * 共计抽奖次数:  # 判断合成玉
                    初始合成玉数 -= 600 * 共计抽奖次数
                    break
                else:
                    if 初始源石数 >= 1 * 共计抽奖次数:
                        初始源石数 -= 共计抽奖次数
                        初始合成玉数 += 180 * 共计抽奖次数
                    else:  # 源石不足
                        raise 游戏货币不足错误("啥都没有抽什么卡,滚蛋!")
            """判断抽卡结果(抽卡过程)"""
            # 将六星和五星分别整理到一个集合中,以便展示结果时使用
            show_list = []
            list_six = []
            list_five = []
            list_four = []
            list_three = []
            频率 = []
            保底 = False
            six_up_result = set(卡池字典['six_up'])
            six_up_result.remove(0)
            five_up_result = set(卡池字典['five_up'])
            five_up_result.remove(0)
            six_stars_result = set(卡池字典['six_stars']) | six_up_result
            five_stars_result = set(卡池字典['five_stars']) | five_up_result
            result = []  # 储存抽卡结果
            six, five, four, three = 0, 0, 0, 0  # 用于判断各个星级出现的总数
            counter1 = 1  # 六星保底或许用得到
            counter2 = 0  # 五星保底用这个也可以
            n = 0  # 用于判断保底次数
            for jk in range(共计抽奖次数):
                n += 1
                if n <= 50:
                    num = 50
                else:
                    num = n  # 判断抽卡次数
                counter2 += 1  # 判断五星保底
                if counter2 == 10 and n in range(10,100,10):
                    b = rd.randint(1, 1000)
                    if 1 <= b <= 167 + (num - 50) * 20:
                        a89 = 卡池字典['six_up'][rd.randint(0, len(卡池字典['six_up'])) - 1]
                        if a89 != 0:
                            保底 = False
                        else:
                            if 保底:
                                while a89 == 0:
                                    a89 = 卡池字典['six_up'][rd.randint(0, len(卡池字典['six_up'])) - 1]
                                保底 = False
                            else:
                                a89 = 卡池字典['six_stars'][rd.randint(0, len(卡池字典['six_stars'])) - 1]
                                保底 = True
                        result.append(a89)
                        six += 1
                        频率.append(n)
                        n = 0
                    else:
                        a89 = 卡池字典['five_up'][rd.randint(0, len(卡池字典['five_up'])) - 1]
                        if a89 != 0:
                            result.append(a89)
                        else:
                            a89 = 卡池字典['five_stars'][rd.randint(0, len(卡池字典['five_stars'])) - 1]
                            result.append(a89)
                        five += 1
                        频率.append(0)
                    counter2 = 0
                else:
                    b = rd.randint(1, 1000)
                    if 114 <= b <= 134 + (num - 50) * 20:  # 六星
                        a89 = 卡池字典['six_up'][rd.randint(0, len(卡池字典['six_up'])) - 1]
                        if a89 != 0:
                            保底 = False
                        else:
                            if 保底:
                                while a89 == 0:
                                    a89 = 卡池字典['six_up'][rd.randint(0, len(卡池字典['six_up'])) - 1]
                                保底 = False
                            else:
                                a89 = 卡池字典['six_stars'][rd.randint(0, len(卡池字典['six_stars'])) - 1]
                                保底 = True
                        result.append(a89)
                        six += 1
                        频率.append(n)
                        n = 0  # 重置抽卡次数
                    elif 921 <= b <= 1000:  # 五星
                        a89 = 卡池字典['five_up'][rd.randint(0, len(卡池字典['five_up'])) - 1]
                        if a89 != 0:
                            result.append(a89)
                        else:
                            a89 = 卡池字典['five_stars'][rd.randint(0, len(卡池字典['five_stars'])) - 1]
                            result.append(a89)
                        five += 1
                        频率.append(0)
                    elif 421 <= b <= 920:  # 四星
                        a89 = 卡池字典['four_stars'][rd.randint(0, len(卡池字典['four_stars'])) - 1]
                        four += 1
                        result.append(a89)
                        频率.append(0)
                    else:  # 三星
                        a89 = 卡池字典['three_stars'][rd.randint(0, len(卡池字典['three_stars'])) - 1]
                        three += 1
                        result.append(a89)
                        频率.append(0)

            for i in six_stars_result:
                if i in result:  # 判断抽卡结果
                    list_six.append(f"{i}:{(result.count(i))}")
            list_six.append(f"总数:{six}")
            show_list.append({"六星": list_six})

            for i in five_stars_result:
                if i in result:  # 判断抽卡结果
                    list_five.append(f"{i}:{(result.count(i))}")
            list_six.append(f"总数:{five}")
            show_list.append({"五星": list_five})

            for i in 卡池字典['four_stars']:
                if i in result:  # 判断抽卡结果
                    list_four.append(f"{i}:{(result.count(i))}")
            list_four.append(f"总数:{four}")
            show_list.append({"四星": list_four})

            for i in 卡池字典['three_stars']:
                if i in result:  # 判断抽卡结果
                    list_three.append(f"{i}:{(result.count(i))}")
            list_three.append(f"总数:{three}")
            show_list.append({"三星": list_three})

            # 打印总览
            show_list.append({'货币消耗': f"共消耗价值{len(result) * 600}合成玉！"})
            try:
                luck = six / len(result) * 100
            except ZeroDivisionError:
                luck = 0.000
            show_list.append({'六星概率': f"六星出货占比：{'百分之%.3f' % luck}"})
            if float(luck) > 3:
                show_list.append({'感悟': "献祭jk,出双金，哈哈哈哈"})

            show_list.append({"卡池信息": (six_up_result, six_stars_result, five_up_result, five_stars_result)})
            show_list.append({"频率": 频率})
            show_list.append({'统计API': result})
            return show_list
        else:
            return "算法和函数不匹配!"


if __name__ == "__main__":
    l1 = []
    l2 = []


    def 抽卡(ma=10000000):
        g = 0
        for ii in range(1, ma + 1, 1):
            g += 1
            a = 米FA游游戏抽卡().崩坏3抽卡(相对次数=g)
            if a[1]:
                l2.append(g)
                g = 0
            l1.append(a[2][1])
            print(ii)


    抽卡()
    print(f"E(x)={sum(l2) / l1.count('S')}")
