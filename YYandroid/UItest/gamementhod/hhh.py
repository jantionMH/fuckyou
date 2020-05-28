import random, time
from Utility.judge import assert_equal_el, assert_more_than, asser_equal_nu


def hhhmenthod(driver):
    time.sleep(2)
    # 断言页面是否可选号
    numtext = driver.find_elements_by_id('com.yy.sport:id/tv_ball')[15].text
    print(type(numtext), '所选元素%s' % numtext)
    assert_equal_el(driver, expect='18', actual=numtext, case="页面选号", scenes='玩法:快三和值')
    for i in range(10):
        r = random.randrange(3, 19)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='%d']" % r).click()

    # 加倍
    driver.find_element_by_xpath("//android.widget.TextView[@text='十']").click()
    time.sleep(1)


# 一键投注
def fastbet(driver):
    #点击一键投注
    driver.find_element_by_xpath(
        "//android.widget.Button[@resource-id='com.yy.sport:id/btn_bet' and @text='一键投注']").click()
    time.sleep(1)
    # 一键投注时拿到现在的金额和下注额
    beforebalance = driver.find_element_by_id("com.yy.sport:id/tv_account_balance").text
    print("下注前账户金额：%s" % beforebalance)
    betnum = driver.find_element_by_id("com.yy.sport:id/tv_amount").text
    print("下注的金额%s" % betnum)
    time.sleep(3)
    # 确认提示框出现表明一键投注功能可用
    subtitle = driver.find_element_by_id("com.yy.sport:id/cb_select").text
    assert_equal_el(driver, expect='本次后不再进行确认提示', actual=subtitle, case='一键投注', scenes='玩法：快三和值')
    driver.find_element_by_id("com.yy.sport:id/btn_sure").click()
    time.sleep(3)
    driver.implicitly_wait(5)
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
        with open('../../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + '玩法:快三和值' + ',' + "返回上层验证金额" + ',' + result + ',' + filename + ',' + '\n')
    time.sleep(1)
    # 找到我的
    driver.find_elements_by_id("com.yy.sport:id/smallLabel")[4].click()
    time.sleep(1)
    # 获取金额数据
    currentbalance = driver.find_element_by_id("com.yy.sport:id/iv_user_balance").text

    newcurrent = currentbalance.replace(",", "")
    before = beforebalance.replace(",", "")
    newbefore = before.split('.')[0] + '.' + before.split('.')[1][:2]

    print('结算后的金额', type(float(newcurrent)), float(newcurrent))
    print('下注前的金额', type(newbefore), newbefore)
    print('下注的金额', type(float(betnum)), betnum)
    print('减法运算后的结果%.2f' % (float(newbefore) - float(betnum)))
    print(str(float(newcurrent) == float(newbefore) - float(betnum)))
    print(str(True))
    asser_equal_nu(driver, current=float(newbefore), bet_number=float(betnum), after_bet=float(newcurrent), case="金额验证",
                   scenes="玩法：快三和值")

    time.sleep(5)


# 进入添加注单页面
def addbetpage(driver):
    driver.find_element_by_id("com.yy.sport:id/btn_add").click()
    time.sleep(2)
    text = driver.find_element_by_xpath("//android.widget.TextView[@text='投注单']").text
    assert_equal_el(driver, expect='投注单', actual=text, case="添加注单", scenes="玩法：快三和值")


def rollback(driver):
    driver.find_elements_by_id("com.yy.sport:id/icon")[1].click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/more_title_text_1' and @text='快三']").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//android.widget.TextView[@resource-id='com.yy.sport:id/item_text_view' and @text='安徽快三']").click()


# 添加注单并结算
def addbetlist(driver):
    # 增加5注
    driver.find_element_by_id("com.yy.sport:id/tv_random_5").click()
    # 投注数量
    betnum = driver.find_element_by_id("com.yy.sport:id/tv_betNum").text
    assert_more_than(driver, expect=4, actual=int(betnum), scenes="玩法：快三和值", case="随机添加5注")
    # 点击下单
    driver.find_element_by_id("com.yy.sport:id/btn_bet").click()
    time.sleep(2)
    beforebalance = driver.find_element_by_id("com.yy.sport:id/tv_account_balance").text
    betnum = driver.find_element_by_id("com.yy.sport:id/tv_amount").text
    driver.find_element_by_id("com.yy.sport:id/btn_sure").click()
    time.sleep(3)
    extitle = driver.find_element_by_id("com.yy.sport:id/tv_play").text
    assert_equal_el(driver, expect="玩法", actual=extitle, case="添加注单下注", scenes="玩法：快三和值")
    time.sleep(1)
    # 返回页面，验证金额
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]").click()
    time.sleep(2)
    driver.find_elements_by_id("com.yy.sport:id/icon")[4].click()
    time.sleep(1)
    currentbalance = driver.find_element_by_id("com.yy.sport:id/iv_user_balance").text
    newcurrent = currentbalance.replace(",", "")
    before = beforebalance.replace(",", "")
    newbefore = before.split('.')[0] + '.' + before.split('.')[1][:2]
    print('结算后的金额', type(float(newcurrent)), float(newcurrent))
    print('下注前的金额', type(newbefore), newbefore)
    print('下注的金额', type(float(betnum)), betnum)
    print('减法运算后的结果%.2f' % (float(newbefore) - float(betnum)))
    print(str(float(newcurrent) == float(newbefore) - float(betnum)))
    print(str(True))
    asser_equal_nu(driver, current=float(newbefore), bet_number=float(betnum), after_bet=float(newcurrent), case="金额验证",
                   scenes="玩法：快三和值")
    time.sleep(1)
    #返回到游戏选号页面
    #wait to write
