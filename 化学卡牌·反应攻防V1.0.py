from tkinter import *
from random import randint as 概率
from pygame import mixer as B
import 更新文件
import time

PG = 0
RG = 0
o = 0
B.init()
dd = False

def END():
    global o
    global KK
    global x
    global RG
    global PG
    list1 = ["赵JK","丁肆","龙狒狒","陈老二","傲娇杰","牛逼哥","栾二蛋"]
    sss = 概率(0,len(list1)-1)
    o = 0
    G = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    KK.destroy()
    g=Tk()
    g.iconbitmap("C:/Users/Administrator/Desktop/程序/LOGO.ico")
    g.geometry("400x200+500+200")
    g.title("化学卡牌·反应攻防--成绩结算")
    Label(g,text=(x+"的成绩:"+str(PG))).place(x=0,y=0)
    Label(g,text=(list1[sss]+"的成绩:"+str(RG))).place(x=0,y=20)
    if PG >= 400:
        Label(g,text="获得成就-- 不敢想象的化学").place(x=0,y=160)
        with open("成就.txt","a+") as f:
            f.write("\n不敢想象的化学---我就是，那道化学的威光......\n"+G+"\n")
    else:
        pass
    if RG >= 400:
        Label(g,text="获得成就--直面大佬").place(x=0,y=180)
        with open("成就.txt","a+") as f:
            f.write("\n直面大佬---总会有地上的菜鸟，敢于直面化学的威光......\n"+G+"\n")
    else:
        pass
    if RG == PG:
        Label(g,text="平手，坚持住！").place(x=0,y=40)
        PG=0
        RG=0
    elif PG > RG:
        Label(g,text="别骄傲，到满分再笑").place(x=0,y=40)
        PG=0
        RG=0
    else:
        Label(g,text="别气馁，下次赢他！").place(x=0,y=40)
        PG=0
        RG=0
    F=Button(g,text="再战这些垃圾/大佬！",command=game)
    F.place(x=0,y=110)
    g.mainloop()


class 化学反应:
    def __init__(self):
        self.盐类 = ["硫酸盐","钡盐","银盐","碳酸盐","钙盐","氯盐","铵盐"]
        self.酸 = ["盐酸","硝酸","硫酸"]
        self.碱 = ["NaOH","Ca(OH)2","KOH","NH3·H2O","Ba(OH)2"]
        self.氧化物 = ["CO2","SO2","Na2O","Na2O2","Fe2O3","H2O"]
        self.单质 = ["Na","Fe","Cu","Cl2","O2","H2"]
    def 反应(self,反应物1=None,反应物2=None,ss=None,name="玄哥"):
        global RG
        global PG
        global o
        global dd
        global x
        x = name
        o += 1
        if 反应物1 == 反应物2 or ((反应物1 in self.盐类) and (反应物2 in self.盐类)) or ((反应物1 in self.酸) and (反应物2 in self.酸)) or ((反应物1 in self.碱) and (反应物2 in self.碱)):
            Label(ss,text="同类物质",font=30,width=50,anchor="w").place(x=0,y=170)
            liebiao = ["music","music2","music3","music4","music5","music6","god_woman_hit_block"]
            R1 = 概率(0,5)
            if dd == False:
                B.music.load("C:\\Users\\Administrator\\Desktop\\程序\\音乐\\"+liebiao[R1]+".mp3")
                B.music.play()
                dd = B.music.get_busy()
            else:
                dd = B.music.get_busy()
                print("now play")
            Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        elif (反应物1 in self.盐类) and (反应物2 in self.盐类):
            Label(ss,text="复分解反应",font=30,width=50,anchor="w").place(x=0,y=150)
            Label(ss,text="先出牌的为防守方",font=30,width=50,anchor="w").place(x=0,y=170)
            if 反应物1 == self.盐类[0] and 反应物2 == self.盐类[1]:
                Label(ss,text="硫酸根遇到钡离子！\n硫酸根离子+钡离子====硫酸钡沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[2] and 反应物2 == self.盐类[5]:
                Label(ss,text="银离子+氯离子====氯化银沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[3] and 反应物2 == self.盐类[4]:
                Label(ss,text="碳酸根离子+钙离子====碳酸钙沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[1] and 反应物2 == self.盐类[0]:
                Label(ss,text="硫酸根遇到钡离子！\n硫酸根离子+钡离子====硫酸钡沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[5] and 反应物2 == self.盐类[2]:
                Label(ss,text="银离子+氯离子====氯化银沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[4] and 反应物2 == self.盐类[3]:
                Label(ss,text="碳酸根离子+钙离子====碳酸钙沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            else:
                Label(ss,text="无现象",font=30,width=50,anchor="w").place(x=0,y=170)
                Label(ss,text=" ",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        elif (反应物1 in self.盐类) and (反应物2 in self.酸):
            Label(ss,text="盐的一方为防守方",font=30,width=50,anchor="w").place(x=0,y=170)
            if 反应物1 == self.盐类[3]:
                Label(ss,text="酸+碳酸根离子====水+二氧化碳气体",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[1] and 反应物2 == self.酸[2]:
                Label(ss,text="硫酸根离子+钡离子====硫酸钡沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物1 == self.盐类[2] and 反应物2 == self.酸[1]:
                Label(ss,text="氯离子+银离子====氯化银沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            else:
                Label(ss,text="无现象",font=30,width=50,anchor="w").place(x=0,y=170)
                Label(ss,text=" ",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        elif (反应物2 in self.盐类) and (反应物1 in self.酸):
            Label(ss,text="盐的一方为防守方",font=30,width=50,anchor="w").place(x=0,y=170)
            if 反应物2 == self.盐类[3]:
                Label(ss,text="酸+碳酸根离子====水+二氧化碳气体",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物2 == self.盐类[1] and 反应物1 == self.酸[2]:
                Label(ss,text="硫酸根离子+钡离子====硫酸钡沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif 反应物2 == self.盐类[2] and 反应物1 == self.酸[1]:
                Label(ss,text="氯离子+银离子====氯化银沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            else:
                Label(ss,text="无现象",font=30,width=50,anchor="w").place(x=0,y=170)
                Label(ss,text=" ",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        elif ((反应物1 in self.酸) and (反应物2 in self.碱)) or ((反应物1 in self.碱) and (反应物2 in self.酸)):
            Label(ss,text="中和反应",font=30,width=50,anchor="w").place(x=0,y=170)
            RG+=5;PG+=5
            Label(ss,text="氢离子+氢氧根离子====水",font=30,width=50,anchor="w").place(x=0,y=200)
            Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        elif (反应物1 in self.碱) and (反应物2 in self.盐类):
            Label(ss,text="碱的一方为防守方",font=30,width=50,anchor="w").place(x=0,y=170)
            if (反应物2 in self.盐类[1]):
                Label(ss,text="钡离子+2氢氧根离子====氢氧化钡",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif (反应物2 in self.盐类[6]) and 反应物1 != self.碱[3]:
                Label(ss,text="氢氧根离子+铵根离子====氨气+水",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif (反应物1 == self.碱[1]) and 反应物2 == self.盐类[3]:
                Label(ss,text="钙离子+碳酸根离子====碳酸钙沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif (反应物1 == self.碱[4]) and 反应物2 == self.盐类[0]:
                Label(ss,text="钡离子+硫酸根离子====硫酸钡沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            else:
                Label(ss,text="无现象",font=30,width=50,anchor="w").place(x=0,y=170)
                Label(ss,text=" ",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        elif (反应物2 in self.碱) and (反应物1 in self.盐类):
            Label(ss,text="碱的一方为防守方",font=30,width=50,anchor="w").place(x=0,y=170)
            if (反应物1 in self.盐类[1]):
                Label(ss,text="钡离子+2氢氧根离子====氢氧化钡",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif (反应物1 in self.盐类[6]) and 反应物2 != self.碱[3]:
                Label(ss,text="氢氧根离子+铵根离子====氨气+水",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif (反应物2 == self.碱[1]) and 反应物1 == self.盐类[3]:
                Label(ss,text="钙离子+碳酸根离子====碳酸钙沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            elif (反应物2 == self.碱[4]) and 反应物1 == self.盐类[0]:
                Label(ss,text="钡离子+硫酸根离子====硫酸钡沉淀",font=30,width=50,anchor="w").place(x=0,y=200)
                PG+=15
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
            else:
                Label(ss,text="无现象",font=30,width=50,anchor="w").place(x=0,y=170)
                Label(ss,text=" ",font=30,width=50,anchor="w").place(x=0,y=200)
                RG+=10
                Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        else:
            Label(ss,text="无此物质",font=30,width=50,anchor="w").place(x=0,y=170)
            Label(ss,text=" ",font=30,width=50,anchor="w").place(x=0,y=200)
            RG+=1;PG-=1
            Label(ss,text=("人机:"+str(RG)+"   "+name+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        if o >= 100:
            END()
        else:
            pass

class VRt_21th(化学反应):
    def __init__(self):
        global entry
        super(化学反应).__init__()
    def kuangkou(self):
        global KK
        global entry
        global entry4
        KK = Tk()
        KK.title("化学反应·反应攻防V0.1—Bate")
        KK.geometry("400x300+500+200")
        KK.iconbitmap("C:/Users/Administrator/Desktop/程序/LOGO.ico")
        Label(KK,text="输入物质名",font=40).place(x=0,y=0)
        entry = Entry(KK)
        entry.place(x=100,y=0)
        Label(KK,text="玩家名",font=40).place(x=0,y=250)
        entry4 = Entry(KK)
        entry4.place(x=60,y=250)
        hh = Button(KK,text="输入",command=FG)
        Label(KK,text=("盐类：",化学反应().盐类)).place(x=0,y=50)
        Label(KK,text=("酸：",化学反应().酸)).place(x=0,y=70)
        Label(KK,text=("碱：",化学反应().碱)).place(x=0,y=90)
        Label(KK,text=("氧化物:",化学反应().氧化物)).place(x=0,y=110)
        Label(KK,text=("单质：",化学反应().单质)).place(x=0,y=130)
        Label(KK,text=("人机:"+str(RG)+"   "+"name"+":"+str(PG)+" 回合"+str(o+1)),font=30,width=50,anchor="w").place(x=0,y=230)
        hh.place(x=360,y=0)
        KK.mainloop()

def FG():
    global KK
    global entry
    global entry2
    global entry4
    entry2 = str(entry.get())
    f = str(entry4.get())
    AM = 化学反应()
    Robot = []
    old = len(Robot)
    if old == 0:
        for i in AM.盐类:
            Robot.append(i)
        for i in AM.酸:
            Robot.append(i)
        for i in AM.碱:
            Robot.append(i)
        for i in AM.氧化物:
            Robot.append(i)
        for i in AM.单质:
            Robot.append(i)
    new = len(Robot)
    entry3 = 概率(0,14)
    AM.反应(反应物1=entry2,反应物2=Robot[entry3],ss=KK,name=f)
    Label(KK,text="人机最后出牌:"+Robot[entry3],width=60,anchor="w").place(x=0,y=270)

def game():
    global JK
    global GM
    global w
    GM = VRt_21th()
    GM.kuangkou()

def ssd():
    dd = 更新文件.更新()

def ddd():
    a = open("成就.txt","r")
    tt = a.read()
    JK = Tk()
    Label(JK,text=tt,anchor="w").pack(side="left",anchor="w")
    a.close()
    JK.mainloop()

w=Tk()
w.iconbitmap("C:/Users/Administrator/Desktop/程序/LOGO.ico")
w.geometry("400x400+500+200")
w.title("化学卡牌·反应攻防")
w.update()
X = w.winfo_width()     #获取窗口大小
Y = w.winfo_height()
w.update()
Label(w,text="化学卡牌·反应攻防",font=("微软雅黑",30,"italic"),fg="#998FFF").place(x=30,y=50)   #italic 斜体
Label(w,text="把化学变成游戏......",font=30).place(x=135,y=180)
A=Button(w,text="STAND",width=5,height=1,command=game).place(x=175,y=210)
YY=Button(w,text="更新公告",command=ssd,bd=0,fg="red").place(x=X/2-25,y=Y-41)
AA=Button(w,text="成就",width=5,height=1,command=ddd).place(x=175,y=250)
BB=Button(w,text="VRt-21th 制作",font=("微软雅黑",10),fg="#00FFFF",command=感谢,bd=0).place(x=X/2-43,y=Y-21)
w.mainloop()
