"""---------------------------少儿Python编程简易教程，包教不包会，少儿写的教程你应该能理解明白-----------------------------------"""

# 引入模块
import os


# 此教程会展示一些代码的用法注释都写了
# 别只局限于此，你可以自己试着去CSDN，Github找找教程学习一波
# 如果要运行示例请在最后一行按规定操作来运行

# 1.代码基础1
def Zhao_JK_buy_Chicken():
    # 穷举法教程
    print("原始版本")
    for x in range(int(100 / 5)):
        for y in range(int(100 / 3)):
            for z in range(int(100 / (1 / 3))):
                if x + y + z == 100 and 5 * x + 3 * y + (1 / 3) * z == 100:
                    print("赵靖凯可以买%d只公鸡,%d只母鸡,%d只小鸡" % (x, y, z))

    # 改良版本1
    def 赵靖凯买鸡(rangex, rangey, rangez):
        for x in range(rangex):
            for y in range(rangey):
                for z in range(rangez):
                    if x + y + z == 100 and 5 * x + 3 * y + (1 / 3) * z == 100:
                        print("赵靖凯可以买%d只公鸡,%d只母鸡,%d只小鸡" % (x, y, z))

    赵靖凯买鸡(20, int(100 / 3), 300)


# 2.表格读写分析
def xlrd和xlwt教程():
    # xlrd,xlwt的简易用法
    import xlrd
    import xlwt

    '''xlwt'''  # '''xxx'''也是注释
    workbook = xlwt.Workbook()  # 创建新excel工作簿
    sheet1 = workbook.add_sheet("sheet1", cell_overwrite_ok=True)  # 创建新表格
    sheet1.write(0, 0, "赵靖凯买了114514只母鸡")  # 在A,1写入success
    sheet1.write(0, 1, "赵靖凯买了191200只公鸡")  # A,2
    sheet1.write(1, 0, "赵靖凯买了24只小鸡")  # B,1
    workbook.save("test.xls")  # 保存为.xls（Excel文件）

    '''xlrd'''
    data = xlrd.open_workbook("test.xls")  # 打开文件
    tabel = data.sheets()[0]  # 打卡列表1
    row = tabel.row_values(0)  # 获取第1行所有数据
    col = tabel.col_values(0)  # 获取第一列所有数据
    print(row, col)
    for i in row:  # 遍历输出
        print("行" + i)
    for i in col:
        print("列" + i)
    print(tabel.cell_value(0, 0))  # 获取指定位置的数据并输出
    print(tabel.cell_value(0, 1))
    print(tabel.cell_value(1, 0))


# 3.爬虫简单教程
def 爬虫教程():
    import requests as rs
    from bs4 import BeautifulSoup

    # 请求(获取信息)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.87.400 QQBrowser/10.9.4613.400"}
    # 请求头也就是浏览器型号,现在是伪装成qq浏览器爬进去，有时爬虫必须要伪装成浏览器才爬的进去
    url = "https://wall.alphacoders.com/by_collection.php?id=47&lang=Chinese"  # url 网址
    res = rs.get(url=url, headers=header)  # 向网站发送申请，获取其信息(url网站地址，heads请求头)

    # 解析(分析信息)
    m = BeautifulSoup(res.text, "html.parser")  # 建立解析对象(res.text 上面网页的代码),解析方式为html.parser(自带的)
    x = m.find_all("img")  # 寻找所有img标签，返回列表
    pict = []  # 存图片地址用的
    for i in x:
        m = i.get('src')  # 获取每一个img标签的src属性值也就是图片地址
        if m is not None:  # 最后一个img什么也没有不要
            pict.append(m)  # 将地址添加进列表

    # 下载(保存信息)
    for s in pict:  # 只要有http地址的都可以发送请求获取数据，网页里的图片也一样
        if ".jpg" in s:  # 判断图片格式防止文件错误，下面的if也是一样
            com = rs.get(url=s, headers=header)  # 获取图片数据，方式和上面的rs.get一样
            shuju = com.content  # 获取图片的二进制数据
            print("数据大小" + str(len(shuju) / 1024 / 1024) + "MB")  # 检测文件大小
            with open("pictor" + str(len(s)) + ".jpg", "wb") as f:  # 建立一个文件，以二进制方式写入(w写入，b二进制)，下面也一样
                f.write(shuju)  # 将数据写入文件
                print("完成")
            # 用with打开创建的文件就不用close关闭文件了，直接用open的话要用close关闭文件防止文件损坏
            # 不用with
            # x=open("文件名.后缀名","写入方式(w只写，r只读,a读写，a+追加读写也就是续写，前面的字母后面加b代表以二进制写入)")
            # x.read()读取文件
            # x.write()写入文件
            # x,close()关闭文件
        if ".png" in s:
            com = rs.get(url=s, headers=header)
            shuju = com.content
            print("数据大小" + str(len(shuju) / 1024 / 1024) + "MB")
            with open("picture" + str(len(s)) + ".png", "wb") as f:
                f.write(shuju)
                print("完成")


# 4.代码基础2
def 基础1():
    """输入输出和基本类型"""
    print()  # 在控制台输出字符
    input()  # 从用户输入中获取数据，默认返回字符str
    int()  # 将数字字符转化为int(整形)类型
    float()  # 将int转化为小数(浮点数float)
    str()  # 将其他数据转换为字符
    bool()  # 将其他数据转化为布尔类型(bool)
    complex(real=0, imag=1)  # 复数类型
    a = 0  # 定义变量a，将0(int)赋值给它


def 基础2():
    """
       基本运算
        1.加减乘除
        2.且，或，与非
        3.位运算(二进制)
       三大结构
        1.顺序
        2.选择
        3.循环
        4.复合示例
    """

    """基本运算"""
    a = 3
    b = 5
    c = a + b  # 当变量均为整型时，将变量的值相加得到它们的和并返回这个和
    c = str(a) + str(b)  # 当变量均为字符时，它代表将变量里的字符按你给的顺序连接起来，例如"dd"+"jk"="ddjk"
    c = a - b  # 和加法运算的规则一样只是两个变量相减(减法只有整型浮点型有)
    c = str(a) * int(b)  # 乘法运算，c=5个字符3['33333']
    c = a * b  # 数字乘除运算你认得的，唯一不同的是整数/整数=浮点数
    """--未完待续--"""


# 5.简单多线程
def 多线程():
    import threading as th
    import time
    def k(**kwargs):
        print(th.current_thread().name, th.current_thread().is_alive(), kwargs)

    # 访问线程本身,name访问其名字（或者变量.属性也行)
    # is-alive访问该线程是否在执行代码(活着)
    a = th.Thread(target=k, name="线程1", args="孙子", kwargs={"a": 5, 's': 33})  # 建立一个线程
    a.start()  # 开始线程a
    a.join()  # 等该线程完成


# 6.数据统计
def 电脑统计基础():
    """此处教你如何做一个统计图表"""
    # 语法高亮在pycharm起到解释函数功能的作用
    import matplotlib.pyplot as plt
    a = [i for i in range(51)]  # 列表生成式
    y = [i for i in range(0, 101, 2)]
    print(a)
    fig = plt.figure("统计图")  # 建立一个画板,画画没有画板怎么画
    plt.title("001")
    a1 = plt.subplot(2, 1, 1)  # 建立一个画布，就像画函数图像要有纸一样
    plt.plot(a, y)  # 绘制散点图,plot折线图,scatter散点图,bar柱状图
    plt.show()  # 显示


# 7.简单伪随机
def random(次数=0):
    from random import randint
    a = []
    b = []
    y = []
    for i in range(次数 + 1):
        f = randint(0, 1)
        if f == 1:
            a.append(f)
        else:
            b.append(f)
        y.append(i)
    print("计算机模拟概率机制测试,共模拟:" + str(次数) + "次")
    print("P(1)=", len(a) / len(y))


# 8.turtle的高阶用法----放蔡徐坤打篮球
def 鸡你太美():
    """此处教你在turtle上画蔡徐坤打篮球,内存容易爆注意着点"""
    import turtle
    import playsound
    import threading as th
    from pygame import time  # 这个可以不要
    turtle.screensize(1280, 720)
    fps = time.Clock()  # 控制帧数的函数

    def aa():
        playsound.playsound("./鸡你太美/鸡你太美.mp3")

    a = th.Thread(target=aa)  # 开了个子线程，多线程上面有
    a.setDaemon(True)  # 守护模式，主线程没了子线程也会没
    a.start()
    f = 0

    while True:
        fps.tick(30)
        try:
            f += 1
            image = f"./鸡你太美/鸡你太美/image{f}.gif"
            turtle.addshape(image)  # 将图片添加进turtle中，每添加一个你内存剩余量就会越少，内存就是在这爆的
            turtle.shape(image)  # 将图片画出来，现在就是画giegie
        except:
            break


# 9.函数的定义与调用
def 函数名(参数1=None):  # 括号里的东西叫过形式参数，简称形参
    """函数定义与调用
    参数1=None代表这个参数默认值为None,也就是什么也没有"""
    pass  # 跳过，斗地主的过和他很像
    """
        函数里要施行的代码
    """
    return 参数1 + 666  # 函数返回(参数1+666)的值,每个函数执行完后可能要给你一个结果，这个结果就叫返回值


# 10.爬虫进阶----白嫖歌曲
def 偷歌的嘎子(歌名=None, 歌手: str = "我自己", 储存路径=None):
    """此处教你爬取付费下载的歌曲，没钱下歌只能靠技术了呗！但付费才给放的歌暂时爬不下来抱歉，爬到了可能会去坐牢吧."""
    import requests as re
    import json as 加瓦
    from urllib import parse
    import moviepy.editor as mp
    from pygame import mixer
    from os import remove
    mixer.init()
    搜索歌曲名字 = 歌名  # 用户输入，基础语法必须会
    keyword = parse.quote(搜索歌曲名字)  # 使用quote()方法，对输入的字符串进行编码
    url = 'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1'.format(keyword)
    referer = 'https://www.kuwo.cn/search/list?key={}'.format(keyword)
    请求头 = {
        'Cookie': '_ga=GA1.2.337131840.1656857132; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1656857131,1658635516; _gid=GA1.2.992504106.1658635516; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1658636222; kw_token=KUUKU45TJK',
        'csrf': 'KUUKU45TJK',
        'Referer': '{}'.format(referer),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    }  # 这个必须有不让进不去
    a = re.get(url=url, headers=请求头)  # 开爬！
    list2 = 加瓦.loads(a.text)["data"]["list"]  # 它的数据是json格式,先解析一下(loads放数据,load放文件)
    歌曲列表1 = []  # 存储所以歌曲的数据
    结果 = []  # 存储用户想要的歌曲数据
    for name in list2:
        歌曲列表1.append({"歌曲名": name['name'], "歌手": name['artist'], "rid识别号": name['rid']})  # 爬数据
        if name['artist'] == 歌手:
            结果.append({"歌曲名": name['name'], "歌手": name['artist'], "rid识别号": name['rid']})
        else:
            pass
    if 歌手 == "":
        结果 = 歌曲列表1
    print("搜索列表")
    for jk in 结果:
        print(jk["歌曲名"], jk["歌手"])  # 找到数据中的歌曲文件地址，把他下载到本地
    g = int(input("放哪首(标号)"))
    try:
        b = re.get(f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={结果[g - 1]["rid识别号"]}&type=mv', headers=请求头)
        print(加瓦.loads(b.text))
        歌曲文件 = 加瓦.loads(b.text)['data']['url']
        歌曲 = re.get(歌曲文件, headers=请求头)  # 下载
        with open("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp4", "wb") as f:
            f.write(歌曲.content)
        ad = mp.VideoFileClip("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp4")  # 打开视频文件
        au = ad.audio  # 提取音频
        au.write_audiofile("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp3")  # 保存音乐
        ad.close()
        remove("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp4")  # 删除文件
        mixer.music.load("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pass
    except:
        print("这首歌没有MV")
        b = re.get(f'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={结果[g - 1]["rid识别号"]}', headers=请求头)
        print(加瓦.loads(b.text))
        歌曲文件 = 加瓦.loads(b.text)['data']['url']
        歌曲 = re.get(歌曲文件, headers=请求头)  # 下载
        with open("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp3", "wb") as f:
            f.write(歌曲.content)
        mixer.music.load("./歌曲/" + 结果[g - 1]["歌曲名"] + "----" + 结果[g - 1]["歌手"] + ".mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            pass


# 11.系统操作os,sys和Dos_cmd指令/python[类]操作
class 启动器(object):  # 创建 启动器 类，object是所有类的子类，也可以--->class 启动器:
    """此处叫你做一个简易的启动器来启动应用"""

    def __init__(self,  # 类中定义的函数第一个参数不能带默认值和星号
                 file="E:\\Genshin Impact\\Genshin Impact Game\\YuanShen.exe"):  # 构造函数__init__,里面放这个类需要的变量和值，这些变量在类中叫做属性
        self.file = file  # 所有属性都要以第一个参数开头,格式为===>第一个参数名字.变量名 = ？？？

    @staticmethod  # 装饰器,留着以后讲,这里装饰器的作用是构造静态函数
    def 启动():  # 在类创建后能自动运行的类中函数叫构造函数,其余的类中函数叫做方法，需要调用才会运行
        print("已启动蕉神")

    def __启动__(self):
        os.startfile(self.file)  # os.startfile打开某个文件


class 原神专属启动器(启动器):  # 创建 原神专属启动器 类，并让其继承 启动器 类，被继承的类叫做父类，此时你定义的叫做被继承类的父类
    """此处在启动器的基础上做一个专门启动原神的启动器"""

    def __init__(self):
        super().__init__()  # 继承父类的属性


# 12.开自瞄----pyautogui简易教程
def 自动点击():
    import pyautogui as g
    m = g.size()  # 获取屏幕大小
    print(m)
    g.moveTo(m[0] / 2, m[1] / 2)  # 鼠标移动到(x,y)处,屏幕左上角为(0,0)
    print(g.position())  # 获取鼠标位置
    g.click(200, 200, 2, button="left")  # 移动鼠标到(200,200),并用左键点击两次


# 实例区
p = 函数名(654)  # 函数调用,调用时给的值叫做实际参数，简称实参，让变量p=此函数的返回值
print(p)
原神专属启动器().启动()  # 类的调用
自动点击()
