from UItest import login, entergame, choosegame
from UItest.game import fast3
import os, time


# def starttest():
#     os.popen("appium -a 127.0.0.1")


# 登录
def do_login():
    login.login(androidA=5)


# 进入彩票游戏
def do_entergame():
    entergame.Entrance(androidB=5)


# 随机选择游戏
def do_choosegame():
    #随机选游戏
    choosegame.randomchoose(androidC=5)

#选择快三游戏
def choosefastthree():

    choosegame.Choosefastthree(androidC=5)
#十一选五游戏






if __name__ == '__main__':
    # starttest()
    # do_entergame()
    # choosefastthree()

    for i in range(20):
       try:
        time.sleep(5)
        choosefastthree()
       except:
          # 增加截图功能以抓取android5.1系统闪退的情况
           time.sleep(5)
           choosefastthree()