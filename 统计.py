import matplotlib.pyplot as plt
from typing import Tuple, Any, List


class 游戏统计:
    def __init__(self, 统计游戏="原神", 模型选择="频数分布直方图", 预设统计类型=None, x: list = None, y: list = None, 抽奖总次数=90):
        self.游戏 = 统计游戏
        self.模型 = 模型选择
        self.x = x
        self.y = y
        self.类型 = 预设统计类型
        self.抽奖 = len(y)

    def 凯子统计法(self, title: str = "统计图", 文字位置=1, 频数统计= None,
              对比数据: Tuple[list, list, Any, Any] = None, 保底位置=0):
        if 频数统计 is None:
            频数统计 = [False, None]
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
            self.玄哥柱状统计图法(频数统计[1], 保底位置)

        plt.show()

    def 玄哥柱状统计图法(self, xy: List[list] = None, 保底位置=90):
        if self.类型 == "原神--出金概率折线图":
            self.a1 = plt.subplot(3, 1, 3)
            list31 = [i for i in range(1, 91)]
            list32 = list([0] * 90)
            for i in xy[0]:
                if i != 0:
                    list32[i - 1] += 1
                else:
                    pass
            plt.plot(list31, list32)
            plt.text(10, 100, f"max is {list31[list32.index(max(list32))]}/st/rd/th", fontsize=15)
        else:
            self.a1 = plt.subplot(2, 1, 2)
            list31 = [i for i in range(1, 保底位置 + 1)]
            list32 = list([0] * 保底位置)
            for i in xy[0]:
                if i != 0:
                    list32[i - 1] += 1
                else:
                    pass
            plt.plot(list31, list32)
            plt.text(10, 800, f"E(x)={list31[list32.index(max(list32))]}", fontsize=15)


if __name__ == "__main__":
    print(len(list([0] * 90)))
