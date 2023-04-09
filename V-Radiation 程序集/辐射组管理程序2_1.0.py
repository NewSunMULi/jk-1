from typing import Optional, List

from 辐射组管理程序2ui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
import sys
import data_update as du
import sv_file as sv
import json as js
import datetime
from 统计 import 辐射计划6_镜像计划部分


class V_Rt2(QtWidgets.QWidget, Ui_app):
    sv_all: object
    sv_q: List[Optional[List[str]]]

    def __init__(self):
        self.Signing = False
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("辐射组管理程序2")
        icon1 = QtGui.QIcon('../logo.ico')
        self.setWindowIcon(icon1)
        self.plan_data = [self.label_16, self.label_17, self.label_18, self.label_20, self.label_21, self.label_22]
        self.subject = ["语文", "数学", "英语", "物理", "生物", "化学"]
        self.subject_en = ["ch", "mt", "en", "ph", "ob", "chs"]
        self.bar = [[self.progressBar, self.progressBar_4], [self.progressBar_2, self.progressBar_5],
                    [self.progressBar_3, self.progressBar_6], [self.progressBar_7, self.progressBar_8],
                    [self.progressBar_9, self.progressBar_10], [self.progressBar_11, self.progressBar_12]]
        self.optionsShow = [self.label_69, self.label_70, self.comboBox_3, self.comboBox_4, self.comboBox_5]
        self.sv_check = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                         self.checkBox_6]
        with open("./setting/options.json", "r", encoding="utf-8") as f:
            self.options = js.load(f)
        self.update_plan()
        self.settings()
        self.svUpdate()
        self.Plan.hide()
        self.Game.hide()
        self.Data.hide()
        self.FrApp.hide()
        self.SV.hide()
        self.SignUp.hide()
        self.label_3.setText("今天是 %s年%s月%s日" % (
            datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
        self.LogUp.hide()
        self.Setting.hide()
        self.pushButton_16.clicked.connect(self.setting)
        self.pushButton_13.clicked.connect(self.Sign_Up)
        self.Backward_6.clicked.connect(self.ToHome)
        self.Backward_8.clicked.connect(self.save)
        self.verticalScrollBar.valueChanged.connect(self.change_position)
        self.commandLinkButton_2.clicked.connect(self.update_plan)
        self.Backward_8.clicked.connect(self.saveSetting)
        self.pushButton_24.clicked.connect(self.change_backgroundImage)
        self.pushButton_14.clicked.connect(self.sv_image)

    def Sign_Up(self):
        self.hide_all()
        self.VIP.hide()
        self.label_8.hide()
        self.label_3.hide()
        self.Home.hide()
        self.SignUp.show()

    def ToHome(self):
        self.VIP.show()
        self.label_8.show()
        self.label_3.show()
        self.Home.show()
        self.SignUp.hide()

    def changePictor(self):
        filename = QFileDialog.getOpenFileName()
        self.label.setPixmap(filename)

    def setting(self):
        self.Home.hide()
        self.Setting.show()
        self.VIP.hide()
        self.label_8.hide()
        self.label_3.hide()

    def save(self):
        self.VIP.show()
        self.label_8.show()
        self.label_3.show()

    def change_position(self):
        self.widget_2.move(80, 33 - self.verticalScrollBar.value())

    def hide_all(self):
        self.Plan.hide()
        self.Game.hide()
        self.Data.hide()
        self.FrApp.hide()
        self.SV.hide()

    def update_plan(self):
        dp = du.Data_Update().plan(way=self.options[2])
        for i in range(len(self.plan_data)):
            self.plan_data[i].setText(f"{self.subject[i]}:{dp[0][i]}/{dp[1][i]}/{dp[2][i]}")
            for j in range(len(self.bar[i])):
                if int(dp[0][i]) / self.bar[i][j].maximum() < 0.65:
                    self.bar[i][j].setStyleSheet(
                        "QProgressBar::chunk{background-color:red; border-radius: 10px;} QProgressBar{text-align:center; border-radius: 10px;}")
                else:
                    self.bar[i][j].setStyleSheet(
                        "QProgressBar::chunk{background-color:green; border-radius: 10px;} QProgressBar{text-align:center; border-radius: 10px;}")
                self.bar[i][j].setValue(int(dp[0][i]))

    def svUpdate(self):
        sv_data = sv.SV_File("./sv30/data2.sv")
        self.sv_q = [sv_data.getData("ch"), sv_data.getData("mt"), sv_data.getData("en"), sv_data.getData("ph"),
                     sv_data.getData("ob"), sv_data.getData("chs"), sv_data.getData("date")]
        self.sv_all = sv_data.getAllScore()
        data_all = sv_data.getData("ch")[-1] + sv_data.getData("mt")[-1] + sv_data.getData("en")[-1] + \
                   sv_data.getData("ph")[-1] + sv_data.getData("ob")[-1] + sv_data.getData("chs")[-1]
        data_all_before = sv_data.getData("ch")[-2] + sv_data.getData("mt")[-2] + sv_data.getData("en")[-2] + \
                          sv_data.getData("ph")[-2] \
                          + sv_data.getData("ob")[-2] + sv_data.getData("chs")[-2]
        cha = data_all - data_all_before
        major = [sv_data.getData("ch")[-1] + sv_data.getData("mt")[-1] + sv_data.getData("en")[-1],
                 sv_data.getData("ch")[-2] + sv_data.getData("mt")[-2] + sv_data.getData("en")[-2]]
        science = [sv_data.getData("ph")[-1] + sv_data.getData("ob")[-1] + sv_data.getData("chs")[-1],
                   sv_data.getData("ph")[-2] + sv_data.getData("ob")[-2] + sv_data.getData("chs")[-2]]
        cha_m = major[0] - major[1]
        cha_s = science[0] - science[1]
        self.label_33.setText(f"自己总分:{data_all}")
        self.label_36.setText(f"相较上一次变化:{cha}")
        self.label_37.setText(f"主三科总分:{major[0]}({cha_m})")
        self.label_49.setText(f"理综总分:{science[0]}({cha_s})")
        self.label_35.setText(
            f"离Rp-6目标还差:{sv_data.getData('pl')[0] - data_all}({round(data_all / sv_data.getData('pl')[0] * 100, 1)}%)")
        self.label_38.setText(
            f"语文:{sv_data.getData('ch')[-1]}({sv_data.getData('ch')[-1] - sv_data.getData('ch')[-2]})")
        self.label_39.setText(
            f"数学:{sv_data.getData('mt')[-1]}({sv_data.getData('mt')[-1] - sv_data.getData('mt')[-2]})")
        self.label_40.setText(
            f"鸟语:{sv_data.getData('en')[-1]}({sv_data.getData('en')[-1] - sv_data.getData('en')[-2]})")
        self.label_50.setText(
            f"物理:{sv_data.getData('ph')[-1]}({sv_data.getData('ph')[-1] - sv_data.getData('ph')[-2]})")
        self.label_51.setText(
            f"生物:{sv_data.getData('ob')[-1]}({sv_data.getData('ob')[-1] - sv_data.getData('ob')[-2]})")
        self.label_52.setText(
            f"化学:{sv_data.getData('chs')[-1]}({sv_data.getData('chs')[-1] - sv_data.getData('chs')[-2]})")
        if cha < 0:
            self.label_53.setText("综合评级:E(都倒退了就基本寄了)")
            self.label_53.setStyleSheet("color:red;")
        elif sv_data.getData('pl')[0] - data_all > 40:
            self.label_53.setText("综合评级:D(进步了但没有一点进展可不行哟)")
            self.label_53.setStyleSheet("color:red;")
        elif sv_data.getData('pl')[0] - data_all < 40:
            self.label_53.setText("综合评级:C(有丁点进展但很难看见)")
            self.label_53.setStyleSheet("color: rgb(255, 145, 19);")
        elif sv_data.getData('pl')[0] - data_all < 20:
            self.label_53.setText("综合评级:B(进度肉眼可见增加，加大力度)")
            self.label_53.setStyleSheet("color: yellow;")
        elif sv_data.getData('pl')[0] - data_all < 0:
            self.label_53.setText("综合评级:A(进度显著增加撑住！)")
            self.label_53.setStyleSheet("color: green;")
        else:
            self.label_53.setText("综合评级:S(完美完成计划)")
            self.label_53.setStyleSheet("color: rgb(37, 255, 240);")

    def saveSetting(self):
        with open("./setting/options.json", "w", encoding="utf-8") as f:
            js.dump(self.options, f)

    def sv_image(self):
        list1 = []
        sub = []
        if self.checkBox_8.isChecked():
            for i in self.sv_all:
                list1.append(sum(i))
            辐射计划6_镜像计划部分().图表([list1], ["ALL"], self.sv_q[-1])
        elif self.checkBox_7.isChecked():
            for i in self.sv_all:
                list1.append(sum(i[3:]))
            辐射计划6_镜像计划部分().图表([list1], ["SC"], self.sv_q[-1])
        else:
            for i in range(len(self.sv_check)):
                if self.sv_check[i].isChecked():
                    list1.append(self.sv_q[i])
                    sub.append(self.subject_en[i])
            辐射计划6_镜像计划部分().图表(list1, sub, self.sv_q[-1])

    def change_backgroundImage(self):
        self.options[0] = QFileDialog.getOpenFileName()[0]
        self.settings()
        self.saveSetting()

    def settings(self):
        self.Backgroud.setPixmap(QtGui.QPixmap(self.options[0]))
        self.optionsShow[0].setText("背景图片：" + self.options[0])
        self.optionsShow[1].setText(".SV文件储存位置：" + self.options[1])
        self.optionsShow[2].setCurrentText(self.options[2])
        self.optionsShow[3].setCurrentText(self.options[3])
        self.optionsShow[4].setCurrentText(self.options[4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sc = V_Rt2()
    sc.show()
    app.exec_()
