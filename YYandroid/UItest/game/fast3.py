from time import sleep
from UItest.gamementhod.hhh import hhhmenthod, fastbet, addbetpage, addbetlist, rollback
from Utility.judge import assert_equal_el, asser_equal_nu
from common.component import Oneclickbetting, ruleoption, add_double, shadowcilck, returntopage, currentbalance, \
    rollbackC, addbetpageC, add5bet, addbet_comfire


def fastthree(driver, ruleselection):
    print("进入快三")
    sleep(3)
    title = driver.find_element_by_id("com.yy.sport:id/tv_num_desc").text
    print(title, '快三' in title)
    assert_equal_el(driver, expect=str(True), actual=str('快三' in title), case="安徽快三游戏投注页面", scenes='进入快三游戏')
    # 阴影三点
    driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
    sleep(1)
    driver.find_element_by_xpath("//android.widget.RelativeLayout").click()

    sleep(2)
    # 打开玩法选项

    driver.find_element_by_xpath("//android.widget.TextView[@text='和值-和值-和值']").click()

    sleep(1)
    if ruleselection == '和值-和值-和值':
        # 选择默认和-和-和玩法
        driver.find_elements_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='和值']")[2].click()
    else:
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text=%s]" % ruleselection).click()

    sleep(2)

    methodtitle = driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                               "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                               "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                               "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout["
                                               "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                               "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]").text
    assert_equal_el(driver, expect=ruleselection, actual=methodtitle, scenes='玩法:快三%s' % ruleselection, case='选择玩法')
    print("当前所选的玩法是%s" % methodtitle)
    return methodtitle


# 和值-和值-和值玩法 专属方法
def hezhi_play(driver, methodtitle):
    if methodtitle == "和值-和值-和值":
        # 一键投注
        hhhmenthod(driver)  # 选号
        fastbet(driver)  # 直接投注并验证金额

        # 回到投注页面
        rollback(driver)

        # 添加注单
        hhhmenthod(driver)  # 选号
        addbetpage(driver)  # 添加注单
        addbetlist(driver)  # 随机增加5注并验证金额

        # 回到投注页面
        rollback(driver)
        sleep(2)


def SBSSDchoosenum(driver, upmethodtitle):
    if upmethodtitle == "和值":
        methodtitle="和值-大小单双"
        gametype='快三'
        gameport='安徽快三'
        sleep(2)
        #阴影三点
        shadowcilck(driver)
        sleep(1)
        # 打开玩法选项
        ruleoption(driver)
        sleep(1)
        # 选择大小单双
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='总和大小单双']").click()
        sleep(1)
        # 下注大小单双
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[0].click()
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[1].click()
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[2].click()
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[3].click()
        sleep(1)
        # 加倍
        add_double(driver)
        # 一键投注
        res=Oneclickbetting(driver,methodtitle)
        A_balance=res[0]
        B_balance=res[1]
        sleep(2)

        #返回上曾页面
        returntopage(driver, rule=methodtitle)
        sleep(1)
        # 验证金额
        C_balance=currentbalance(driver)
        asser_equal_nu(driver, current=float(A_balance), bet_number=float(B_balance), after_bet=float(C_balance), case="金额验证",
                       scenes="玩法：%s"%methodtitle)
        # 回滚到投注页面
        sleep(1)
        rollbackC(driver,gametype='快三', gameport='安徽快三')
        sleep(2)
        # 打开玩法选项
        ruleoption(driver)
        sleep(1)
        # 选择大小单双
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_play_desc' and @text='总和大小单双']").click()
        sleep(1)
        # 下注大小单双
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[0].click()
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[1].click()
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[2].click()
        driver.find_elements_by_id("com.yy.sport:id/tv_ball")[3].click()

        # 加注
        addbetpageC(driver,methodtitle=methodtitle)
        sleep(2)
        # 选5注
        add5bet(driver, methodtitle=methodtitle)
        sleep(2)
        # 确认下注
        res2=addbet_comfire(driver, methodtitle=methodtitle)

        A2_balance=res2[0]
        B2_balance=res2[1]
        sleep(2)
        #返回上层页面
        returntopage(driver, rule=methodtitle)
        # 验证金额
        C2_balance = currentbalance(driver)
        asser_equal_nu(driver, current=float(A2_balance), bet_number=float(B2_balance), after_bet=float(C2_balance),
                       case="金额验证",
                       scenes="玩法：%s" % methodtitle)
        # 回滚到投注页面
        print('返回')
        sleep(1)
        rollbackC(driver, gametype='快三', gameport='安徽快三')