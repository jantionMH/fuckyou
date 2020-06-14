from appium.webdriver.common.touch_action import TouchAction

from UItest.gamementhod.hhh import gametownchossenum
from Utility.judge import assert_equal_el, assert_more_than, assert_not_null
from time import sleep
import time, random


def switcho_e(driver):
    try:
        # 娱乐城阴影两点
        # shadowcilckgametown(driver)
        # 切换到官方玩法
        rightconer(driver)
        # 切换到官方玩法
        office_play(driver)
        # 阴影三点
        shadowcilck(driver)
    except:
        pass


# 玩法选项打开
def ruleoption(driver):
    driver.find_element_by_xpath("//android.widget.TextView[@text='和值-和值-和值']").click()


# 阴影三点
def shadowcilck(driver):
    try:
        driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
        sleep(1)
        driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
        sleep(1)
        driver.find_element_by_xpath("//android.widget.RelativeLayout").click()


    except:
        print("无阴影可点")


def shadowcilckgametown(driver):
    try:
        driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
        sleep(1)
        driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
        driver.find_element_by_xpath("//android.widget.RelativeLayout").click()


    except:
        print("无阴影可点")


# 加倍
def add_double(driver):
    driver.find_element_by_xpath("//android.widget.TextView[@text='十']").click()


# 一键投注,点击确认,返回两个金额
def Oneclickbetting(driver, methodtitle):
    # 一键投注点击
    driver.find_element_by_xpath(
        "//android.widget.Button[@resource-id='com.yy.sport:id/btn_bet' and @text='一键投注']").click()
    # 获取当前余额
    sleep(1)
    A_beforebalance = driver.find_element_by_id("com.yy.sport:id/tv_account_balance").text
    before = A_beforebalance.replace(",", "")
    newbefore = before.split('.')[0] + '.' + before.split('.')[1][:2]
    print("下注前账户金额：%s" % A_beforebalance)
    # 获取下注额
    B_betnum = driver.find_element_by_id("com.yy.sport:id/tv_amount").text
    b_betnum = B_betnum.replace(",", "")
    print("下注的金额%s" % b_betnum)

    # 断言:确认提示框出现表明一键投注功能可用
    subtitle = driver.find_element_by_id("com.yy.sport:id/cb_select").text
    assert_equal_el(driver, expect='本次后不再进行确认提示', actual=subtitle, case='一键投注', scenes='玩法:%s' % methodtitle)
    # 点击确定
    sleep(2)
    driver.find_element_by_id("com.yy.sport:id/btn_sure").click()

    return [newbefore, b_betnum]


# 返回上级并转到我的金额页面
def returntopage(driver, rule):
    # 返回上级页面，验证金额,点击返回箭头
    try:
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                     "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                     "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                     "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout["
                                     "1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
    except:
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + '玩法:%s' % rule + ',' + "返回上层验证金额" + ',' + result + ',' + filename + ',' + '返回上级箭头点击失效' + '\n')
    time.sleep(1)
    # 找到我的
    driver.find_elements_by_id("com.yy.sport:id/smallLabel")[4].click()


def currentbalance(driver):
    currentbalance = driver.find_element_by_id("com.yy.sport:id/iv_user_balance").text

    newcurrent = currentbalance.replace(",", "")
    print("当前金额", newcurrent)
    return newcurrent


# 从我的金额返回到投注页面
def rollbackC(driver, gametype, gameport):
    driver.find_elements_by_id("com.yy.sport:id/icon")[1].click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/more_title_text_1' and @text='%s']" % gametype).click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/item_text_view' and @text='%s']" % gameport).click()


# 添加注单
def addbetpageC(driver, methodtitle):
    driver.find_element_by_id("com.yy.sport:id/btn_add").click()
    time.sleep(2)
    text = driver.find_element_by_xpath("//android.widget.TextView[@text='投注单']").text
    assert_equal_el(driver, expect='投注单', actual=text, case="添加注单", scenes="玩法:%s" % methodtitle)


def add5bet(driver, methodtitle):
    # 增加5注
    driver.find_element_by_id("com.yy.sport:id/tv_random_5").click()
    # 投注数量
    betnum = driver.find_element_by_id("com.yy.sport:id/tv_betNum").text
    assert_more_than(driver, expect=4, actual=int(betnum), scenes="玩法:%s" % methodtitle, case="随机添加5注")


def addbet_comfire(driver, methodtitle):
    # 下注按钮
    driver.find_element_by_id("com.yy.sport:id/btn_bet").click()
    time.sleep(2)
    # 获取信息
    beforebalance = driver.find_element_by_id("com.yy.sport:id/tv_account_balance").text
    before = beforebalance.replace(",", "")
    newbefore = before.split('.')[0] + '.' + before.split('.')[1][:2]
    betnum = driver.find_element_by_id("com.yy.sport:id/tv_amount").text
    time.sleep(2)
    # 确认按钮
    driver.find_element_by_id("com.yy.sport:id/btn_sure").click()
    time.sleep(1)
    # 断言:下注可用,点击确认后返回的添加注单页面
    extitle = driver.find_element_by_id("com.yy.sport:id/tv_play").text
    assert_equal_el(driver, expect="玩法", actual=extitle, case="添加注单下注", scenes="玩法:%s" % methodtitle)
    time.sleep(1)

    return [newbefore, betnum]


def isin_gametown(driver):
    try:
        driver.find_element_by_class_name("android.widget.TextView").text == '整合'


    except:
        officeswitchtogametown(driver)


def officeswitchtogametown(driver):
    # 点击右上角...按钮
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.yy.sport:id/iv_right_menu']").click()
    sleep(1)
    # 点击娱乐城玩法按钮
    driver.find_element_by_id("com.yy.sport:id/rb_play_happy").click()
    sleep(1)
    # 获取断言要素
    title = driver.find_element_by_xpath("//android.widget.TextView[@text='整合']").text
    assert_equal_el(driver, expect="整合", actual=title, case="到达娱乐城页面", scenes="进入快三娱乐")

    # 获取断言需要的页面元素
    titlenum = driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='9']").text
    assert_equal_el(driver, expect="9", actual=titlenum, case="出现投注号码", scenes="进入快三娱乐城")


def fast3_unitprice(driver):
    # 注数
    n = driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]").text
    # 点开单价器页面
    driver.find_element_by_id("com.yy.sport:id/et_input_recreation_multiple").click()

    return n


def stratge_max_bets(driver, n):
    r = int(44444 / int(n))
    l = len(str(r))
    for i in range(l):
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_number' and @text='%s']" % str(r)[i]).click()


def strage_min_bets(driver):
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_number' and @text='5']").click()


def pageamount(driver):
    bets = driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[2]").text
    toatl = driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.TextView[4]").text
    uprice = driver.find_element_by_id("com.yy.sport:id/et_input_recreation_multiple").text
    mprice = int(bets) * int(uprice)
    newtotal = toatl.replace(",", "")
    assert_equal_el(driver, expect=int(newtotal), actual=int(mprice), scenes="娱乐城玩法", case="投注前页面总金额校验")
    # 返回下注的数量
    return bets


def gain_lottey_phase(driver):
    ph = driver.find_element_by_id("com.yy.sport:id/tv_next_code").text
    return ph


# 右上角按钮
def rightconer(driver):
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.yy.sport:id/iv_right_menu']").click()


# 切换官方玩法
def office_play(driver):
    driver.find_element_by_id("com.yy.sport:id/rb_play_official").click()
    # 随便一点，消除菜单
    TouchAction(driver).tap(x=700, y=1000).perform()


def page_betreocrd(driver):
    driver.find_element_by_id("com.yy.sport:id/tv_bet_record").click()


def verify_betreocrd(driver):
    # 注记录页面
    driver.find_element_by_xpath("//android.widget.TextView[@text='投注记录']").click()
    # 取投‘注记录字’样断言
    title = driver.find_element_by_id("com.yy.sport:id/mToolbarTitleLabel").text
    assert_equal_el(driver, expect='投注记录', actual=title, case='进入投注页面', scenes='玩法:快三娱乐城')


def totalphasepage_1(driver, p, b):
    """
    p：奖期号码 用于控制循环进行的条件
    b:下注数量 用于控制循环退出的条件
    """
    global play_name

    list_1 = []

    listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
    # 当前页面的所有玩法和所有下注号码
    play_number_1 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
    play_name_1 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
    # print("奖期列表长度",len(listnum))
    # print("玩法明列表长度",len(listnum))
    # print("玩法号码列表长度",len(listnum))
    print("当前的期数号码是：%s" % p)

    j = 0
    # 循环奖期列表
    for i in range(len(listnum)):
        # 分支过滤出符合条件的列表元素
        if listnum[i].text == ('第' + p + '期'):
            # 每次循环开始都初始化字典/把该分支下的玩法和下注内容编入字典
            dict_1 = {play_name_1[i].text: play_number_1[i].text}
            # 添加到全局的列表
            list_1.append(dict_1)
            # 符合的数目就自加1
            j += 1
            # 如果达到了投注数量就表明循环可以单方面停止，交给下一步去判断内同是否正确
            if j == int(b):
                break
        elif listnum[i].text != ('第' + p + '期'):
            break

    if j == 5:
        # 下拉整个屏幕
        # driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)

        play_number_2 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_2 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_2 = {}
                dict_2[play_name_2[i].text] = play_number_2[i].text
                list_1.append(dict_2)
                if j == int(b):
                    break

    if j == 10:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        sleep(3)
        driver.swipe(start_x=20, start_y=1350, end_x=20, end_y=330, duration=2000)
        sleep(1)
        play_number_3 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_3 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_3 = {play_name_3[i].text: play_number_3[i].text}
                list_1.append(dict_3)
                if j == int(b):
                    break

    if j == 15:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        play_number_4 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_4 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_4 = {}
                dict_4[play_name_4[i].text] = play_number_4[i].text
                list_1.append(dict_4)
                if j == int(b):
                    break

    if j == 20:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        sleep(3)
        driver.swipe(start_x=20, start_y=1350, end_x=20, end_y=330, duration=2000)
        play_number_5 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_5 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_5 = {}
                dict_5[play_name_5[i].text] = play_number_5[i].text
                list_1.append(dict_5)
                if j == int(b):
                    break

    if j == 25:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        play_number_6 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_6 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_6 = {}
                dict_6[play_name_6[i].text] = play_number_6[i].text
                list_1.append(dict_6)
                if j == int(b):
                    break

    if j == 30:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        sleep(3)
        driver.swipe(start_x=20, start_y=1350, end_x=20, end_y=330, duration=2000)
        play_number_7 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_7 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_7 = {}
                dict_7[play_name_7[i].text] = play_number_7[i].text
                list_1.append(dict_7)
                if j == int(b):
                    break

    if j == 35:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        play_number_8 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_8 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_8 = {}
                dict_8[play_name_8[i].text] = play_number_8[i].text
                list_1.append(dict_8)
                if j == int(b):
                    break

    if j == 40:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        sleep(3)
        driver.swipe(start_x=20, start_y=1350, end_x=20, end_y=330, duration=2000)
        play_number_9 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_9 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_9 = {}
                dict_9[play_name_9[i].text] = play_number_9[i].text
                list_1.append(dict_9)
                if j == int(b):
                    break

    if j == 45:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        play_number_10 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_10 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_10 = {}
                dict_10[play_name_10[i].text] = play_number_10[i].text
                list_1.append(dict_10)
                if j == int(b):
                    break

    if j == 50:
        # 下拉整个屏幕
        driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
        sleep(3)
        driver.swipe(start_x=20, start_y=1350, end_x=20, end_y=330, duration=2000)
        play_number_11 = driver.find_elements_by_id('com.yy.sport:id/betItemTextView')
        play_name_11 = driver.find_elements_by_id("com.yy.sport:id/betTypeTextView")
        listnum = driver.find_elements_by_id("com.yy.sport:id/smallTextView")
        for i in range(len(listnum)):
            if listnum[i].text != ('第' + p + '期'):
                break
            if listnum[i].text == ('第' + p + '期'):
                j += 1
                dict_11 = {}
                dict_11[play_name_11[i].text] = play_number_11[i].text
                list_1.append(dict_11)
                if j == int(b):
                    break

    driver.swipe(start_x=20, start_y=1470, end_x=20, end_y=260, duration=2000)
    sleep(3)
    driver.swipe(start_x=20, start_y=1350, end_x=20, end_y=330, duration=2000)
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if driver.find_elements_by_id("com.yy.sport:id/smallTextView")[0] == ('第' + p + '期'):
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + '玩法:快三娱乐城' + ',' + '投注记录验证' + ',' + result + ',' + filename + ',' + '实际投注数量小于统计数量' + '\n')
    if j < int(b):
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + '玩法:快三娱乐城' + ',' + '投注记录验证' + ',' + result + ',' + filename + ',' + '实际投注数量大于统计数量' + '\n')


    else:
        assert_equal_el(driver, expect=int(b), actual=j, case='投注记录数量验证', scenes='玩法:快三娱乐城')
    print(len(list_1))

    return j, list_1


def compaire_dict(driver, page_1, page_2, page_3, dict_statistics):
    list_content = []
    list_except = []

    for i in dict_statistics:
        # 如果键刚好在p1中
        if i in page_1:
            for j in page_1[i]:
                if j in dict_statistics[i] and len(dict_statistics[i]) == len(page_1[i]):
                    # print("%s玩法，%s下注内容一致，数量相等"%(i,j))
                    list_content.append('相同')
                else:
                    # print('%s玩法%s下注内容一致，数量不相等'%(i,j))
                    list_except.append({'玩法': i, '内容': j})

        if i in page_2:
            for j in page_2[i]:
                if j in dict_statistics[i] and len(dict_statistics[i]) == len(page_2[i]):
                    # print("%s玩法，%s下注内容一致，数量相等"%(i,j))
                    list_content.append('相同')
                else:
                    # print('%s玩法%s下注内容一致，数量不相等'%(i,j))
                    list_except.append({'玩法': i, '内容': j})

        if i in page_3:
            for j in page_3[i]:
                if j in dict_statistics[i] and len(dict_statistics[i]) == len(page_3[i]):
                    # print("%s玩法，%s下注内容一致，数量相等"%(i,j))
                    list_content.append('相同')
                else:
                    # print('%s玩法%s下注内容一致，数量不相等'%(i,j))
                    list_except.append({'玩法': i, '内容': j})

    assert_not_null(actual=list_except, case='投注次数和投注内容', scenes='玩法:快三娱乐城')
    return '快三游戏执行结束'
