from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from UItest.login import login
from Utility.judge import assert_equal_el
import time

def Entrance(androidB):
    driver=login(androidA=androidB)
    TouchAction(driver).tap(x=356, y=164).perform()
    sleep(3)
    TouchAction(driver).long_press(x=492, y=1442).move_to(x=448, y=247).release().perform()
    sleep(6)
    try:
     # 进入彩票游戏
     driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                      "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                      "1]/android.widget.FrameLayout["
                                      "1]/androidx.drawerlayout.widget.DrawerLayout["
                                      "1]/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager["
                                      "1]/android.view.View[1]/androidx.viewpager.widget.ViewPager["
                                      "1]/android.view.View[1]/android.view.View[1]/android.widget.FrameLayout["
                                      "1]/android.view.View[1]/android.view.View[1]/android.view.View["
                                      "3]/android.view.View[1]/android.view.View[1]/android.widget.ImageView["
                                      "1]").click()
     sleep(8)

     subtitle = driver.find_element_by_id("com.yy.sport:id/mToolbarTitleLabel").text

     assert_equal_el(driver,expect='彩票',actual= subtitle, case="进入彩票游戏模块",scenes="进入首页")

    except:
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + "进入首页" + ',' + "进入彩票模块" + ',' + result + ',' + filename + ',' +  '\n')
    return driver