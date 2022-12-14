"""
此文件为 新日暮里唱片机 窗口程序的配套脚本，用来操作本地播放界面的大部分窗口控件。
"""
from GUI import *
from typing import List
import os


class 播放列表:
    def __init__(self, master: Ui_MainWindow = None, music_names: List[str] = None):
        """不调用任何方法可以将歌曲添加进播放列表

        :param master: PyQt窗口对象
        :param music_names: 要播放的歌曲名
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
        """
        此类负责扫描本地音乐文件夹，找到音乐文件

        :param master: PyQt窗口对象
        """
        self.qt2 = master

    def 扫描(self, dirs=None):
        """
        扫描本地音乐文件夹，获取本地音乐文件

        :param dirs: 要扫描的文件夹路径
        :return: 扫描到的音乐文件
        """
        path_list = os.listdir(dirs)
        self.qt2.comboBox.clear()
        for i in range(len(path_list)):
            if path_list[i][-4:] in (".mp3", ".ogg"):
                a = path_list[i]
                self.qt2.comboBox.addItem(a)
            else:
                pass

    def 获取(self):
        """获取正在播放的歌曲名字，用于歌曲播放、切换和修改歌曲播放进度

        :return: 目前播放的歌曲名字
        """
        return self.qt2.comboBox.currentText()


if __name__ == "__main__":
    pass