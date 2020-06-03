import random, time
from interface.fast3gametown import *


def hhhmenthod(driver):
    for i in range(10):
        r = random.randrange(3, 19)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='%d']" % r).click()
    time.sleep(2)


def dxds(driver):
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[0].click()
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[1].click()
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[2].click()
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[3].click()


def s3g(driver):
    driver.find_element_by_id("com.yy.sport:id/tv_ball").click()


def s3s(driver):
    r = random.choice(["com.yy.sport:id/tv_menu_all", "com.yy.sport:id/tv_menu_da", "com.yy.sport:id/tv_menu_xiao",
                       "com.yy.sport:id/tv_menu_ji", "com.yy.sport:id/tv_menu_ou"])

    driver.find_element_by_id("%s" % r).click()


def d3dt(driver):
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.view.View[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.view.View["
                                 "1]/android.widget.RelativeLayout[%s]/android.view.View["
                                 "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % 2).click()

    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.view.View[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.view.View["
                                 "1]/android.widget.RelativeLayout[%s]/android.view.View["
                                 "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % 5).click()
    driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
        "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
        "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
        "1]/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
        "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout["
        "1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.RelativeLayout["
        "2]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.RelativeLayout[%s]/android.view.View["
        "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % 3).click()


# 对于12个元素在同一frame下的胆码1拖码2的不重复选择
def d2td(driver):
    total = driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    print(len(total))
    r = random.choice([0, 2, 4])
    total[r].click()
    for i in range(2):
        r1 = random.choice([7, 9, 11])
        total[r1].click()
        time.sleep(1)


def gametownchossenum(driver):
    # 玩法名
    play_name_1 = list(page1.keys())[0]
    # 数字名 后期可升级为自动获取
    playn_umber_1 = list(page1['和值'].keys())[0]
    # 路径
    h3 = driver.find_element_by_xpath(page1['和值']['3']).click()
    h4 = driver.find_element_by_xpath(page1['和值']['4']).click()
    h7 = driver.find_element_by_xpath(page1['和值']['7']).click()
    h9 = driver.find_element_by_xpath(page1['和值']['9']).click()
    h12 = driver.find_element_by_xpath(page1['和值']['12']).click()
    h15 = driver.find_element_by_xpath(page1['和值']['15']).click()
    play_name_2 = list(page1.keys())[1]
    play_number_2 = list(page1['和值大小单双'].keys())[0]
    driver.find_element_by_xpath(page1['和值大小单双']['大']).click()
    driver.find_element_by_xpath(page1['和值大小单双']['单']).click()

    return {play_name_1: ['3','4','7','9','12','15'], play_name_2: ['大', '单']}

    # 随机下注方式
    # listofelpage=driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    # print(len(listofelpage))
    #
    # for i in range(len(listofelpage)-10):
    #    listc=['大','小','单','双',3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    #    r=random.choice(listc)
    #    driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='%s']"%r).click()


def gametownchooseserial1(driver):
    driver.find_element_by_xpath(page2['两连']['12']).click()
    driver.find_element_by_xpath(page2['两连']['16']).click()
    driver.find_element_by_xpath(page2['两连']['23']).click()
    driver.find_element_by_xpath(page2['两连']['26']).click()

    driver.find_element_by_xpath(page2['独胆']['1']).click()
    driver.find_element_by_xpath(page2['独胆']['3']).click()
    driver.find_element_by_xpath(page2['独胆']['4']).click()
    return {'两连': ['12', '16', '23', '26'], '独胆': ['1', '3', '4']}

    # 页面元素总数
    # listofelpage = driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    # print(len(listofelpage))
    # for i in range(len(listofelpage) - 10):
    #     r = random.randrange(18)
    #     listofelpage[r].click()


def gametownchooseserial2(driver):
    driver.find_element_by_xpath(page3['对子']['1']).click()
    driver.find_element_by_xpath(page3['对子']['2']).click()
    driver.find_element_by_xpath(page3['对子']['5']).click()
    driver.find_element_by_xpath(page3['对子']['6']).click()

    driver.find_element_by_xpath(page3['豹子']['1']).click()
    driver.find_element_by_xpath(page3['豹子']['2']).click()
    driver.find_element_by_xpath(page3['豹子']['3']).click()
    driver.find_element_by_xpath(page3['豹子']['任意豹子']).click()
    return {"对子": ['1', '2', '5', '6'], "豹子": ['1', '2', '3', '任意豹子']}

    # # 页面元素总数
    # listofelpage = driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    # print(len(listofelpage))
    # for i in range(len(listofelpage)):
    #     r = random.randrange(len(listofelpage))
    #     listofelpage[r].click()


def Splitter(dict_j):
    listbaozi = []
    listduizi = []
    listdudan = []
    listlianglian=[]
    listhezhidanxiaodanshuang = []
    listhezhi = []
    dict_v = {"豹子": listbaozi, '对子': listduizi, '两连': listlianglian, '独胆': listdudan, '和值大小单双': listhezhidanxiaodanshuang,
              '和值': listhezhi}
    dict_j = [{'豹子': '任意豹子'}, {'豹子': '3'}, {'豹子': '2'}, {'豹子': '1'}, {'对子': '6'}, {'对子': '5'}, {'对子': '2'},
              {'对子': '1'}, {'独胆': '4'}, {'独胆': '3'}, {'独胆': '1'}, {'两连': '26'}, {'两连': '23'}, {'两连': '16'},
              {'两连': '12'}, {'和值大小单双': '单'}, {'和值大小单双': '大'}, {'和值': '15'}, {'和值': '12'}, {'和值': '9'}, {'和值': '7'},
              {'和值': '4'}, {'和值': '3'}]
    for i in dict_j:
        if list(i.keys())[0] == '豹子':
            listbaozi.append(i['豹子'])

        elif list(i.keys())[0] == '对子':
            listduizi.append((i['对子']))

        elif list(i.keys())[0] == "独胆":
            listdudan.append(i['独胆'])

        elif list(i.keys())[0] == '两连':
            listlianglian.append(i['两连'])

        elif list(i.keys())[0] == '和值大小单双':
            listhezhidanxiaodanshuang.append(i['和值大小单双'])

        elif list(i.keys())[0] == '和值':
            listhezhi.append(i['和值'])

    return dict_v
