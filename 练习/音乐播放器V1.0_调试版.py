from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
import sys, time
from 窗口01 import *
from pygame.mixer import init, music
from pygame.time import Clock
from play_qt5 import *

sc = QApplication(sys.argv)
sc2 = uic.loadUi("窗口01.ui")
t = 0
t3 = Clock()


class 数字输出(QThread):
    sign = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global t
        while True:
            t3.tick(30)
            xy = sc2.horizontalSlider.value()
            sc2.jishiqi.setProperty("value", xy)


class MyThread(QThread):
    sign = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        global t
        jk = True
        g = 0
        while True:
            if music.get_busy():
                time.sleep(1)
                t += 1
                if sc2.horizontalSlider.value() == g:
                    sc2.horizontalSlider.setValue(t)
                    g = sc2.horizontalSlider.value()
                else:
                    t = sc2.horizontalSlider.value()
                    g = sc2.horizontalSlider.value()
            else:
                pass


def 函数01():
    # sc2.comboBox.currentText()获取输入框内的字符
    a = music_play()
    init()
    a.start()


def ui加载():
    sc2.show()
    sc2.bt1.clicked.connect(函数01)
    sc2.ti.clicked.connect(music.pause)
    sc2.zh.clicked.connect(music.unpause)
    print(sc2.horizontalSlider.value())
    sc.exec_()


def py加载():
    sc = QApplication(sys.argv)
    sc2 = QMainWindow()
    sc3 = Ui_MainWindow()
    sc3.setupUi(sc2)
    sc2.show()
    sc3.bt1.clicked.connect(函数01)
    sc.exec_()


ui加载()
