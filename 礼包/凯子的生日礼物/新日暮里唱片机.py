import time
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from ML_Loc import *
from ML_Home import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Tk
import sys, json, mutagen.mp3
import pygame as pg

pg.mixer.init()
t = Tk().withdraw()
pt = 1
a = 0
signNB = 1
clock = pg.time.Clock()
上一首序列 = -1
通用rid = []
通用序列 = 0


class MuLi_Sanger_Ui:
    def __init__(self):
        self.ap = QApplication(sys.argv)
        self.sc2 = uic.loadUi("GUI.ui")
        self.rid = []

    def run(self):
        with open("背景.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("下载文件夹.json", "r", encoding="utf-8") as f:
            dirs = json.load(f)
        # 扫描本地音乐文件
        本地音乐(self.sc2).扫描(dirs=dirs)
        # 主页和本地音乐组件控制
        self.sc2.label_11.setText(f"{dirs}")
        self.sc2.label.setPixmap(QtGui.QPixmap(f"{data}"))
        self.sc2.label_8.setText(f"{data}")
        self.sc2.ToHome.clicked.connect(self.Home)
        self.sc2.ToLM.clicked.connect(self.LM)
        self.sc2.ToIT.clicked.connect(self.IT)
        self.sc2.Sosuo.clicked.connect(self.So)
        self.sc2.d_h.clicked.connect(self.Dl)
        self.sc2.ch_IP.clicked.connect(lambda x=None, y=self.sc2: 设置IT.Change_Picture(y))
        self.sc2.Abous.clicked.connect(lambda x=None, y=self.sc2: 设置IT.About_us(y))
        self.sc2.ch_IDL.clicked.connect(lambda x=None, y=self.sc2: 设置IT.Change_DL(y))
        # 播放器播放状态设置
        self.sc2.up.clicked.connect(lambda sign=None, y=self.sc2: music_play.next(1, y))
        self.sc2.under.clicked.connect(lambda sign=None, y=self.sc2: music_play.next(2, y))
        self.sc2.play_h.clicked.connect(self.play)
        self.sc2.play_LM.clicked.connect(lambda sign=None, s=self.sc2: music_play().play(s, "l"))
        self.sc2.pause.clicked.connect(music_play.pause)
        # self.sc2.next_LM.clicked.connect()
        # self.sc2.next_h.clicked.connect()
        # 线程
        a = 计时(self.sc2)
        a.start()
        b = 改时(self.sc2)
        b.start()
        # 主页和设置按钮设置， 窗口设置
        self.sc2.show()
        self.sc2.LM.hide()
        self.sc2.IT.hide()
        self.sc2.huan1.hide()
        self.sc2.ToHome.setCheckable(True)
        self.sc2.ToIT.setCheckable(True)
        self.sc2.ToLM.setCheckable(True)
        self.sc2.ToHome.setChecked(True)
        self.ap.exec_()

    def Home(self):
        self.sc2.ToHome.setChecked(True)
        self.sc2.ToIT.setChecked(False)
        self.sc2.ToLM.setChecked(False)
        self.sc2.Home.show()
        self.sc2.LM.hide()
        self.sc2.IT.hide()

    def IT(self):
        self.sc2.ToIT.setChecked(True)
        self.sc2.ToLM.setChecked(False)
        self.sc2.ToHome.setChecked(False)
        self.sc2.IT.show()
        self.sc2.LM.hide()
        self.sc2.Home.hide()

    def LM(self):
        self.sc2.ToLM.setChecked(True)
        self.sc2.ToIT.setChecked(False)
        self.sc2.ToHome.setChecked(False)
        self.sc2.LM.show()
        self.sc2.Home.hide()
        self.sc2.IT.hide()

    def So(self):
        s = GUI_Requests('qt5', self.sc2, self.sc2.lineEdit.text()). \
            老狗搜索('comboBox', self.sc2.comboBox_3)
        self.rid.clear()
        for i in s:
            self.rid.append(i['rid识别号'])

    def Dl(self):
        global 通用序列
        通用rid.clear()
        rid = self.sc2.comboBox_3.currentIndex()
        通用序列 = self.sc2.comboBox_3.currentIndex()
        GUI_Requests().download('老狗', self.rid[rid], self.sc2.label_11.text() + "/" + self.sc2.comboBox_3.currentText(),
                                self.sc2.huan1)
        本地音乐(master=self.sc2).扫描(self.sc2.label_11.text())
        for kl in self.rid:
            通用rid.append(kl)

    def play(self):
        self.Dl()
        music_play.play(master=self.sc2, page='h')


class MuLi_Sanger_Py:
    def __init__(self):
        global 通用rid
        self.ap = QApplication(sys.argv)
        self.sc = QMainWindow()
        self.sc2 = Ui_MainWindow()
        self.sc2.setupUi(self.sc)
        self.rid = []

    def run(self):
        with open("背景.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("下载文件夹.json", "r", encoding="utf-8") as f:
            dirs = json.load(f)
        # 扫描本地音乐文件
        本地音乐(self.sc2).扫描(dirs=dirs)
        # 主页和本地音乐组件控制
        self.sc2.label_11.setText(f"{dirs}")
        self.sc2.label.setPixmap(QtGui.QPixmap(f"{data}"))
        self.sc2.label_8.setText(f"{data}")
        self.sc2.ToHome.clicked.connect(self.Home)
        self.sc2.ToLM.clicked.connect(self.LM)
        self.sc2.ToIT.clicked.connect(self.IT)
        self.sc2.Sosuo.clicked.connect(self.So)
        self.sc2.d_h.clicked.connect(self.Dl)
        self.sc2.ch_IP.clicked.connect(lambda x=None, y=self.sc2: 设置IT.Change_Picture(y))
        self.sc2.Abous.clicked.connect(lambda x=None, y=self.sc: 设置IT.About_us(y))
        self.sc2.ch_IDL.clicked.connect(lambda x=None, y=self.sc2: 设置IT.Change_DL(y))
        # 播放器播放状态设置
        self.sc2.up.clicked.connect(lambda sign=None, y=self.sc2: music_play.next(1, y))
        self.sc2.under.clicked.connect(lambda sign=None, y=self.sc2: music_play.next(2, y))
        self.sc2.play_h.clicked.connect(self.play)
        self.sc2.play_LM.clicked.connect(lambda sign=None, s=self.sc2: music_play().play(s, "l"))
        self.sc2.pause.clicked.connect(music_play.pause)
        # self.sc2.next_LM.clicked.connect()
        # self.sc2.next_h.clicked.connect()
        # 线程
        a = 计时(self.sc2)
        a.start()
        b = 改时(self.sc2)
        b.start()
        # 主页和设置按钮设置， 窗口设置
        self.sc.show()
        self.sc2.LM.hide()
        self.sc2.IT.hide()
        self.sc2.huan1.hide()
        self.sc2.ToHome.setCheckable(True)
        self.sc2.ToIT.setCheckable(True)
        self.sc2.ToLM.setCheckable(True)
        self.sc2.ToHome.setChecked(True)
        self.ap.exec_()

    def Home(self):
        self.sc2.ToHome.setChecked(True)
        self.sc2.ToIT.setChecked(False)
        self.sc2.ToLM.setChecked(False)
        self.sc2.Home.show()
        self.sc2.LM.hide()
        self.sc2.IT.hide()

    def IT(self):
        self.sc2.ToIT.setChecked(True)
        self.sc2.ToLM.setChecked(False)
        self.sc2.ToHome.setChecked(False)
        self.sc2.IT.show()
        self.sc2.LM.hide()
        self.sc2.Home.hide()

    def LM(self):
        self.sc2.ToLM.setChecked(True)
        self.sc2.ToIT.setChecked(False)
        self.sc2.ToHome.setChecked(False)
        self.sc2.LM.show()
        self.sc2.Home.hide()
        self.sc2.IT.hide()

    def So(self):
        s = GUI_Requests('qt5', self.sc2, self.sc2.lineEdit.text()). \
            老狗搜索('comboBox', self.sc2.comboBox_3)
        self.rid.clear()
        for i in s:
            self.rid.append(i['rid识别号'])

    def Dl(self):
        global 通用序列
        print(self.rid, 通用rid)
        通用rid.clear()
        rid = self.sc2.comboBox_3.currentIndex()
        通用序列 = self.sc2.comboBox_3.currentIndex()
        GUI_Requests().download('老狗', self.rid[rid], self.sc2.label_11.text() + "/" + self.sc2.comboBox_3.currentText(),
                                self.sc2.huan1)
        本地音乐(master=self.sc2).扫描(self.sc2.label_11.text())
        for kl in self.rid:
            通用rid.append(kl)

    def play(self):
        self.Dl()
        music_play.play(master=self.sc2, page='h')


class 设置IT:
    def __init__(self):
        pass

    @staticmethod
    def Change_Picture(master):
        try:
            data1 = askopenfilename(title="选一张背景图片", filetype=[("图片", ".png"), ("压缩图片", ".jpg"),
                                                               ("经典位图", ".bmp"), ("网页下载图片", ".jpeg"),
                                                               ("gif图片", ".gif"), ("网页图片", ".webp")])
            with open("背景.json", "w", encoding="utf-8") as f:
                json.dump(data1, f)
            master.label.setPixmap(QtGui.QPixmap(f"{data1}"))
            master.label_8.setText(f"{data1}")
        except Exception as f:
            print(f)

    @staticmethod
    def About_us(master):
        try:
            QMessageBox.about(master, "关于我们", "开发者：陈玄\n赠与赵靖凯......")
        except Exception as e:
            print(e)

    @staticmethod
    def Change_DL(master):
        dirs = askdirectory(title="选择你的下载文件夹")
        with open("下载文件夹.json", "w", encoding="utf-8") as f:
            json.dump(dirs, f)
        master.label_11.setText(f"{dirs}")
        本地音乐(master).扫描(dirs=dirs)


class music_play:
    def __init__(self):
        pass

    @staticmethod
    def play(master: Ui_MainWindow, page="l"):
        global signNB, 上一首序列
        signNB = 3
        if page == "h":
            now = master.comboBox_3
        else:
            now = master.comboBox
        try:
            music_play.转换(master, now)
            play_path = now.currentText()
            lt = mutagen.mp3.MP3(master.label_11.text() + "/" + play_path)
            master.horizontalSlider.setMaximum(int(lt.info.length))
            master.all_time.setText(f"总时长:{int(lt.info.length)}s")
            pg.mixer.music.load(master.label_11.text() + "/" + play_path)
            pg.mixer.music.play()
            master.label_5.setText(f'歌曲名字:{play_path[:-4]}')
            播放列表(master, []).change(play_path)
            上一首序列 = now.currentIndex()
        except Exception as e:
            print(e)

    @staticmethod
    def pause():
        global pt
        if pt == 1:
            pg.mixer.music.pause()
            pt = 2
        else:
            pg.mixer.music.unpause()
            pt = 1

    @staticmethod
    def next(sg=1, master: Ui_MainWindow = None, 进度条=True):
        global 上一首序列, signNB, 通用序列
        signNB = 2
        if 上一首序列 + 1 >= master.comboBox_2.count():
            上一首序列 = -1
        elif master.comboBox_2.currentText() == "我让":
            sg = -1
        elif 上一首序列 - 1 < 0 and sg == 1:
            上一首序列 = master.comboBox_2.count() - 1

        if sg == 1:
            try:
                pg.mixer.music.stop()
                play_path = master.comboBox_2.itemText(上一首序列 - 1)
                music_play.转换(master, master.comboBox_2)
                lt = mutagen.mp3.MP3(master.label_11.text() + "/" + play_path)
                master.horizontalSlider.setMaximum(int(lt.info.length))
                master.all_time.setText(f"总时长:{int(lt.info.length)}s")
                pg.mixer.music.load(master.label_11.text() + "/" + play_path)
                pg.mixer.music.play()
                master.label_5.setText(f'歌曲名字:{play_path[:-4]}')
                播放列表(master, []).change(play_path)
            except Exception:
                if 通用序列 > 0 and sg == 1:
                    f = 通用序列 - 1
                    GUI_Requests().download('老狗', 通用rid[f], master.label_11.text() + "/" + master.comboBox_2.itemText(f),
                                            Qt进度条=master.huan1, 进度条使用=进度条)
                    music_play.next(sg=1, master=master)
                    通用序列 -= 1
                else:
                    通用序列 = master.comboBox_3.count() - 1
                    music_play.next(sg=1, master=master)
            else:
                上一首序列 -= 1

        elif sg == 2:
            try:
                pg.mixer.music.stop()
                play_path = master.comboBox_2.itemText(上一首序列 + 1)
                music_play.转换(master, master.comboBox_2)
                lt = mutagen.mp3.MP3(master.label_11.text() + "/" + play_path)
                master.horizontalSlider.setMaximum(int(lt.info.length))
                master.all_time.setText(f"总时长:{int(lt.info.length)}s")
                pg.mixer.music.load(master.label_11.text() + "/" + play_path)
                pg.mixer.music.play()
                master.label_5.setText(f'歌曲名字:{play_path[:-4]}')
                播放列表(master, []).change(play_path)
            except Exception:
                f = 通用序列 + 1
                GUI_Requests().download('老狗', 通用rid[f],
                                        master.label_11.text() + "/" + master.comboBox_2.itemText(f),
                                        Qt进度条=master.huan1, 进度条使用=进度条)
                music_play.next(sg=2, master=master)
                通用序列 += 1
            else:
                上一首序列 += 1

    @staticmethod
    def 转换(master: Ui_MainWindow = None, com: QtWidgets.QComboBox = None, a1=0):
        num = com.count()
        if num > master.comboBox_2.count():
            for i in range(master.comboBox_2.count(), num):
                master.comboBox_2.addItem('')
        if num < master.comboBox_2.count():
            master.comboBox_2.clear()
            for i in range(master.comboBox_2.count(), num):
                master.comboBox_2.addItem('')
        while len(com.itemText(a1)) > 0 and com is not master.comboBox_2:
            try:
                master.comboBox_2.setItemText(a1, com.itemText(a1))
                a1 += 1
            except Exception as e:
                print(e)
                break


class 计时(QThread):
    sign = pyqtSignal(str)

    def __init__(self, master: Ui_MainWindow):
        try:
            super().__init__()
            self.qt3 = master
        except Exception as eee:
            print(eee)

    def run(self):
        global signNB, a, 上一首序列
        try:
            yuan = 上一首序列
            while True:
                clock.tick(1)
                a = self.qt3.horizontalSlider.value()
                if pg.mixer.music.get_busy():
                    if yuan == -1:
                        a = 0
                        a += 1
                        self.qt3.horizontalSlider.setValue(a)
                        signNB = 1
                        yuan = 上一首序列
                    elif signNB == 3 and 上一首序列 == yuan:
                        a = 0
                        self.qt3.horizontalSlider.setValue(a)
                        a += 1
                        self.qt3.horizontalSlider.setValue(a)
                        signNB = 1
                    elif yuan != 上一首序列:
                        a = 0
                        self.qt3.horizontalSlider.setValue(a)
                        a += 1
                        self.qt3.horizontalSlider.setValue(a)
                        yuan = 上一首序列
                        time.sleep(1 / 30)
                        signNB = 1
                    else:
                        a += 1
                        self.qt3.jishiqi.setProperty('value', a)
                        self.qt3.horizontalSlider.setValue(a)
                else:
                    pass

        except Exception as ee:
            print(ee)


class 改时(QThread):
    si = pyqtSignal(str)

    def __init__(self, master: Ui_MainWindow):
        super().__init__()
        self.qt = master

    def run(self):
        yuan = self.qt.horizontalSlider.value()
        while True:
            clock.tick(15)
            try:
                yuan2 = self.qt.horizontalSlider.value()
                if ((yuan - yuan2) > 0 or yuan - yuan2 < -1) and pg.mixer.music.get_busy() and signNB != 2 and signNB != 3:
                    print(yuan - yuan2)
                    pg.mixer.music.pause()
                    play_path = self.qt.comboBox_2.itemText(上一首序列)
                    pg.mixer.music.load(self.qt.label_11.text() + "/" + play_path)
                    pg.mixer.music.play(start=yuan2)
                    self.qt.jishiqi.setProperty('value', yuan2)
                    yuan = yuan2
                elif 上一首序列 == -1:
                    self.qt.horizontalSlider.setValue(0)
                else:
                    self.qt.jishiqi.setProperty('value', yuan2)
                    yuan = yuan2
                if yuan2 >= self.qt.horizontalSlider.maximum() - 1:
                    music_play.next(sg=2, master=self.qt, 进度条=False)
                    self.qt.horizontalSlider.setValue(0)
            except Exception as ee:
                print(ee)


if __name__ == "__main__":
    MuLi_Sanger_Ui().run()
