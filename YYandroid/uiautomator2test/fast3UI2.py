import uiautomator2

from uiautomator2test.publicomponent.assertion import assert_presence, page_number_avaliable
from uiautomator2test.publicomponent.modules import onclick_verify_balance_back_game, \
    add_betlist_verify_balance_back_game
from uiautomator2test.publicomponent.others import choose_betstyle, check_if_in_offical, check_if_in_gametown, \
    shadow_click


class Anhuifast3:
    def __init__(self):
        phone = uiautomator2.connect('127.0.0.1:62001')
        print(phone.device_info)


        phone.app_clear("com.yy.sport")
        print('清除app')

        phone.watcher("OK").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='Wait']").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").click()
        print('启动watcher ,点击ok')
        phone.watcher.start()


        phone.app_start('com.yy.sport', stop=True)
        print('启动app')
        phone.watcher("OK").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").click()
        print('启动watcher ,点击ok')
        phone.watcher.start()
        phone.wait_timeout = 20

        self.s = phone.session(package_name='com.yy.sport', attach=True)
        try:
            self.s(resourceId='com.yy.sport:id/tv_download').click()
            print('点广告')
        except:
            print('没有广告')
        self.s(resourceId='com.yy.sport:id/account').click(timeout=8)
        self.s(resourceId='com.yy.sport:id/account').clear_text()
        self.s(resourceId='com.yy.sport:id/account').send_keys('jantion001')
        self.s(resourceId="com.yy.sport:id/tv_password").click()
        self.s(resourceId="com.yy.sport:id/tv_password").send_keys('jantion001')
        self.s(resourceId="com.yy.sport:id/tv_login").click()
        try:
            self.s(resourceId="com.yy.sport:id/iv_delete").click()  # 活动公告


        except:
            print('没有广告')
        try:
            login_text = self.s(text="M6体育").get_text()
            assert_presence(self, expect='M6体育', actual=login_text, case='登录测试', scenes='进入首页')
        except:
            pass

        self.s(description="娱乐").click()
        self.s().must_wait(2)
        self.s.swipe(fx=448, fy=1350, tx=448, ty=250, duration=0.5)
        self.s().must_wait(2)
        self.s(resourceId="com.yy.sport:id/home_imageview2", instance=4).click()
        try:
            caipiao_text = self.s(text="彩票").get_text()
            assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')
        except:
            try:
                self.s(resourceId="com.yy.sport:id/home_imageview2", instance=4).click()
                caipiao_text = self.s(text="彩票").get_text()
                assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')
            except:
                assert_presence(self, expect='彩票', actual='无', case='进入彩票模块', scenes='进入首页')
        self.s(text="快三").click()
        self.s().must_wait = 1

        try:
            self.s(text="安徽快三").click(timeout=2)
            game_text = self.s(text="玩法").get_text()
            assert_presence(self, expect='玩法', actual=game_text, case='进入"安徽快三"', scenes='进入游戏')
        except:
            print('第一次点击失败了')
            self.s(text="安徽快三").click(timeout=2)
            game_text = self.s(text="玩法").get_text()
            assert_presence(self, expect='玩法', actual=game_text, case='进入"安徽快三"', scenes='进入游戏')
        try:

            self.s.click(x=430,y=770)
            self.s.click(x=430,y=770)
            self.s.click(x=430,y=770)
        except:
            print('没有阴影')




    def fast3_sum(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='和值',betstyle_2='和值',instance2=1,betstyle_3='和值',instance3=2)  # 选择玩法
        page_number_avaliable(self, style='快三-安徽快三-和值', num=0, exnum='3')  # 页面选号断言
        self.s(text='3').click()
        self.s(text='4').click()
        self.s(text='5').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s(text='任意豹子').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-和值', case1='一键投注',
                                         gamename1='快三-安徽快三-和值',
                                         playmenthod='快三-安徽快三-和值', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-和值')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='和值', betstyle_2='和值', instance2=1, betstyle_3='和值', instance3=2)  # 选择玩法
        self.s(text='3').click()
        self.s(text='4').click()
        self.s(text='5').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s(text='任意豹子').click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-和值', scenes='玩法:快三-安徽快三-和值',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-和值', playmenthod='玩法:快三-安徽快三-和值',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-和值')

    def fast3_dxds(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='和值', betstyle_2='和值', instance2=1, betstyle_3='总和大小单双')  # 选择玩法
        page_number_avaliable(self, style='快三-安徽快三-总和大小单双', num=0, exnum='大')  # 页面选号断言
        self.s(text='大').click()
        self.s(text='小').click()
        self.s(text='单').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-总和大小单双', case1='一键投注',
                                         gamename1='快三-安徽快三-总和大小单双',
                                         playmenthod='快三-安徽快三-总和大小单双', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-总和大小单双')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='和值', betstyle_2='和值', instance2=1, betstyle_3='总和大小单双')  # 选择玩法
        self.s(text='大').click()
        self.s(text='小').click()
        self.s(text='单').click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-总和大小单双', scenes='玩法:快三-安徽快三-总和大小单双',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-总和大小单双', playmenthod='玩法:快三-安徽快三-总和大小单双',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-总和大小单双')




    def fast3_same3_general(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三同号通选',  betstyle_3='三同号通选',instance3=1)  # 选择玩法
        page_number_avaliable(self, style='快三-安徽快三-三同号通选', num=0, exnum='三同号通选')  # 页面选号断言
        self.s(text='三同号通选').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-三同号通选', case1='一键投注',
                                         gamename1='快三-安徽快三-三同号通选',
                                         playmenthod='快三-安徽快三-三同号通选', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-三同号通选')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='和值', betstyle_2='和值', instance2=1, betstyle_3='三同号通选')  # 选择玩法
        self.s(text='三同号通选').click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-三同号通选', scenes='玩法:快三-安徽快三-三同号通选',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-三同号通选', playmenthod='玩法:快三-安徽快三-三同号通选',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-三同号通选')
    def fast3_same3_single(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三同号单选',  betstyle_3='三同号单选',instance3=1)  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball',instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-三同号单选', case1='一键投注',
                                         gamename1='快三-安徽快三-三同号单选',
                                         playmenthod='快三-安徽快三-三同号单选', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-三同号单选')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三同号单选', betstyle_3='三同号单选',instance3=1) # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball',instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-三同号单选', scenes='玩法:快三-安徽快三-三同号单选',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-三同号单选', playmenthod='玩法:快三-安徽快三-三同号单选',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-三同号单选')

    def fast3_diff3(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三不同号',  betstyle_3='三不同号',instance3=2)  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball',instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball',instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball',instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-三不同号', case1='一键投注',
                                         gamename1='快三-安徽快三-三不同号',
                                         playmenthod='快三-安徽快三-三不同号', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-三不同号')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三不同号',  betstyle_3='三不同号',instance3=2)  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-三不同号', scenes='玩法:快三-安徽快三-三不同号',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-三不同号', playmenthod='玩法:快三-安徽快三-三不同号',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-三不同号')



    def fast3_diff3_TD(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三不同号',  betstyle_3='三不同号胆拖')  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball',instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball',instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball',instance=10).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-三不同号胆拖', case1='一键投注',
                                         gamename1='快三-安徽快三-三不同号胆拖',
                                         playmenthod='快三-安徽快三-三不同号胆拖', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-三不同号胆拖')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三不同号', betstyle_3='三不同号胆拖')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=10).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-三不同号胆拖', scenes='玩法:快三-安徽快三-三不同号胆拖',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-三不同号胆拖', playmenthod='玩法:快三-安徽快三-三不同号胆拖',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-三不同号胆拖')


    def fast3_continuous3_general(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三连号通选',  betstyle_3='三连号通选',instance3=1)  # 选择玩法

        self.s(text='三连号通选').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-三连号通选', case1='一键投注',
                                         gamename1='快三-安徽快三-三连号通选',
                                         playmenthod='快三-安徽快三-三连号通选', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-三连号通选')


        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三连号通选', betstyle_3='三连号通选',instance3=1)  # 选择玩法
        self.s(text='三连号通选').click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-三连号通选', scenes='玩法:快三-安徽快三-三连号通选',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-三连号通选', playmenthod='玩法:快三-安徽快三-三连号通选',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-三连号通选')

    def fast3_same2_duplex(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二同号复选',  betstyle_3='二同号复选',instance3=1)  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-二同号复选', case1='一键投注',
                                         gamename1='快三-安徽快三-二同号复选',
                                         playmenthod='快三-安徽快三-二同号复选', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-二同号复选')


        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二同号复选', betstyle_3='二同号复选',instance3=1)  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-二同号复选', scenes='玩法:快三-安徽快三-二同号复选',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-二同号复选', playmenthod='玩法:快三-安徽快三-二同号复选',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-二同号复选')
    def fast3_same2_single(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二同号单选',  betstyle_3='二同号单选',instance3=1)  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-二同号单选', case1='一键投注',
                                         gamename1='快三-安徽快三-二同号单选',
                                         playmenthod='快三-安徽快三-二同号单选', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-二同号单选')


        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二同号单选', betstyle_3='二同号单选',instance3=1)  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-二同号单选', scenes='玩法:快三-安徽快三-二同号单选',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-二同号单选', playmenthod='玩法:快三-安徽快三-二同号单选',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-二同号单选')

    def fast3_diff2(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二不同号',  betstyle_3='二不同号',instance3=2)  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball',instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball',instance=2).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-二不同号', case1='一键投注',
                                         gamename1='快三-安徽快三-二不同号',
                                         playmenthod='快三-安徽快三-二不同号', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-二不同号')
        check_if_in_offical(self, text='和值-和值-和值', style='二不同号')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二不同号',  betstyle_3='二不同号',instance3=2)  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-二不同号', scenes='玩法:快三-安徽快三-二不同号',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-二不同号', playmenthod='玩法:快三-安徽快三-二不同号',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-二不同号')



    def fast3_diff2_TD(self):
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二不同号',  betstyle_3='二不同号胆拖')  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball',instance=1).click()

        self.s(resourceId='com.yy.sport:id/tv_ball',instance=10).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-二不同号胆拖', case1='一键投注',
                                         gamename1='快三-安徽快三-二不同号胆拖',
                                         playmenthod='快三-安徽快三-二不同号胆拖', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-二不同号胆拖')
        check_if_in_offical(self, text='和值-和值-和值', style='安徽快三')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二不同号', betstyle_3='二不同号胆拖')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=10).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='快三-安徽快三-二不同号胆拖', scenes='玩法:快三-安徽快三-二不同号胆拖',
                                             case1='添加注单下注',
                                             gamename1='快三-安徽快三-二不同号胆拖', playmenthod='玩法:快三-安徽快三-二不同号胆拖',
                                             case2='添加注单金额验证',
                                             gamename2='快三', style2='安徽快三', menthod='快三-安徽快三-二不同号胆拖')

    def fast3_gametown(self):
        shadow_click(self)
        check_if_in_gametown(self, text='整合', style='快三-安徽快三')
        shadow_click(self)

        self.s(text='3').click()
        self.s(text='4').click()
        self.s(text='5').click()
        self.s(text='大').click()
        self.s(text='小').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s(text='任意豹子').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:快三-安徽快三-娱乐城', case1='一键投注',
                                         gamename1='快三-安徽快三-娱乐城',
                                         playmenthod='快三-安徽快三-娱乐城', case2='一键投注金额验证',
                                         gamename2='快三', style='安徽快三', menthod='快三-安徽快三-娱乐城')
        self.s.service('uiautomator').stop()


if __name__ == '__main__':
    A=Anhuifast3()
    A.fast3_sum()
    A.fast3_dxds()
    A.fast3_same3_general()
    A.fast3_same3_single()
    A.fast3_same2_single()
    A.fast3_same2_duplex()
    A.fast3_diff3()
    A.fast3_diff3_TD()
    A.fast3_diff2()
    A.fast3_diff2_TD()
    A.fast3_continuous3_general()




