import uiautomator2
import os,subprocess,time

class BB:

    def __init__(self):

        phone = uiautomator2.connect('127.0.0.1:62001')
        print(phone.device_info)


        phone.app_clear("com.cy.sports")
        print('清除app')

        phone.watcher("OK").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='Wait']").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").click()
        print('启动watcher ,点击ok')
        phone.watcher.start()


        phone.app_start('com.cy.sports',stop=True)
        print('启动app')

        phone.implicitly_wait(20)
        self.s=phone
        # self.s = phone.session(package_name='com.cy.sports', attach=True)
        try:
            self.s(resourceId='com.cy.sports:id/tv_cancel').click()
            print('点广告')
        except:
            print('没有广告')

        # self.s(resourceId='com.yy.sport:id/account').click(timeout=8)
        self.s(resourceId='com.cy.sports:id/et_input').click(timeout=8)
        self.s(resourceId='com.cy.sports:id/et_input').clear_text()
        self.s(resourceId='com.cy.sports:id/et_input').send_keys('jantion001')
        self.s(resourceId="com.cy.sports:id/et_input",instance=1).click()
        self.s(resourceId="com.cy.sports:id/et_input",instance=1).send_keys('jantion001')
        self.s(resourceId="com.cy.sports:id/tv_login").click()


        try:
            self.s(resourceId="com.cy.sports:id/iv_close").click()  # 活动公告

        #
        except:
            print('没有广告')
        try:
            login_text = self.s(text="游戏").get_text()
            # assert_presence(self, expect='游戏', actual=login_text, case='登录测试', scenes='进入首页')
        except:
            pass

        self.s(text='游戏').click()
        # self.s().must_wait(2)
        self.s.swipe(fx=448, fy=1350, tx=448, ty=250, duration=0.5)
        self.s.swipe(fx=448, fy=1350, tx=448, ty=250, duration=0.5)
        self.s.swipe(fx=448, fy=1350, tx=448, ty=250, duration=0.5)

        # self.s().must_wait(2)
        self.s(resourceId="com.cy.sports:id/iv_image", instance=0).click()
        # try:
        #     caipiao_text = self.s(text="彩票").get_text()
        #     assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')
        # except:
        #     try:
        #         self.s(resourceId="com.yy.sport:id/home_imageview2", instance=4).click()
        #         caipiao_text = self.s(text="彩票").get_text()
        #         assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')
        #     except:
        #         assert_presence(self, expect='彩票', actual='无', case='进入彩票模块', scenes='进入首页')
        # self.s(text="快三").click()
        # self.s().must_wait = 1
        #
        # try:
        #     self.s(text="安徽快三").click(timeout=2)
        #     game_text = self.s(text="玩法").get_text()
        #     assert_presence(self, expect='玩法', actual=game_text, case='进入"安徽快三"', scenes='进入游戏')
        # except:
        #     print('第一次点击失败了')
        #     self.s(text="安徽快三").click(timeout=2)
        #     game_text = self.s(text="玩法").get_text()
        #     assert_presence(self, expect='玩法', actual=game_text, case='进入"安徽快三"', scenes='进入游戏')
        # try:
        #
        #     self.s.click(x=430,y=770)
        #     self.s.click(x=430,y=770)
        #     self.s.click(x=430,y=770)
        # except:
        #     print('没有阴影')
if __name__ == '__main__':
    # subprocess.getstatusoutput(r'C:\Program Files (x86)\Nox\bin\Nox.exe')

    # os.system(r'C:\Program Files (x86)\Nox\bin\Nox.exe')
    os.popen(r'C:\Program Files (x86)\Nox\bin\Nox.exe')
    time.sleep(30)
    B = BB()


