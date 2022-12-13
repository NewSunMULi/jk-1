from GUI import *
from typing import List
import os


class 播放列表:
    def __init__(self, master: Ui_MainWindow = None, music_names: List[str] = None):
        """不调用任何方法可以将歌曲添加进播放列表
        :type master: PyQt窗口对象
        """
        self.qt = master
        for i in range(len(music_names)):
            master.comboBox_2.addItem(music_names[i])

    def change(self, music_name):
        self.qt.comboBox_2.setCurrentText(music_name)

    def get(self):
        return self.qt.comboBox_2.currentText()


class 本地音乐:
    def __init__(self, master: Ui_MainWindow = None):
        self.qt2 = master

    def 扫描(self, dirs=None):
        path_list = os.listdir(dirs)
        self.qt2.comboBox.clear()
        for i in range(len(path_list)):
            if path_list[i][-4:] in (".mp3", ".ogg"):
                a = path_list[i]
                self.qt2.comboBox.addItem(a)
            else:
                pass

    def 获取(self):
        return self.qt2.comboBox.currentText()


if __name__ == "__main__":
    pass