import time

import uiautomator2

from uiautomator2test.publicomponent.assertion import assert_equal_bet, assert_presence, page_text_avaliable, \
    page_number_avaliable
from uiautomator2test.publicomponent.bettingwidget import oneclick_bet, add_list_bet
from uiautomator2test.publicomponent.modules import onclick_verify_balance_back_game, \
    add_betlist_verify_balance_back_game
from uiautomator2test.publicomponent.others import game_back_to_check_balance, get_c_balance_and_check, \
    balance_back_to_game, check_if_in_gametown, check_if_in_offical, choose_betstyle


class login_to_game3d:

    def __init__(self):
        phone = uiautomator2.connect('127.0.0.1:62001')
        print(phone.device_info)
        phone.reset_uiautomator()
        phone.watcher("ok").when(xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").when(xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").click()
        phone.watcher.start()
        phone.app_start('com.yy.sport',stop=True)

        self.s = phone.session(package_name='com.yy.sport', attach=True)
        self.s.implicitly_wait = 5

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

        caipiao_text = self.s(text="彩票").get_text()
        assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')

        self.s(text="3D彩").click()
        self.s().must_wait = 1
        self.s(text="福彩3D").click()

        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='进入3D福彩投注页面', scenes='进入游戏')

    def game_3d_basic(self):
        """
        基础就是默认的玩法：3星-直选-直选复式
        """
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-三星-直选-直选复式', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星直选复式', case1='一键投注',
                                         gamename1='3D-3星直选复式',
                                         playmenthod='玩法:3D-3星直选复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星直选复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星直选复式', scenes='玩法:3D-3星直选复式',
                                             case1='添加注单下注',
                                             gamename1='3D-3星直选复式', playmenthod='玩法:3D-3星直选复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星直选复式')

    def game_3d_3star_direct_selection_single(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-3星直选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星直选单式', case1='一键投注',
                                         gamename1='3D-3星直选单式',
                                         playmenthod='玩法:3D-3星直选单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星直选单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星直选单式', scenes='玩法:3D-3星直选单式',
                                             case1='添加注单下注',
                                             gamename1='3D-3星直选单式', playmenthod='玩法:3D-3星直选单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星直选单式')

    def game_3d_3star_direct_selection_sum(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-三星-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        self.s(text='14').click()
        self.s(text='16').click()
        self.s(text='27').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星直选和值', case1='一键投注',
                                         gamename1='3D-3星直选和值',
                                         playmenthod='玩法:3D-3星直选和值', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星直选和值')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='直选和值').click()
        self.s(text='14').click()
        self.s(text='16').click()
        self.s(text='27').click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星直选和值', scenes='玩法:3D-3星直选和值',
                                             case1='添加注单下注', keys_2='直选和值',
                                             gamename1='3D-3星直选和值', playmenthod='玩法:3D-3星直选和值',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星直选和值')

    def game_3d_3star_group_selection_3snigle(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-3星组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星组三单式', case1='一键投注',
                                         gamename1='3D-3星组三单式',
                                         playmenthod='玩法:3D-3星组三单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星组三单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星组三单式', scenes='玩法:3D-3星组三单式',
                                             case1='添加注单下注',
                                             gamename1='3D-3星组三单式', playmenthod='玩法:3D-3星组三单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星组三单式')

    def game_3d_3star_group_selection_3duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-三星-直选-直选和值', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星组三复式', case1='一键投注',
                                         gamename1='3D-3星组三复式',
                                         playmenthod='玩法:3D-3星组三复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星组三复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星组三复式', scenes='玩法:3D-3星组三复式',
                                             case1='添加注单下注', keys_2='组三复式',
                                             gamename1='3D-3星组三复式', playmenthod='玩法:3D-3星组三复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星组三复式')

    def game_3d_3star_group_selection_6snigle(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-3星组六单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星组六单式', case1='一键投注',
                                         gamename1='3D-3星组六单式',
                                         playmenthod='玩法:3D-3星组六单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星组六单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星组六单式', scenes='玩法:3D-3星组六单式',
                                             case1='添加注单下注',
                                             gamename1='3D-3星组六单式', playmenthod='玩法:3D-3星组六单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星组六单式')

    def game_3d_3star_group_selection_6duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-三星-直选-组六复式', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-3星组六复式', case1='一键投注',
                                         gamename1='3D-3星组六复式',
                                         playmenthod='玩法:3D-3星组六复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-3星组六复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-3星组六复式', scenes='玩法:3D-3星组六复式',
                                             case1='添加注单下注',
                                             gamename1='3D-3星组六复式', playmenthod='玩法:3D-3星组六复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-3星组六复式')

    def game_3d_3star_group_selection_mix_duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-3星混合组选')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-混合组选', case1='一键投注',
                                         gamename1='3D-混合组选',
                                         playmenthod='玩法:3D-混合组选', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-混合组选')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-混合组选', scenes='玩法:3D-混合组选',
                                             case1='添加注单下注',
                                             gamename1='3D-混合组选', playmenthod='玩法:3D-混合组选',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-混合组选')

    def game_3d_3star_group_selection_sum_duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-三星-组选-组选和值', num=0, exnum='1')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=19).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-组选和值', case1='一键投注',
                                         gamename1='3D-组选和值',
                                         playmenthod='玩法:3D-组选和值', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-组选和值')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三星', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=19).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-组选和值', scenes='玩法:3D-组选和值',
                                             case1='添加注单下注', keys_2='组选和值',
                                             gamename1='3D-组选和值', playmenthod='玩法:3D-组选和值',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-组选和值')

    def game_3d_2star_top2_direct_duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-三星-直选-前二直选复式', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星前二直选复式', case1='一键投注',
                                         gamename1='3D-2星前二直选复式',
                                         playmenthod='玩法:3D-2星前二直选复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星前二直选复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星前二直选复式', scenes='玩法:3D-2星前二直选复式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星前二直选复式', playmenthod='玩法:3D-2星前二直选复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星前二直选复式')

    def game_3d_2star_top2_direct_single(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='前二直选单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-前二直选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星前二直选单式', case1='一键投注',
                                         gamename1='3D-2星前二直选单式',
                                         playmenthod='玩法:3D-2星前二直选单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星前二直选单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='前二直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星前二直选单式', scenes='玩法:3D-2星前二直选单式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星前二直选单式', playmenthod='玩法:3D-2星前二直选单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星前二直选单式')

    def game_3d_2star_last2_direct_duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-2星后二直选复式', num=0, exnum='0')  # 页面选号断言


        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星后二直选复式', case1='一键投注',
                                         gamename1='3D-2星后二直选复式',
                                         playmenthod='玩法:3D-2星后二直选复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星后二直选复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法


        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星后二直选复式', scenes='玩法:3D-2星后二直选复式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星后二直选复式', playmenthod='玩法:3D-2星后二直选复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星后二直选复式')

    def game_3d_2star_last2_direct_single(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='后二直选单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-2星后二直选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='86')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星后二直选单式', case1='一键投注',
                                         gamename1='3D-2星后二直选单式',
                                         playmenthod='玩法:3D-2星后二直选单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星后二直选单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='直选', betstyle_3='后二直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='86')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星后二直选单式', scenes='玩法:3D-2星后二直选单式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星后二直选单式', playmenthod='玩法:3D-2星后二直选单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星后二直选单式')

    def game_3d_2star_top2_group_duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='前二组选复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-二星-组选-前二组选复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星前二组选复式', case1='一键投注',
                                         gamename1='3D-2星前二组选复式',
                                         playmenthod='玩法:3D-2星前二组选复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星前二组选复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='前二组选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星前二组选复式', scenes='玩法:3D-2星前二组选复式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星前二组选复式', playmenthod='玩法:3D-2星前二组选复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星前二组选复式')

    def game_3d_2star_top2_group_single(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='前二组选单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-2星前二组选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星前二组选单式', case1='一键投注',
                                         gamename1='3D-2星前二组选单式',
                                         playmenthod='玩法:3D-2星前二组选单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星前二组选单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='前二组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星前二组选单式', scenes='玩法:3D-2星前二组选单式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星前二组选单式', playmenthod='玩法:3D-2星前二组选单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星前二组选单式')

    def game_3d_2star_last2_group_duplex(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='后二组选复式')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-二星-组选-后二组选复式', num=0, exnum='0')  # 页面选号断言


        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星后二组选复式', case1='一键投注',
                                         gamename1='3D-2星后二组选复式',
                                         playmenthod='玩法:3D-2星后二组选复式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星后二组选复式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='后二组选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星后二组选复式', scenes='玩法:3D-2星后二组选复式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星后二组选复式', playmenthod='玩法:3D-2星后二组选复式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星后二组选复式')

    def game_3d_2star_last2_group_single(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='后二组选单式')  # 选择玩法
        page_text_avaliable(self, text='111', style='3D游戏-2星后二组选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='92,73,46')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-2星后二组选单式', case1='一键投注',
                                         gamename1='3D-2星后二组选单式',
                                         playmenthod='玩法:3D-2星后二组选单式', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-2星后二组选单式')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='二星', betstyle_2='组选', betstyle_3='后二组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='92,73,46')

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-2星后二组选单式', scenes='玩法:3D-2星后二组选单式',
                                             case1='添加注单下注',
                                             gamename1='3D-2星后二组选单式', playmenthod='玩法:3D-2星后二组选单式',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-2星后二组选单式')

    def position(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='定位胆', betstyle_2='定位胆',instance2=1, betstyle_3='定位胆',instance3=2)  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-二星-组选-后二组选复式', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=25).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-定位胆', case1='一键投注',
                                         gamename1='3D-定位胆',
                                         playmenthod='玩法:3D-定位胆', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-定位胆')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='定位胆', betstyle_2='定位胆',instance2=1, betstyle_3='定位胆',instance3=2)  # 选择玩法

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=25).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-定位胆', scenes='玩法:3D-定位胆',
                                             case1='添加注单下注',
                                             gamename1='3D-定位胆', playmenthod='玩法:3D-定位胆',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-定位胆')

    def random_postion_1(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', instance2=1, betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-不定位-不定位-一码不定位', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-一码不定位', case1='一键投注',
                                         gamename1='3D-一码不定位',
                                         playmenthod='玩法:3D-一码不定位', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-一码不定位')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', instance2=1, betstyle_3='一码不定位')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-一码不定位', scenes='玩法:3D-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='3D-一码不定位', playmenthod='玩法:3D-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-一码不定位')

    def random_postion_2(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-不定位-不定位-二码不定位', num=0, exnum='0')  # 页面选号断言

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-二码不定位', case1='一键投注',
                                         gamename1='3D-一码不定位',
                                         playmenthod='玩法:3D-二码不定位', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-二码不定位')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-二码不定位', scenes='玩法:3D-二码不定位',
                                             case1='添加注单下注',
                                             gamename1='3D-二码不定位', playmenthod='玩法:3D-二码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-二码不定位')

    def dxds_top2(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='大小单双', betstyle_2='大小单双', instance2=1, betstyle_3='前二大小单双')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-大小单双-大小单双-前二大小单双', num=0, exnum='大')  # 页面选号断言

        self.s(text='单', instance=0).click()
        self.s(text='大', instance=1).click()
        onclick_verify_balance_back_game(self, scenes='玩法:3D-前二大小单双', case1='一键投注',
                                         gamename1='3D-前二大小单双',
                                         playmenthod='玩法:3D-前二大小单双', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-前二大小单双')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='大小单双', betstyle_2='大小单双', instance2=1, betstyle_3='前二大小单双')  # 选择玩法
        self.s(text='单', instance=0).click()
        self.s(text='大', instance=1).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-前二大小单双', scenes='玩法:3D-前二大小单双',
                                             case1='添加注单下注',
                                             gamename1='3D-前二大小单双', playmenthod='玩法:3D-前二大小单双',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-前二大小单双')

    def dxds_last2(self):
        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='大小单双', betstyle_2='大小单双', instance2=1, betstyle_3='后二大小单双')  # 选择玩法
        page_number_avaliable(self, style='3D彩-福彩3D-大小单双-大小单双-后二大小单双', num=0, exnum='大')  # 页面选号断言


        self.s(text='双', instance=0).click()
        self.s(text='小', instance=1).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:3D-后二大小单双', case1='一键投注',
                                         gamename1='3D-后二大小单双',
                                         playmenthod='玩法:3D-后二大小单双', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D-后二大小单双')

        check_if_in_offical(self, text='三星-直选-直选复式', style='3D游戏-福彩3D')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='大小单双', betstyle_2='大小单双', instance2=1, betstyle_3='后二大小单双')  # 选择玩法
        self.s(text='双', instance=0).click()
        self.s(text='小', instance=1).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='3D-后二大小单双', scenes='玩法:3D-后二大小单双',
                                             case1='添加注单下注',
                                             gamename1='3D-后二大小单双', playmenthod='玩法:3D-后二大小单双',
                                             case2='添加注单金额验证',
                                             gamename2='3D彩', style2='福彩3D', menthod='3D-后二大小单双')

    def gametown_3D_position_1(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='一字定位')  # 选择玩法


        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(text='单').click()
        self.s(text='合数').click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城一字定位-百', case1='一键投注',
                                         gamename1='3D-D娱乐城一字定位-百',
                                         playmenthod='玩法:3D娱乐城一字定位-百', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城一字定位-百')

        # 切换到娱乐城
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')

        self.s(text='十定位').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(text='单').click()
        self.s(text='合数').click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城一字定位-十', case1='一键投注',
                                         gamename1='3D-D娱乐城一字定位-十',
                                         playmenthod='玩法:3D娱乐城一字定位-十', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城一字定位-十')

        # 切换到娱乐城
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        self.s(text='个定位').click()

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(text='单').click()
        self.s(text='合数').click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城一字定位-个', case1='一键投注',
                                         gamename1='3D-D娱乐城一字定位-十',
                                         playmenthod='玩法:3D娱乐城一字定位-个', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城一字定位-个')

    def gametown_3d_duplex_1(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='一字组合')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城一字组合', case1='一键投注',
                                         gamename1='3D-D娱乐城一字组合',
                                         playmenthod='玩法:3D娱乐城一字组合', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城一字组合')

    def gametown_3d_positon_2(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='二字定位')  # 选择玩法

        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='97x').click()
        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-二字定位', case1='一键投注',
                                         gamename1='3D-D娱乐城-二字定位',
                                         playmenthod='玩法:3D娱乐城-二字定位', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-二字定位')

    def gametown_3d_duplex_2(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='二字组合')  # 选择玩法

        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='97').click()
        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-二字组合', case1='一键投注',
                                         gamename1='3D-D娱乐城-二字组合',
                                         playmenthod='玩法:3D娱乐城-二字组合', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-二字组合')

    def gametown_3d_sum_2(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='二字和数')  # 选择玩法

        self.s().swipe('up', steps=10)
        self.s(text='17').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=22).click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-二字和数-百十和数', case1='一键投注',
                                         gamename1='3D-D娱乐城-二字和数-百十和数',
                                         playmenthod='玩法:3D娱乐城-二字和数-百十和数', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-二字和数-百十和数')

        # 百个和数
        choose_betstyle(self, betstyle_1='二字和数')  # 选择玩法
        self.s(text='百个和数').click()
        self.s().swipe('up', steps=10)
        self.s(text='17').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=22).click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-二字和数-百个和数', case1='一键投注',
                                         gamename1='3D-3D娱乐城-二字和数-百个和数',
                                         playmenthod='玩法:3D娱乐城-二字和数-百个和数', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-二字和数-百个和数')

        # 十个和数
        choose_betstyle(self, betstyle_1='二字和数')  # 选择玩法
        self.s(text='十个和数').click()
        self.s().swipe('up', steps=10)
        self.s(text='17').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=22).click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-二字和数-十个和数', case1='一键投注',
                                         gamename1='3D-D娱乐城-二字和数-十个和数',
                                         playmenthod='玩法:3D娱乐城-二字和数-十个和数', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-二字和数-十个和数')

    def gametown_3d_position_3(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='三字定位')  # 选择玩法

        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='097').click()
        self.s(text='098').click()
        self.s(text='099').click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-三字定位', case1='一键投注',
                                         gamename1='3D-D娱乐城-三字定位',
                                         playmenthod='玩法:3D娱乐城-三字定位', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-三字定位')

    def gametown_3d_deplex_3(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='三字组合')  # 选择玩法

        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='097').click()
        self.s(text='098').click()
        self.s(text='099').click()
        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-三字组合', case1='一键投注',
                                         gamename1='3D-D娱乐城-三字组合',
                                         playmenthod='玩法:3D娱乐城-三字组合', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-三字组合')

    def gametown_3d_sum_3(self):
        check_if_in_gametown(self, text='一字定位', style='3D-娱乐城')
        choose_betstyle(self, betstyle_1='三字和数')  # 选择玩法

        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='26').click()
        self.s(text='23').click()

        onclick_verify_balance_back_game(self, scenes='玩法:3D娱乐城-三字和数', case1='一键投注',
                                         gamename1='3D-D娱乐城-三字和数',
                                         playmenthod='玩法:3D娱乐城-三字和数', case2='一键投注金额验证',
                                         gamename2='3D彩', style='福彩3D', menthod='3D娱乐城-三字和数')


if __name__ == '__main__':
    ltg = login_to_game3d()

    # 3star
    ltg.game_3d_basic()
    ltg.game_3d_3star_direct_selection_single()
    ltg.game_3d_3star_direct_selection_sum()
    ltg.game_3d_3star_group_selection_3snigle()
    ltg.game_3d_3star_group_selection_3duplex()
    ltg.game_3d_3star_group_selection_6snigle()
    ltg.game_3d_3star_group_selection_6duplex()
    ltg.game_3d_3star_group_selection_mix_duplex()
    ltg.game_3d_3star_group_selection_sum_duplex()

    '''
    2star
    '''
    ltg.game_3d_2star_top2_direct_duplex()
    ltg.game_3d_2star_top2_direct_single()
    ltg.game_3d_2star_last2_direct_duplex()
    ltg.game_3d_2star_last2_direct_single()
    ltg.game_3d_2star_top2_group_single()
    ltg.game_3d_2star_top2_group_duplex()
    ltg.game_3d_2star_last2_group_single()
    ltg.game_3d_2star_last2_group_duplex()
    '''
    定位胆
    
    '''
    ltg.position()
    """
    不定位
    """
    ltg.random_postion_1()
    ltg.random_postion_2()
    """
    大小单双
    """
    ltg.dxds_top2()
    ltg.dxds_last2()
