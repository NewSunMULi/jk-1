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

pg.mixer.init()  # 初始化音乐播放模块，本程序使用Pygame播放音乐
t = Tk().withdraw()  # TK库隐藏它自带的窗口，此程序用PyQt5写的GUI(即窗口)，不需要tk窗口
pt = 1  # 它控制歌曲的暂停与继续
a = 0  # 和下面的一样，不同的只有它用于控制进度条和计时器
signNB = 1  # 这个变量的值可以作为信号来让某函数实现特定功能
clock = pg.time.Clock()  # 创建一个时钟，他可以控制程序频率或用于计时，频率越低计时越准
上一首序列 = -1  # 正在播放的歌曲在播放列表的位置，用它可以实现歌曲的转换(即下一首/上一首播放)
通用rid = []  # 创建一个列表，用于储存上一次搜索获得的歌曲的RID，实现边搜索边听上一次搜到的音乐，且可以由任意函数调用
通用序列 = 0  # 网络模式播放音乐要先缓存，再播放，使用序列定位播放的歌曲以控制下一首或上一首网络音乐的播放，这个序列所有函数皆可调用
FPS = 1  # 程序计时频率，频率越低计时越准，别问我为什么


class MuLi_Sanger_Ui:
    """
    Ui模式\n
    使用Qt Designer UI代码编写的窗口作为运行窗口，使用Qt Designer(Qt设计师)制作的ui文件可直接在此使用
    """

    def __init__(self):
        self.ap = QApplication(sys.argv)  # 创建一个窗口应用
        self.sc2 = uic.loadUi("GUI.ui")  # 加载Qt Designer UI文件
        self.rid = []  # 创建一个属性列表，用于储存搜索获得的歌曲的RID

    def run(self):
        with open("背景.json", "r", encoding="utf-8") as f:
            data = json.load(f)  # 获取(用户设置/初始)背景的文件路径
        with open("下载文件夹.json", "r", encoding="utf-8") as f:
            dirs = json.load(f)  # 获取(用户设置/初始)下载音乐要保存的文件夹路径
        # 扫描本地音乐文件
        本地音乐(self.sc2).扫描(dirs=dirs)  # 获取本地音乐，为本地播放提供文件搜索支持
        # 主页和本地音乐组件控制
        self.sc2.label_11.setText(f"{dirs}")  # 在提前设计好的窗口设置要显示的文本
        # QtGui.QPixmap()和tk.PhotoImage()功能一样，都用于加载图片
        self.sc2.label.setPixmap(QtGui.QPixmap(f"{data}"))  # 在提前设计好的窗口设置要显示的图片
        self.sc2.label_8.setText(f"{data}")
        self.sc2.ToHome.clicked.connect(self.Home)  # 在提前设计好的按钮上绑定函数，在按下这个按钮时触发绑定的函数，实现特定功能，这里实现切换界面到主页
        self.sc2.ToLM.clicked.connect(self.LM)  # 和上面一样，不同的是它可以将界面切换到本地音乐播放界面
        self.sc2.ToIT.clicked.connect(self.IT)  # 和上面一样，不同的是它可以将界面切换到设置界面
        self.sc2.Sosuo.clicked.connect(self.So)  # 按下(点击)这个按钮就会搜索用户想要的歌曲，并在窗口某个下拉条处返回搜索结果
        self.sc2.d_h.clicked.connect(self.Dl)  # 点击此按钮可下载网络上搜到的某个音乐到用户的电脑上
        self.sc2.ch_IP.clicked.connect(lambda x=None, y=self.sc2: 设置IT.Change_Picture(y))  # 点击此按钮可更改窗口背景图片
        self.sc2.Abous.clicked.connect(lambda x=None, y=self.sc2: 设置IT.About_us(y))  # 点击此按钮可查看关于这个程序的一些信息
        self.sc2.ch_IDL.clicked.connect(lambda x=None, y=self.sc2: 设置IT.Change_DL(y))  # 点击此按钮可设置保存歌曲的文件夹或者本地音乐所在的文件夹
        # 播放器播放状态设置
        self.sc2.up.clicked.connect(lambda sign=None, y=self.sc2: music_play.next(1, y))  # 点击此按钮可切换在播放列表内的上一首歌曲
        self.sc2.under.clicked.connect(lambda sign=None, y=self.sc2: music_play.next(2, y))  # 点击此按钮可切换在播放列表内的下一首歌曲
        self.sc2.play_h.clicked.connect(self.play)  # 点击此按钮，启用网络播放模式，播放网络上搜到的歌曲
        self.sc2.play_LM.clicked.connect(
            lambda sign=None, s=self.sc2: music_play().play(s, "l"))  # 点击此按钮，启用本地播放模式，播放本地音乐
        self.sc2.pause.clicked.connect(music_play.pause)  # 暂停或继续音乐的播放
        # self.sc2.next_LM.clicked.connect()  # 设置下一首要播放的歌曲，当正在播放的歌曲播放完时，就播放用户设置的歌曲(在网络播放模式下可用)
        # self.sc2.next_h.clicked.connect()  # 设置下一首要播放的歌曲，当正在播放的歌曲播放完时，就播放用户设置的歌曲(在本地播放模式下可用)
        # 开启多线程进行播放计时，为用户调控歌曲播放进度提供支持(例如像其他播放器一样拖拉进度条快进或快退)
        a = 计时(self.sc2)  # 此线程负责记录乐曲播放的时间和进度
        a.start()  # 开启线程，功能开始发挥
        b = 改时(self.sc2)  # 此线程负责支持用户改变乐曲播放的时间和进度
        b.start()
        # 主页和设置按钮设置， 窗口设置
        self.sc2.show()  # 显示窗口
        self.sc2.LM.hide()  # 隐藏本地音乐播放界面
        self.sc2.IT.hide()  # 隐藏设置播放界面
        self.sc2.huan1.hide()  # 隐藏主页
        self.sc2.ToHome.setCheckable(True)  # 设置按钮状态，这里设置为点击一次按钮激活，再点击一次按钮关闭不再处于激活状态
        self.sc2.ToIT.setCheckable(True)  # 设置按钮状态，这里设置为点击一次按钮激活，再点击一次按钮关闭不再处于激活状态
        self.sc2.ToLM.setCheckable(True)  # 设置按钮状态，这里设置为点击一次按钮激活，再点击一次按钮关闭不再处于激活状态
        self.sc2.ToHome.setChecked(True)  # 设置按钮状态，这里设置为点击一次按钮激活，再点击一次按钮关闭不再处于激活状态
        self.ap.exec_()  # 保存窗口运行直到程序出Bug闪退/崩溃或者用户自己关闭窗口

    def Home(self):
        """
        实现界面切换到首页的函数

        :return: 没有返回任何东西
        """
        self.sc2.ToHome.setChecked(True)  # 激活此按钮
        self.sc2.ToIT.setChecked(False)
        self.sc2.ToLM.setChecked(False)
        self.sc2.Home.show()  # 展示首页
        self.sc2.LM.hide()
        self.sc2.IT.hide()  # 隐藏本地播放界面和设置界面

    def IT(self):
        """
        实现界面切换到设置的函数

        :return: 没有返回任何东西
        """
        self.sc2.ToIT.setChecked(True)
        self.sc2.ToLM.setChecked(False)
        self.sc2.ToHome.setChecked(False)
        self.sc2.IT.show()
        self.sc2.LM.hide()
        self.sc2.Home.hide()

    def LM(self):
        """
        实现界面切换到本地播放界面的函数

        :return: 没有返回任何东西
        """
        self.sc2.ToLM.setChecked(True)
        self.sc2.ToIT.setChecked(False)
        self.sc2.ToHome.setChecked(False)
        self.sc2.LM.show()
        self.sc2.Home.hide()
        self.sc2.IT.hide()

    def So(self):
        """
        此函数实现搜索并在窗口某个下拉条处输出搜索结果

        :param self: 类中的函数如果没设置为静态，必须带一个参数用来接收创建此类的对象,一般叫做self
        :return: 歌曲搜索结果
        """
        s = GUI_Requests('qt5', self.sc2, self.sc2.lineEdit.text()). \
            老狗搜索('comboBox', self.sc2.comboBox_3)  # 调用ML_Home脚本里搜索函数，脚本里有对此函数的注释
        self.rid.clear()  # 清空列表
        for i in s:  # 循环/遍历
            self.rid.append(i['rid识别号'])  # 挨个将搜索结果添加进结果列表

    def Dl(self):
        """
        此函数可将搜索到的歌曲下载到用户电脑上

        :return: 歌曲
        """
        global 通用序列  # 设置变量 通用序列 在此函数中可以被修改(设置变量为全局变量)
        通用rid.clear()
        rid = self.sc2.comboBox_3.currentIndex()  # 获取下拉条被用户选中的元素，此处获取用户想要下载的歌曲
        通用序列 = self.sc2.comboBox_3.currentIndex()  # 和上面一样，只是这两个下拉条负责显示不同东西
        GUI_Requests().download('老狗', self.rid[rid], self.sc2.label_11.text() + "/" + self.sc2.comboBox_3.currentText(),
                                self.sc2.huan1)  # 调用ML_Home脚本里的下载函数，脚本里有对此函数的注释
        本地音乐(master=self.sc2).扫描(self.sc2.label_11.text())  # 在此扫描文件夹，更新本地音乐列表

    def play(self):
        """
        播放音乐
        """
        self.Dl()  # 在同一个类中调用不同函数(方法), 可以使用 self.函数名(参数) 来使用(调用)函数
        music_play.play(master=self.sc2, page='h')  # 调用其他类中的静态函数，可直接使用 类名.静态函数名(参数) 调用函数
        for kl in self.rid:  # 循环结构在比较完整的程序中经常会用很多次
            通用rid.append(kl)  # 更新通用rid列表里的rid号，保存为上一次的搜索数据供其它函数使用


class MuLi_Sanger_Py:
    """
    py模式\n
    使用纯py代码编写的窗口作为运行窗口，ui文件必须经过转化成py文件才可使用，但是py模式可以安全高效使用插件以扩充程序功能
    """

    def __init__(self):
        """
        大部分变量和Ui模式一样，这里就不作过多注释了
        """
        global 通用rid
        self.ap = QApplication(sys.argv)
        self.sc = QMainWindow()  # 建立一个新窗口
        self.sc2 = Ui_MainWindow()  # 加载py代码编写的窗口代码(实例化用py代码编写的窗口类)
        self.sc2.setupUi(self.sc)  # 将py窗口代码载入你写的程序里
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

    def play(self):
        self.Dl()
        music_play.play(master=self.sc2, page='h')
        for kl in self.rid:
            通用rid.append(kl)


class 设置IT:
    """设置模块，为用户设置程序提供支持"""

    def __init__(self):
        """
        pass 关键字，跳过这一个函数/代码 ---- 有这个代表此处无任何操作直接跳过
        """
        pass

    @staticmethod  # 这个就是静态函数修饰符，类中的函数(方法)上方只要有这个，就不需要参数self了
    def Change_Picture(master):
        try:
            data1 = askopenfilename(title="选一张背景图片", filetype=[("图片", ".png"), ("压缩图片", ".jpg"),
                                                               ("经典位图", ".bmp"), ("网页下载图片", ".jpeg"),
                                                               ("gif图片", ".gif"),
                                                               ("网页图片", ".webp")])  # 打开文件选择对话框，让用户选择图片
            with open("背景.json", "w", encoding="utf-8") as f:
                json.dump(data1, f)  # 将(用户设置/初始)背景的文件路径保存，下次就可以直接使用而无须再次设置
            master.label.setPixmap(QtGui.QPixmap(f"{data1}"))  # 第四十三行代码和它一模一样，上面有注释
            master.label_8.setText(f"{data1}")  # 对此代码的注释上面也有
        except Exception as f:  # try-except模块用于捕获程序错误(也就是Bug)而不导致程序崩溃，为改良代码提供信息
            print(f)  # 输出错误信息

    @staticmethod
    def About_us(master):
        try:
            QMessageBox.about(master, "关于我们", "开发者：陈玄\n赠与赵靖凯......")  # 开发者想说的话可以写在Qt5弹窗的about模块
        except Exception as e:
            print(e)

    @staticmethod
    def Change_DL(master):
        dirs = askdirectory(title="选择你的下载文件夹")  # 打开文件夹选择对话框，让用户选择文件夹
        with open("下载文件夹.json", "w", encoding="utf-8") as f:
            json.dump(dirs, f)  # 将(用户设置/初始)背景的文件夹路径保存，下次就可以直接使用而无须再次设置
        master.label_11.setText(f"{dirs}")
        本地音乐(master).扫描(dirs=dirs)  # 扫描并更新本地音乐文件


class music_play:
    """
    用于音乐播放，暂停，切换的一个类
    """

    def __init__(self):
        pass

    @staticmethod
    def play(master: Ui_MainWindow, page="l"):
        """
        播放音乐函数，调用可播放音频

        :param master: 父组件----装着所以窗口组件的窗口对象，例如窗口MainWindow()就装所有qt5控件
        :param page: 模式，h-网络播放模式，l-本地播放模式
        :return: 没得
        """
        global signNB, 上一首序列
        signNB = 3
        if page == "h":
            now = master.comboBox_3  # 将下拉条赋值给局部变量now，作变量转移
        else:
            now = master.comboBox
        try:
            music_play.转换(master, now)  # 将其他下拉条的值转入播放列表下拉条里
            play_path = now.currentText()
            lt = mutagen.mp3.MP3(master.label_11.text() + "/" + play_path)  # 获取单首乐曲的信息
            master.horizontalSlider.setMaximum(int(lt.info.length) * FPS)  # 获取单首乐曲的时长，并设置进度条的最大值为乐曲时长(单位为秒)
            master.all_time.setText(f"总时长:{int(lt.info.length)}s")  # 输出乐曲的总时长
            pg.mixer.music.load(master.label_11.text() + "/" + play_path)  # 将音频加载，准备播放
            pg.mixer.music.play()  # 播放音频
            master.label_5.setText(f'歌曲名字:{play_path[:-4]}')  # 输出正在播放的乐曲的名字
            播放列表(master, []).change(play_path)  # 改变播放列表，输出正在播放乐曲的名字
            上一首序列 = now.currentIndex()
        except Exception as e:
            print(e)

    @staticmethod
    def pause():
        """
        控制歌曲的暂停播放和继续播放
        :return: 无
        """
        global pt  # 控制乐曲暂停或继续的信号
        if pt == 1:
            pg.mixer.music.pause()  # 暂停乐曲播放
            pt = 2
        else:
            pg.mixer.music.unpause()  # 继续乐曲播放
            pt = 1

    @staticmethod
    def next(sg=1, master: Ui_MainWindow = None, 进度条=True):
        """
        控制上一首/下一首歌曲的播放

        :param sg: 信号，用来控制上一曲还是下一曲
        :param master: 父容器，和此类的play函数里的一样
        :param 进度条: 是否使用进度条来显示歌曲缓存/下载/载入进度
        :return: 无
        """
        global 上一首序列, signNB, 通用序列
        signNB = 2  # 用来控制计时器的信号
        if 上一首序列 + 1 >= master.comboBox_2.count():
            上一首序列 = -1  # 如果正在播放的是最后一首歌曲，他的下一首就为播放列表第一首，防止抛出索引错误引发程序崩溃
        elif master.comboBox_2.currentText() == "我让":
            sg = -1  # 此处纯粹防止有些人炒冷饭，无其他作用
        elif 上一首序列 - 1 < 0 and sg == 1:
            上一首序列 = master.comboBox_2.count() - 1  # 如果正在播放的是第一首歌曲，他的上一首就为播放列表最后一首，防止抛出索引错误引发程序崩溃

        if sg == 1:  # 播放上一首歌曲
            try:
                pg.mixer.music.stop()  # 停止播放歌曲
                play_path = master.comboBox_2.itemText(上一首序列 - 1)  # 获取正在播放的乐曲的上一首乐曲的信息
                music_play.转换(master, master.comboBox_2)  # 下面的都和此类中play()函数一样
                lt = mutagen.mp3.MP3(master.label_11.text() + "/" + play_path)
                master.horizontalSlider.setMaximum(int(lt.info.length) * FPS)
                master.all_time.setText(f"总时长:{int(lt.info.length)}s")
                pg.mixer.music.load(master.label_11.text() + "/" + play_path)
                pg.mixer.music.play()
                master.label_5.setText(f'歌曲名字:{play_path[:-4]}')
                播放列表(master, []).change(play_path)
            except Exception:  # 如果是网络播放模式且要播放的歌曲不存在于本地文件夹中，就执行except里面的代码
                if 通用序列 > 0 and sg == 1:
                    f = 通用序列 - 1  # 和上一首序列变量的改变差不多
                    GUI_Requests().download('老狗', 通用rid[f],
                                            master.label_11.text() + "/" + master.comboBox_2.itemText(f),
                                            Qt进度条=master.huan1, 进度条使用=进度条)
                    music_play.next(sg=1, master=master)  # 重复调用自己
                    通用序列 -= 1
                else:
                    通用序列 = master.comboBox_3.count() - 1
                    music_play.next(sg=1, master=master)
            else:  # 如果except里面的代码不执行，就将上一首播放的歌曲索引-1来指向现在播放的歌曲，为下一次切换上一首歌曲做准备
                上一首序列 -= 1

        elif sg == 2:  # 下一首播放，功能和上面上一首播放差不多，只是切换方向反了而已(例如-变成+)
            try:
                pg.mixer.music.stop()
                play_path = master.comboBox_2.itemText(上一首序列 + 1)
                music_play.转换(master, master.comboBox_2)
                lt = mutagen.mp3.MP3(master.label_11.text() + "/" + play_path)
                master.horizontalSlider.setMaximum(int(lt.info.length) * FPS)
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
        """
        此函数可实现不同下拉条内的元素的转换

        :param master: 父容器，和上面一样的
        :param com: 下拉条对象
        :param a1: 起始索引
        :return: 无
        """
        num = com.count()  # 获取下拉条中元素的个数，和列表一样
        # 之后下拉条的操作和列表一样，不作过多注释
        if num > master.comboBox_2.count():
            for i in range(master.comboBox_2.count(), num):
                master.comboBox_2.addItem('')  # 添加元素
        if num < master.comboBox_2.count():
            master.comboBox_2.clear()
            for i in range(master.comboBox_2.count(), num):
                master.comboBox_2.addItem('')
        while len(com.itemText(a1)) > 0 and com is not master.comboBox_2:
            try:
                master.comboBox_2.setItemText(a1, com.itemText(a1))  # 等价于list[a1] = value(值)
                a1 += 1
            except Exception as e:
                print(e)
                break  # 强制退出循环


class 计时(QThread):  # QThread 多线程
    """此类用于歌曲播放计时"""
    sign = pyqtSignal(str)  # 多线程必须带这个

    def __init__(self, master: Ui_MainWindow):
        try:
            super().__init__()  # 继承QThread
            self.qt3 = master
        except Exception as eee:
            print(eee)

    def run(self):  # 创建多线程后自动执行run()
        global signNB, a, 上一首序列, FPS
        try:
            yuan = 上一首序列
            while True:
                clock.tick(FPS)  # 循环频率
                a = self.qt3.horizontalSlider.value()  # 获取下拉条的值
                if pg.mixer.music.get_busy():
                    if yuan == -1:
                        a = int(pg.mixer.music.get_pos() // 1000 * FPS)
                        self.qt3.horizontalSlider.setValue(a)
                        signNB = 1
                        yuan = 上一首序列
                        a += 1
                    elif signNB == 3 and 上一首序列 == yuan:
                        a = int(pg.mixer.music.get_pos() // 1000 * FPS)
                        a += 1
                        self.qt3.horizontalSlider.setValue(a)
                        signNB = 1
                    elif yuan != 上一首序列:
                        a = int(pg.mixer.music.get_pos() // 1000 * FPS)
                        a += 1
                        self.qt3.horizontalSlider.setValue(a)
                        yuan = 上一首序列
                        time.sleep(1 / FPS)
                        a += 1
                        self.qt3.horizontalSlider.setValue(a)
                        signNB = 1
                    else:
                        a += 1
                        self.qt3.jishiqi.setProperty('value', a // FPS)
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
            clock.tick(7)
            try:
                yuan2 = self.qt.horizontalSlider.value()
                if ((
                            yuan - yuan2) > 0 or yuan - yuan2 < -1 * FPS) and pg.mixer.music.get_busy() and signNB != 2 and signNB != 3:
                    pg.mixer.music.pause()
                    play_path = self.qt.comboBox_2.itemText(上一首序列)
                    pg.mixer.music.load(self.qt.label_11.text() + "/" + play_path)
                    pg.mixer.music.play(start=yuan2 // FPS)
                    self.qt.jishiqi.setProperty('value', yuan2 // FPS)
                    yuan = yuan2
                elif 上一首序列 == -1:
                    self.qt.horizontalSlider.setValue(0)
                else:
                    self.qt.jishiqi.setProperty('value', yuan2 // FPS)
                    yuan = yuan2
                if yuan2 > self.qt.horizontalSlider.maximum() - 1:
                    music_play.next(sg=2, master=self.qt, 进度条=False)
                    self.qt.horizontalSlider.setValue(0)
            except Exception as ee:
                print(ee)


if __name__ == "__main__":
    MuLi_Sanger_Ui().run()
