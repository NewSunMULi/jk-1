from 辐射组管理程序2ui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
import sys


class V_Rt2(QtWidgets.QWidget, Ui_app):
    def __init__(self):
        self.Signing = False
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("辐射组管理程序2")
        icon1 = QtGui.QIcon('../logo.ico')
        self.setWindowIcon(icon1)
        self.Plan.hide()
        self.Game.hide()
        self.Data.hide()
        self.FrApp.hide()
        self.SV.hide()
        self.SignUp.hide()
        self.LogUp.hide()
        self.Setting.hide()
        self.pushButton_16.clicked.connect(self.setting)
        self.pushButton_13.clicked.connect(self.Sign_Up)
        self.Backward_6.clicked.connect(self.ToHome)
        self.Backward_8.clicked.connect(self.save)
        self.verticalScrollBar.valueChanged.connect(self.change_position)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sc = V_Rt2()
    sc.show()
    app.exec_()