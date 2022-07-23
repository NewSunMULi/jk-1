import matplotlib.pyplot as plt


class 游戏统计:
    def __init__(self, 统计游戏="原神", 模型选择="频数分布直方图", 预设统计类型=None, x: list = None, y: list = None, 抽奖总次数=90):
        self.游戏 = 统计游戏
        self.模型 = 模型选择
        self.x = x
        self.y = y
        self.类型 = 预设统计类型
        self.抽奖 = len(y)

    def 凯子统计法(self, title: str = "统计图"):
        fig = plt.figure(title, (10, 6))
        plt.title("001")
        if self.类型 == "原神--出金概率折线图":
            a1 = plt.subplot(2, 1, 1)
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
            a1 = plt.subplot(2, 1, 2)
            plt.title("star - 5")
            plt.plot(x, list2, "green")
            a1 = plt.subplot(2, 1, 1)
            plt.text(int(len(x) / 20), 0.45, f"P(5)={list2[-1]},P(4)={list1[-1]}", fontsize=15)

        if self.类型 == "明日之后--物品概率对比折线图":
            a1 = plt.subplot(1, 1, 1)
            print("绘画中")
            plt.plot(self.x,self.y)
            print("绘画完成")

        plt.show()


if __name__ == "__main__":
    游戏统计(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         y=[3, 3, 3, 5, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
            3, 3, 3],
         预设统计类型="原神--出金频数分布图").凯子统计法()
