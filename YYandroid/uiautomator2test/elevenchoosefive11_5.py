import time

import uiautomator2

from uiautomator2test.publicomponent.assertion import assert_presence, assert_equal_bet, page_number_avaliable, \
    add_list_and_assert, page_text_avaliable
from uiautomator2test.publicomponent.bettingwidget import oneclick_bet, add_list_bet
from uiautomator2test.publicomponent.modules import onclick_verify_balance_back_game, \
    add_betlist_verify_balance_back_game
from uiautomator2test.publicomponent.others import game_back_to_check_balance, balance_back_to_game, \
    get_c_balance_and_check, check_if_in_gametown, check_if_in_offical, choose_betstyle, random_add_5, \
    gamtown_11c5_randomchoose, gametown_11c5_TG, shadow_click


class login_to_11c5:
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

        self.s(text="十一选五").click()
        self.s().must_wait = 1

        try:
                self.s(text="上海11选5").click(timeout=1)
                game_text = self.s(text="玩法").get_text()
                assert_presence(self, expect='玩法', actual=game_text, case='进入上海11选5', scenes='进入游戏')
        except:
                self.s(text="上海11选5").click(timeout=1)
                game_text = self.s(text="玩法").get_text()
                assert_presence(self, expect='玩法', actual=game_text, case='进入上海11选5', scenes='进入游戏')
        try:

            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
        except:
            print('没有阴影')
    def top3_direct_duplex(self):

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前三直选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=18).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=28).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前三直选复式', case1='一键投注',
                                         gamename1='上海11选5-前三直选复式',
                                         playmenthod='上海11选5-前三直选复式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前三直选复式')

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=18).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=28).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前三直选复式', scenes='玩法:上海11选5-前三直选复式'
                                             , case1='添加注单下注', gamename1='上海11选5-前三直选复式',
                                             playmenthod='玩法:上海11选5-前三直选复式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前三直选复式')

    def top3_direct_single(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03 05', style='上海11选5-前三直选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前三直选单式', case1='一键投注',
                                         gamename1='上海11选5-前三直选单式',
                                         playmenthod='上海11选5-前三直选单式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前三直选单式')

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前三直选单式', scenes='玩法:上海11选5-前三直选单式'
                                             , case1='添加注单下注', gamename1='上海11选5-前三直选单式',
                                             playmenthod='玩法:上海11选5-前三直选单式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前三直选单式')

    def top3_group_duplex(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前三组选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前三组选复式', case1='一键投注',
                                         gamename1='上海11选5-前三组选复式',
                                         playmenthod='上海11选5-前三组选复式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前三组选复式')
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前三组选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前三组选复式', scenes='玩法:上海11选5-前三组选复式'
                                             , case1='添加注单下注', gamename1='上海11选5-前三组选复式',
                                             playmenthod='玩法:上海11选5-前三组选复式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前三组选复式')

    def top3_group_single(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03 05', style='上海11选5-前三组选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前三组选单式', case1='一键投注',
                                         gamename1='上海11选5-前三组选单式',
                                         playmenthod='上海11选5-前三组选单式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前三组选单式')
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前三组选单式', scenes='玩法:上海11选5-前三组选单式'
                                             , case1='添加注单下注', gamename1='上海11选5-前三组选单式',
                                             playmenthod='玩法:上海11选5-前三组选单式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前三组选单式')

    def top2_direct_duplex(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前二直选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前二直选复式', case1='一键投注',
                                         gamename1='上海11选5-前二直选复式',
                                         playmenthod='上海11选5-前二直选复式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前二直选复式')
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前二直选复式', scenes='玩法:上海11选5-前二直选复式'
                                             , case1='添加注单下注', gamename1='上海11选5-前二直选复式',
                                             playmenthod='玩法:上海11选5-前二直选复式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前二直选复式')

    def top2_direct_single(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03', style='上海11选5-前二直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前二直选单式', case1='一键投注',
                                         gamename1='上海11选5-前二直选单式',
                                         playmenthod='上海11选5-前二直选单式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前二直选单式')
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前二直选单式', scenes='玩法:上海11选5-前二直选单式'
                                             , case1='添加注单下注', gamename1='上海11选5-前二直选单式',
                                             playmenthod='玩法:上海11选5-前二直选单式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前二直选单式')

    def top2_group_duplex(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前二组选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前二组选复式', case1='一键投注',
                                         gamename1='上海11选5-前二组选复式',
                                         playmenthod='上海11选5-前二组选复式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前二组选复式')
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前二组选复式', scenes='玩法:上海11选5-前二组选复式'
                                             , case1='添加注单下注', gamename1='上海11选5-前二组选复式',
                                             playmenthod='玩法:上海11选5-前二组选复式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前二组选复式')

    def top2_group_single(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03', style='上海11选5-前二组选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-前二组选单式', case1='一键投注',
                                         gamename1='上海11选5-前二组选单式',
                                         playmenthod='上海11选5-前二组选单式', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-前二组选单式')
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面

        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-前二组选单式', scenes='玩法:上海11选5-前二组选单式'
                                             , case1='添加注单下注', gamename1='上海11选5-前二组选单式',
                                             playmenthod='玩法:上海11选5-前二组选单式', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-前二组选单式')


    def position_11c5(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='定位胆', instance=0).click()
        self.s(text='定位胆', instance=2).click()
        page_number_avaliable(self, style='上海11选5-定位胆', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-定位胆', case1='一键投注',
                                         gamename1='上海11选5-定位胆',
                                         playmenthod='上海11选5-定位胆', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-定位胆')

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='定位胆', instance=0).click()
        self.s(text='定位胆', instance=2).click()

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-定位胆', scenes='玩法:上海11选5-定位胆'
                                             , case1='添加注单下注', gamename1='上海11选5-定位胆',
                                             playmenthod='玩法:上海11选5-定位胆', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-定位胆')


    def random_position_11c5(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', betstyle_3='前三位')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-不定位', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-不定位', case1='一键投注',
                                         gamename1='上海11选5-不定位',
                                         playmenthod='上海11选5-不定位', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-不定位')

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', betstyle_3='前三位')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='上海11选5-不定位', scenes='玩法:上海11选5-不定位'
                                             , case1='添加注单下注', gamename1='上海11选5-不定位',
                                             playmenthod='玩法:上海11选5-不定位', case2='添加注单金额验证',
                                             gamename2='十一选五', style2='上海11选5', menthod='上海11选5-不定位')

    def gametown_11c5_two_sides(self):

        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-两面', num=0, exnum='大')

        self.s(text='小', instance=0).click()
        self.s(text='大', instance=1).click()
        self.s(text='小', instance=2).click()
        self.s().swipe('up', steps=10)
        self.s(text='小', instance=1).click()
        self.s(text='小', instance=2).click()
        self.s(text='小', instance=3).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-两面', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-两面',
                                         playmenthod='上海11选5-娱乐城-两面', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-两面')

    def gametown_11c5_ball_1(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='第一球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第一球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-第一球', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-第一球',
                                         playmenthod='上海11选5-娱乐城-第一球', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第一球')

    def gametown_11c5_ball_2(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='第二球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第二球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-第二球', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-第二球',
                                         playmenthod='上海11选5-娱乐城-第二球', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第二球')

    def gametown_11c5_ball_3(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='第三球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第三球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-第三球', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-第三球',
                                         playmenthod='上海11选5-娱乐城-第三球', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第三球')

    def gametown_11c5_ball_4(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='第四球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第四球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-第四球', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-第四球',
                                         playmenthod='上海11选5-娱乐城-第四球', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第四球')

    def gametown_11c5_ball_5(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='第五球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第五球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-第五球', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-第五球',
                                         playmenthod='上海11选5-娱乐城-第五球', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第五球')

    def gametown_11c5_ball_random(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='任选')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-任选', num=0, exnum='1')
        gamtown_11c5_randomchoose(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-任选', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-任选',
                                         playmenthod='上海11选5-娱乐城-任选', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-任选')


    def gametown_11c5_ball_TG(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='龙虎斗')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-龙虎斗', num=0, exnum='龙')
        gametown_11c5_TG(self)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:上海11选5-娱乐城-龙虎斗', case1='一键投注',
                                         gamename1='上海11选5-娱乐城-龙虎斗',
                                         playmenthod='上海11选5-娱乐城-龙虎斗', case2='一键投注金额验证',
                                         gamename2='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-龙虎斗')
if __name__ == '__main__':
    lt_11c5 = login_to_11c5()
    lt_11c5.top3_direct_duplex()
    lt_11c5.top3_direct_single()
    lt_11c5.top3_group_duplex()
    lt_11c5.top3_group_single()
    lt_11c5.top2_direct_duplex()
    lt_11c5.top2_direct_single()
    lt_11c5.top2_group_duplex()
    lt_11c5. top2_group_single()
    lt_11c5.position_11c5()
    lt_11c5.random_position_11c5()
    lt_11c5.gametown_11c5_two_sides()
    lt_11c5.gametown_11c5_ball_1()
    lt_11c5.gametown_11c5_ball_2()
    lt_11c5.gametown_11c5_ball_3()
    lt_11c5.gametown_11c5_ball_4()
    lt_11c5.gametown_11c5_ball_5()
    lt_11c5.gametown_11c5_ball_random()
    lt_11c5.gametown_11c5_ball_TG()
