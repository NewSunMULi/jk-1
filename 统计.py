import matplotlib.pyplot as plt
from typing import Tuple, Any, List, IO
import json as js
import os


class 游戏统计:
    def __init__(self, 统计游戏="原神", 模型选择="频数分布直方图", 预设统计类型=None, x: list = None, y: list = None, 抽奖总次数=90):
        self.游戏 = 统计游戏
        self.模型 = 模型选择
        self.x = x
        self.y = y
        self.类型 = 预设统计类型
        self.抽奖 = len(y)

    def 凯子统计法(self, title: str = "统计图", 文字位置=1, 频数统计=None,
              对比数据: Tuple[list, list, Any, Any] = None, 保底位置=0):
        if 频数统计 is None:
            频数统计 = [False, None, None]
        self.fig = plt.figure(title, (15, 8))
        plt.title("001")
        if self.类型 == "原神--出金概率折线图":
            self.a1 = plt.subplot(3, 1, 1)
            plt.title("star - 4")
            x = [i for i in range(1, self.抽奖 + 1)]
            four = []
            five = []
            list1 = []
            list2 = []
            for i in range(len(self.y)):
                if self.y[i] == 3:
                    pass
                elif self.y[i] == 4:
                    four.append(1)
                else:
                    five.append(1)
                list1.append(round(len(four) / (i + 1), 4))
                list2.append(round(len(five) / (i + 1), 4))

            plt.axis([0, self.抽奖 + 1, 0, 0.6])
            plt.plot(x, list1, "red")
            if 对比数据 is not None:
                plt.plot(对比数据[0], 对比数据[1])
            self.a1 = plt.subplot(3, 1, 2)
            plt.title("star - 5")
            plt.plot(x, list2, "green")
            if 对比数据 is not None:
                plt.plot(对比数据[2], 对比数据[3])
            self.a1 = plt.subplot(3, 1, 1)
            plt.text(int(len(x) / 20), 0.45, f"P(5)={round(list2[-1] * 100, 3)}%,P(4)={round(list1[-1] * 100, 3)}%",
                     fontsize=15)

        elif self.类型 == "明日之后--物品概率对比折线图":
            self.a1 = plt.subplot(2, 1, 1)
            print("绘画中")
            plt.plot(self.x, self.y)
            if 对比数据 is not None:
                plt.plot(对比数据[0], 对比数据[1])
            print("绘画完成")
            plt.text(20, 0.03, f"P={round(self.y[-1] * 100, 4)}%", fontsize=15)

        else:
            self.a1 = plt.subplot(2, 1, 1)
            plt.plot(self.x, self.y)
            if 对比数据 is not None:
                plt.plot(对比数据[0], 对比数据[1])
            plt.text(文字位置, 1, f"P={round(self.y[-1], 4)}%", fontsize=15)
        if 频数统计[0]:
            self.玄哥柱状统计图法(频数统计[1], 频数统计[2], 保底位置)

        plt.show()

    def 玄哥柱状统计图法(self, xy1: List[list] = None, xy2=None, 保底位置=90):
        if self.类型 == "原神--出金概率折线图":
            self.a1 = plt.subplot(3, 1, 3)
            list31 = [i for i in range(1, 181)]
            list32 = list([0] * 180)
            for i in xy1[0]:
                if i != 0:
                    list32[i - 1] += 1
                else:
                    pass
            plt.plot(list31, list32)

            list34 = [i for i in range(1, 181)]
            list36 = list([0] * 180)
            for i in xy2:
                if i != 0:
                    list36[i - 1] += 1
                else:
                    pass
            plt.plot(list34, list36)
            plt.text(10, 100,
                     f"max is {list31[list32.index(max(list32))]} and {list34[list36.index(max(list36))]}/st/rd/th",
                     fontsize=15)

        else:
            self.a1 = plt.subplot(2, 1, 2)
            list31 = [i for i in range(1, 保底位置 + 1)]
            list32 = list([0] * 保底位置)
            for i in xy1[0]:
                if i != 0:
                    list32[i - 1] += 1
                else:
                    pass
            plt.plot(list31, list32)
            plt.text(10, 800, f"E(x)={list31[list32.index(max(list32))]}", fontsize=15)


class 辐射计划5_镜像计划:
    @staticmethod
    class 科别数:
        ch = 0
        mt = 1
        en = 5
        ph = 2
        ob = 3
        chs = 4

    def __init__(self, json文件对象: List = None):
        """json文件对象:你需要加载的标准json成绩分析文件名,例如a.json"""
        self.科别 = ['语文', '数学', '物理', '生物', '化学', "鸟语"]
        self.file = json文件对象
        self.color = ["green", "blue", "yellow", "red", "orange", "#EE00F0"]

    def 图表(self, 科别: int = 0, 评级等级: List = None):
        plt.figure(f"趋势统计-{self.科别[科别]}")
        plt.subplot(1, 1, 1)
        for i in self.file:
            list2 = []
            data2 = []
            for da in i:
                data2.append(f"{da[0][0:4]}-{da[0][4:6]}-{da[0][6:]}")
                list2.append(da[科别 + 1])
            plt.plot(data2, list2, label=评级等级[self.file.index(i)], color=self.color[self.file.index(i)])
            for data in i:
                plt.scatter(f"{data[0][0:4]}-{data[0][4:6]}-{data[0][6:]}", data[科别 + 1],
                            color=self.color[self.file.index(i)], s=10)
                plt.text(f"{data[0][0:4]}-{data[0][4:6]}-{data[0][6:]}", data[科别 + 1] + 0.5, str(data[科别 + 1]), size=8)

        plt.legend()
        plt.show()


class 辐射计划6_镜像计划部分:
    def __init__(self):
        pass

    def 图表(self, 统计列表: List = None, 科目: List = None, 日期列表=None):
        """
        :param 日期列表: x轴显示具体日期，必须做到len(日期列表) == len(统计列表[n, n∈N])
        :param 统计列表: 格式[[科目1成绩], [科目2成绩], ...... , [科目n的成绩]]
        :param 科目: 格式[科目1, 科目2, ...... ,科目n]，必须做到len(统计列表) == len(科目)
        :return:
        """
        plt.figure(f"S-V 3.0 统计图")
        plt.subplot(1, 1, 1)
        for i in 统计列表:
            plt.plot(日期列表, i, label=科目[统计列表.index(i)])
            plt.scatter(日期列表, i)
            for d in i:
                plt.text(日期列表[i.index(d)], d, str(d), size=8)
        plt.legend()
        plt.show()


if __name__ == "__main__":
    pass
