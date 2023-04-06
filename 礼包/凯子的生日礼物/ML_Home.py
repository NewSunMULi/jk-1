"""
此文件为 新日暮里唱片机 窗口程序的配套脚本，用来操作主页的一些窗口控件。\n
但里面的一些函数/类可在其他使用Tk和PyQt5做的窗口程序中使用，例如GUI_Requests()可以为播放器类窗口程序提供网络音乐搜索，下载，显示支持
"""
from GUI import *
from typing import List, Dict, Any
import moviepy.editor as me
import requests as rt
import urllib.parse as up
import json as js
import tkinter as tk


class GUI_Requests:
    """
    老狗搜索: 使用酷我音乐进行歌曲爬取\n
    海涛搜索: 使用QQ音乐进行歌曲爬取
    """
    print_GUI: object
    list_sing: List[Dict[str, Any]]

    def __init__(self, GUI_Type=None, master=None, keyword=None):
        """
        :param GUI_Type: Tk-tkinter制作的窗口， qt5-PyQt5制作的窗口
        :param master: 父容器，TK是创建Tk()或Canvas()实例的变量，PyQt5是创建Ui_MainWindow()类实例的变量
        :param keyword: 搜索关键字，可以是歌手也可以是歌曲名等等
        """
        if keyword is None:
            pass
        else:
            keyword = up.quote(keyword)
        self.type = GUI_Type
        self.sc = master
        self.url_ku = 'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(
            keyword)
        referer = 'https://www.kuwo.cn/search/list?key={}'.format(keyword)
        self.download_URLK = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid='
        self.head_ku = {
            'Cookie': '_ga=GA1.2.337131840.1656857132; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1656857131,1658635516; _gid=GA1.2.992504106.1658635516; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1658636222; kw_token=KUUKU45TJK',
            'csrf': 'KUUKU45TJK',
            'Referer': '{}'.format(referer),
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        }

    def 老狗搜索(self, 组件类型: str = None, ID号: QtWidgets = None, tk_pos: tuple = None):
        """
        :param 组件类型: label-标签，comboBox-pyqt5独有-下拉条，canvas.text-tk独有-画板文字输出。
        :param ID号: 如果是tk做的，就无须填这个参数，如果是PyQt5做的，就必须填要输出的组件对象，ID的格式为master.组件对象名，master和上面的父容器的master一样。
        :param tk_pos: tk组件必须给出坐标才能显示输出，pyqt5不加,使用qt设计师(qt designer)提前放置组件省去坐标之苦
        :return: 歌曲的链接
        """
        rq = rt.get(url=self.url_ku, headers=self.head_ku)
        try:
            list2 = js.loads(rq.text)["data"]["list"]
            list_sing = []
            for i in list2:
                list_sing.append({"歌曲名": i['name'], "歌手": i['artist'], "rid识别号": i['rid']})
            if self.type == "Tk":
                if 组件类型 == 'label':
                    self.print_GUI = tk.Label(self.sc, text=(a + "\n" for a in list_sing))
                    self.print_GUI.place(x=tk_pos[0], y=tk_pos[1])
                elif 组件类型 == "canvas.text":
                    self.print_GUI = self.sc.create_text(tk_pos[0], tk_pos[1], text=(a + "\n" for a in list_sing))
                else:
                    print(f'抱歉，老兄无能为力在组件{组件类型}上输出内容')

            elif self.type == 'qt5':
                if 组件类型 == "label":
                    g = ""
                    for ii in list_sing:
                        g += str(ii) + "\n"
                    ID号.setText(g)
                elif 组件类型 == "comboBox":
                    if len(list_sing) != 0:
                        ID号.clear()
                        for ii in list_sing:
                            ID号.addItem(ii['歌曲名'] + '-' + ii['歌手'] + '.mp3')
                    else:
                        ID号.clear()
                        ID号.addItem("无结果")
                else:
                    print(f'抱歉，老兄无能为力在组件{组件类型}上输出内容')
            return list_sing
        except KeyError:
            if self.type == 'qt5':
                if 组件类型 == "comboBox":
                    ID号.clear()
                    ID号.addItem("关键词无效", 0)
            elif self.type == "Tk":
                if 组件类型 == 'label':
                    self.print_GUI = tk.Label(self.sc, text="无效关键词")
                    self.print_GUI.place(x=tk_pos[0], y=tk_pos[1])
                elif 组件类型 == "canvas.text":
                    self.print_GUI = self.sc.create_text(tk_pos[0], tk_pos[1], text="无效关键词")
            else:
                return "无效关键词"

    def 海涛搜索(self):
        """正在制作中"""
        pass

    def download(self, 搜索引擎=None, rid=None, 歌曲名字=None, Qt进度条: QtWidgets.QProgressBar = None, 进度条使用=True,
                 mv_Music: bool = False, print2: QtWidgets.QLabel = None):
        """
        :param print2: 输出标签
        :param mv_Music:  视频提声
        :param 进度条使用: 使不使用进度条显示下载进度
        :param Qt进度条: Qt如果有进度条可以选择
        :param 歌曲名字: 给你要的歌曲取个名字
        :param 搜索引擎: 老狗-使用老狗搜索爬取歌曲，海涛-使用海涛搜索爬取歌曲
        :param rid: 歌曲的rid(id)号，国内各大音乐平台(酷我、酷狗、网易云、 QQ音乐等)通用
        :return:歌曲文件
        """
        if 搜索引擎 == "老狗":
            p = js.loads(rt.get(url=f"{self.download_URLK}{rid}", headers=self.head_ku).text)
            if p["msg"] == "该歌曲为付费内容，请下载酷我音乐客户端后付费收听" or mv_Music:
                p = js.loads(rt.get(url=f"{self.download_URLK}{rid}&type=mv", headers=self.head_ku).text)
                mv_Music = True
            if p['msg'] == '该歌曲已下线':
                print2.setText("歌曲没了")
            else:
                try:
                    p = p['data']['url']
                    GG = rt.get(url=p, headers=self.head_ku, stream=True)
                    if 进度条使用:
                        Qt进度条.show()
                        Qt进度条.setMaximum(int(GG.headers.get('content-length', 0)))
                    if not mv_Music:
                        with open(歌曲名字, 'wb') as file:
                            d = 0
                            for data in GG.iter_content(chunk_size=1024):
                                d1 = file.write(data)
                                d += d1
                                if 进度条使用:
                                    Qt进度条.setValue(d)
                            if 进度条使用:
                                Qt进度条.hide()
                    else:
                        with open(歌曲名字[:-4]+".mp4", 'wb') as file:
                            d = 0
                            for data in GG.iter_content(chunk_size=1024):
                                d1 = file.write(data)
                                d += d1
                                if 进度条使用:
                                    Qt进度条.setValue(d)
                            if 进度条使用:
                                Qt进度条.hide()
                        print(歌曲名字[:-4]+".mp4")
                        ad = me.VideoFileClip(歌曲名字[:-4]+".mp4")
                        au = ad.audio
                        au.write_audiofile(歌曲名字[:-4]+".mp3")  # 保存音乐
                        ad.close()
                except Exception as e:
                    print(e)
        elif 搜索引擎 == '海涛':
            pass
        else:
            print('搜索引擎无效')


if __name__ == "__main__":
    print(GUI_Requests(keyword="小三").老狗搜索())
