from UItest import entergame
import random, time
from UItest.game import D3, fast3, elevewithinfive, pk10, timetimehappy, marksix
from UItest.game.fast3 import hezhi_play, SBSSDchoosenum, same3general, same3single, diff3, diff3tuo, \
    Consecutive3general, same2repeat, same2single, diff2, diff2tuo
from Utility.judge import assert_equal_el

now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))


def randomchoose(androidC):
    driver = entergame.Entrance(androidB=androidC)
    listmodel = [1, 2]
    i = random.choice(listmodel)
    if i == 1:
        # 随机选择的游戏
        listgametype = driver.find_elements_by_id("com.yy.sport:id/lottery_more_img_1")
        print(len(listgametype))
        listgametype[random.randrange(len(listgametype))].find_element_by_id(
            'com.yy.sport:id/lottery_more_img_1').click()
        # 随机选择的端口
        listgameport = driver.find_elements_by_id("com.yy.sport:id/item_text_view")
        j = random.randrange(len(listgameport))
        listgameport[j].find_element_by_id("com.yy.sport:id/item_text_view").click()
        time.sleep(2)
        # 判断进入了哪个游戏
        gamename = driver.find_element_by_id("com.yy.sport:id/tv_num_desc").text
        print(gamename)
        if "VR金星" or "分分彩" or "新疆" or "M6-3" or "河内" or "腾讯" or "3.5分" or "M6-5" or "重庆" in gamename:
            timetimehappy.tthappy(driver)
        if "福彩3D" or "M6-3D" or "M6-3D分分彩" or "M6-3D5" or "排列三" or "M6-3D10" in gamename:
            D3.game3D(driver)
        if "安徽快三" or "湖北快三" or "M6-1分快三" or "M6-5分快三" or "M6-3分快三" or "江苏快三" or "北京快三" in gamename:
            fast3.enterfast3(driver)

    else:
        # 随机选择的游戏
        list2 = driver.find_elements_by_id("com.yy.sport:id/lottery_more_img_2")
        list2[random.randrange(len(list2))].find_element_by_id('com.yy.sport:id/lottery_more_img_2').click()
        # 随机选择的端口
        listgameport = driver.find_elements_by_id("com.yy.sport:id/item_text_view")
        j = random.randrange(len(listgameport))
        listgameport[j].find_element_by_id("com.yy.sport:id/item_text_view").click()
        # 判断进入了哪个游戏
        gamename = driver.find_element_by_id("com.yy.sport:id/tv_num_desc").text
        print(gamename)
        if '11选5' in gamename:
            elevewithinfive.elenwithfive(driver)
        elif "5分急速" or "分分极速" or "北京PK10" or "幸运飞艇" or "3分极速赛车" in gamename:
            pk10.pk10(driver)
        elif "六合彩" or "大乐透" in gamename:
            marksix.sixhappy(driver)


def Choosefastthree(androidC):
    driver = entergame.Entrance(androidB=androidC)
    driver.implicitly_wait(5)

    listgameport = ['安徽快三', '湖北快三']
    listgametype = ['快三']
    #进入快三游戏
    fast3.enterfast3(driver, listgametype[0], listgameport[0])  # 后期可以再升级为循环方式

    listrule = ['和值', '三同号通选', '三同号单选', '三不同号', '三连号通选', '二同号复选', '二同号单选', '二不同号']



    for spe_one in listrule:

        if spe_one == "和值":
            # 和值
            hezhi_play(driver, methodtitle=spe_one)
            # 大小单双
            SBSSDchoosenum(driver, upmethodtitle=spe_one)
            pass
        elif spe_one == '三同号通选':

            same3general(driver,methodtitle=spe_one)
            pass
        elif spe_one == '三同号单选':

            same3single(driver,methodtitle=spe_one)
            pass
        elif spe_one == '三不同号':
             #三不同号
            diff3(driver,methodtitle=spe_one)
            #三不同号拖胆
            diff3tuo(driver)
            pass
        elif spe_one == '三连号通选':
            Consecutive3general(driver)
            pass
        elif spe_one == '二同号复选':
            same2repeat(driver)
            pass
        elif spe_one == '二同号单选':
            same2single(driver)
            pass
        elif spe_one == '二不同号':
            #二不同号
            diff2(driver)
            # 二不同号胆拖
            diff2tuo(driver)
            pass
