import sys

from PyQt5.QtCore import QUrl, QThread, pyqtSignal
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QApplication
import sys

a = QApplication(sys.argv)


class music_play(QThread):
    sign = pyqtSignal(str)

    def __init__(self, file="../../歌曲/你从未离去----白挺.mp3", master=None):
        try:
            super(music_play, self).__init__()
            file = QUrl.fromLocalFile(file)
            self.q1 = QMediaContent(file)
            self.qt = master
            self.q2 = QMediaPlayer()
            self.q2.setMedia(self.q1)
        except Exception as ee:
            print(ee)

    def run(self):
        self.q2.play()