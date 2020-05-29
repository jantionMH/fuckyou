from Utility.judge import assert_equal_el, assert_more_than
from time import sleep
import time


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
    print("下注的金额%s" % B_betnum)

    # 断言:确认提示框出现表明一键投注功能可用
    subtitle = driver.find_element_by_id("com.yy.sport:id/cb_select").text
    assert_equal_el(driver, expect='本次后不再进行确认提示', actual=subtitle, case='一键投注', scenes='玩法:%s' % methodtitle)
    # 点击确定
    sleep(2)
    driver.find_element_by_id("com.yy.sport:id/btn_sure").click()

    return [newbefore, B_betnum]


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
                now + ',' + '玩法:%s' % rule + ',' + "返回上层验证金额" + ',' + result + ',' + filename + ',' + '\n')
    time.sleep(1)
    # 找到我的
    driver.find_elements_by_id("com.yy.sport:id/smallLabel")[4].click()


def currentbalance(driver):
    currentbalance = driver.find_element_by_id("com.yy.sport:id/iv_user_balance").text

    newcurrent = currentbalance.replace(",", "")
    print("当前金额",newcurrent)
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
