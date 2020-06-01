from UItest import android5,android8
from time import sleep
import time
from appium import webdriver

from Utility.judge import assert_equal_el

def login(androidA):
    # 不关心进入到彩票游戏之前的其他任何选择
    # 升级新版本

    driver=None
    if androidA==5:

        driver=android5.android5app()
    elif androidA==8:
        driver=android8.Android8app()
        sleep(3)
    driver.implicitly_wait(5)

    el1 = driver.find_element_by_id("com.yy.sport:id/tv_download").click()

    # 输入用户名
    el3 =driver.find_element_by_id("com.yy.sport:id/account").click()

    driver.find_element_by_id("com.yy.sport:id/account").send_keys("jantion001")
    # 输入密码
    driver.find_element_by_id("com.yy.sport:id/tv_password").click()
    el4 =driver.find_element_by_id("com.yy.sport:id/tv_password").send_keys("jantion001")

    # 点击登录
    el5 =driver.find_element_by_id("com.yy.sport:id/tv_login").click()

    # 关闭小广告
    try:
     driver.find_element_by_id("com.yy.sport:id/iv_delete").click()
     sleep(7)
    except:
        print("没有广告")
    listtitle = driver.find_elements_by_id('com.yy.sport:id/tv_tab')
    title = listtitle[0].find_element_by_id('com.yy.sport:id/tv_tab').text
    print(title)
    assert_equal_el(driver,expect='M6体育', actual=title, case='登陆测试',scenes='进入首页')

    return driver
