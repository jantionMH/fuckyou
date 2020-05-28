import os, subprocess, random, datetime, time
from time import sleep
from appium import webdriver
# genymotion SamsungNote2
from appium.webdriver.common.touch_action import TouchAction
from UItest import android5
from Utility.judge import assert_equal_el,asser_equal_nu


class YYAndroid:
    def __init__(self):


        self.driver = android5.android5app()
        self.now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time()))

    def login(self):
        # 不关心进入到彩票游戏之前的其他任何选择
        # 升级新版本
        sleep(2)
        el1 = self.driver.find_element_by_id("com.yy.sport:id/tv_download").click()
        sleep(3)
        # 输入用户名
        el3 = self.driver.find_element_by_id("com.yy.sport:id/account").click()
        sleep(3)
        self.driver.find_element_by_id("com.yy.sport:id/account").send_keys("jantion001")
        # 输入密码
        self.driver.find_element_by_id("com.yy.sport:id/tv_password").click()
        el4 = self.driver.find_element_by_id("com.yy.sport:id/tv_password").send_keys("jantion001")


        # 点击登录
        el5 = self.driver.find_element_by_id("com.yy.sport:id/tv_login").click()
        sleep(4)
        # 关闭小广告


        try:
            el6 = self.driver.find_element_by_id("com.yy.sport:id/iv_delete").click()
            sleep(7)
            listtitle = self.driver.find_elements_by_id('com.yy.sport:id/tv_tab')
            title = listtitle[0].find_element_by_id('com.yy.sport:id/tv_tab').text
            print(title)
            self.assert_equal_el(expect='M6体育',actual=title,case='登陆测试')
        except:
            print('代码执行失败')
            now=time.strftime("%H%m%d%H%M%S")
            filename = '%s.png' % now
            self.driver.get_screenshot_as_file("./report/screenshot/%s" % filename)
            with open('../data/result.csv', mode="a+") as f:
                f.write(self.now + ',' + "登录测试" + ',' + '失败' + ',' + filename + '\n')

    # assert_equal_el(driver=self.driver, expect='M6体育', actual=title, case="登陆测试")


    def openmainpage(self):

        # 关闭上方公告
        # driver.find_element_by_id('com.yy.sport:id/ivMessageClose').click()
        # sleep(3)
        # 点击娱乐
        TouchAction(self.driver).tap(x=356, y=164).perform()
        # self.driver.find_element_by_android_uiautomator('text("娱乐")')
        sleep(3)
        # 获取屏幕尺寸
        screensize = self.driver.get_window_size()
        print(screensize)
        width = screensize['width']
        height = screensize['height']

        # 向下滑动
        # driver.swipe(179,992,179,700)
        # driver.swipe(179,992,179,700)

        TouchAction(self.driver).long_press(x=492, y=1442).move_to(x=448, y=247).release().perform()
        sleep(3)
        print('进入彩票之前')
        # 进入彩票游戏fullindexXpath
        self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                          "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                          "1]/android.widget.FrameLayout["
                                          "1]/androidx.drawerlayout.widget.DrawerLayout["
                                          "1]/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager["
                                          "1]/android.view.View[1]/androidx.viewpager.widget.ViewPager["
                                          "1]/android.view.View[1]/android.view.View[1]/android.widget.FrameLayout["
                                          "1]/android.view.View[1]/android.view.View[1]/android.view.View["
                                          "3]/android.view.View[1]/android.view.View[1]/android.widget.ImageView["
                                          "1]").click()
        sleep(6)
        # 备选方案
        # TouchAction(driver).tap(x=240,y=887).perform()
        subtitle=self.driver.find_element_by_id("com.yy.sport:id/mToolbarTitleLabel").text
        assert_equal_el(self.driver,'彩票',subtitle,"进入彩票游戏页面")


    def gamehotlist(self):
        hoslist = self.driver.find_elements_by_id("hot_img_icon")
        index = random.randrange(len(hoslist))
        hoslist[index].click()

    def moregamelist(self):
        gamelist1 = self.driver.find_elements_by_id("layout1")
        index1 = random.randrange(len(gamelist1))
        gamelist2 = self.driver.find_elements_by_id("layout2")
        index2 = random.randrange(len(gamelist2))
        random.choice(gamelist2[index2].click(), gamelist1[index1].click())

    def joinSSHgame(self):
        # 点击时时彩色
        sleep(3)
        self.driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/more_title_text_1' and @text='时时彩']").click()
        # sleep(5)
        # # 进入金星1.5分彩
        # driver.find_element_by_name('VR金星1.5分彩').click()

        print('长度',len(self.driver.find_elements_by_id("com.yy.sport:id/item_text_view")))
        gametitle=self.driver.find_element_by_xpath("//android.widget.TextView["
                                                    "@resource-id='com.yy.sport:id/item_text_view' and "
                                                    "@text='VR金星1.5分彩']").text
        assert_equal_el(self.driver,expect='VR金星1.5分彩',actual=gametitle,case='金星1.5分彩页面检查')
        sleep(2)
        self.driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/item_text_view' and @text='VR金星1.5分彩']").click()
        sleep(3)

    def do_prompt(self):
            # 我知道了/两种方式定位
            self.clickoff()
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
            self.clickoff()
            sleep(1)
            self.clickoff()
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
            self.clickoff()
            sleep(1)
            self.clickoff()
            self.driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
            self.clickoff()
            numberunit=self.driver.find_elements_by_id('com.yy.sport:id/tv_title')
            self.clickoff()
            munit=numberunit[0].find_element_by_id('com.yy.sport:id/tv_title').text
            self.clickoff()
            assert_equal_el(self.driver,expect="万位",actual=munit,case="进入时时彩金星1.5页面")
            self.clickoff()
            self.driver.implicitly_wait(5)





    def numberlist(self):
        pass

    def choosenumber(self):
            # 选号
            # 万千百十
            self.clickoff()
            for i in range(1, 5):
                self.clickoff()
                U1 = random.randint(1, 9)
                self.clickoff()
                self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                                  "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                                  "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                                  "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                                  "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                                  "1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
                                                  "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                                  "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                                  "1]/android.view.View[1]/android.widget.RelativeLayout["
                                                  "%d]/android.widget.LinearLayout[1]/android.view.View["
                                                  "1]/android.widget.RelativeLayout[%d]/android.widget.RelativeLayout["
                                                  "1]/android.widget.TextView[1]" % (i, U1)).click()
                self.clickoff()
                if i == 4:
                    self.driver.swipe(start_x=492, start_y=1000, end_x=448, end_y=700, duration=1000)
                    self.clickoff()
                    # TouchAction(driver).long_press(x=492, y=1000).move_to(x=448, y=700).release().perform()

            sleep(2)
            self.clickoff()
            # 个
            U2 = random.randint(1, 9)

            self.clickoff()
            self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                              "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                              "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                              "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                              "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                              "1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
                                              "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                              "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                              "1]/android.view.View[1]/android.widget.RelativeLayout["
                                              "4]/android.widget.LinearLayout[1]/android.view.View["
                                              "1]/android.widget.RelativeLayout[%d]/android.widget.RelativeLayout["
                                              "1]/android.widget.TextView[1]" % U2).click()
            self.clickoff()
            sleep(3)

            self.clickoff()



            # 加倍
            sleep(3)

            self.clickoff()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='十']").click()

            self.clickoff()
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='十']").click()
            self.clickoff()
            # 选角
            sleep(2)
            self.clickoff()
            self.driver.find_element_by_id("com.yy.sport:id/rd_mode_jiao").click()
            self.clickoff()
            # 添加注单
            self.driver.find_element_by_id("com.yy.sport:id/btn_add").click()

            self.clickoff()
            sleep(3)
            self.clickoff()
            # 机选5注
            self.driver.find_element_by_id('com.yy.sport:id/tv_random_5').click()

            self.clickoff()
            # 确认下注
            self.driver.find_element_by_id("com.yy.sport:id/btn_bet").click()
            self.clickoff()
            # 余额
            current=self.driver.find_element_by_id("com.yy.sport:id/tv_account_balance").text
            self.clickoff()
            # 下注额
            bet_number=self.driver.find_element_by_id("com.yy.sport:id/tv_amount").text
            self.clickoff()
            # 确定
            self.driver.find_element_by_xpath(
                "//android.widget.Button[@resource-id='com.yy.sport:id/btn_sure' and @text='确定']").click()
            self.clickoff()


            # print("下注过程中测试中断并截图")
            # result = '失败'
            # now = time.strftime("%H%m%d%H%M%S")
            # filename = '%s.png' % now
            # self.driver.get_screenshot_as_file("./report/screenshot/%s" % filename)
            # with open('../data/result.csv', mode="a+") as f:
            #     f.write(self.now + ',' + '点击开奖结束通知' + ',' + result + ',' + filename + '\n')
            # 开奖结束通知



    # def assert_equal(self, expect, actual, case):
    def assert_equal_el(self,expect, actual, case):
        if expect == actual:
            result = '成功'
            print(result)

            with open('../data/result.csv', mode='a+') as f:
                f.write(self.now + ',' + case + ',' + result + ',' + '无' + '\n')
        else:
            result = '失败'
            filename = '%s.png' % self.now
            self.driver.get_screenshot_as_file("./report/screenshot/%s" % filename)
            with open('../data/result.csv', mode="a+") as f:
                f.write(self.now + ',' + case + ',' + result + ',' + filename + '\n')
    def clickoff(self):
        try:

            self.driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout["
                                              "1]/android.widget.FrameLayout[1]/android.widget.FrameLayout["
                                              "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                              "1]/android.widget.Button[1]").click()
            sleep(1)
            print('弹框被清除')
        except:
            print('没有弹框可清除')


if __name__ == '__main__':
    Y = YYAndroid()
    Y.login()
    Y.openmainpage()
    Y.joinSSHgame()
    Y.do_prompt()
    Y.choosenumber()
    # Y.gamehotlist()
