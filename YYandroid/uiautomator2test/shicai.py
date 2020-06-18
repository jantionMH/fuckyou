import uiautomator2
import time
from uiautomator2test.publicomponent.assertion import assert_presence, page_number_avaliable, page_text_avaliable
from uiautomator2test.publicomponent.modules import onclick_verify_balance_back_game, \
    add_betlist_verify_balance_back_game
from uiautomator2test.publicomponent.others import M6_5_star5_direct_num_page, check_if_in_offical, choose_betstyle, \
    check_if_in_gametown, shadow_click


class M65:
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

        phone.app_start('com.yy.sport',stop=True)
        print('启动app')
        phone.watcher("OK").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").click()
        print('启动watcher ,点击ok')
        phone.watcher.start()
        phone.settings['wait_timeout'] = 20

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
        self.s(text="时时彩").click()


        try:
            self.s(text="M6-5分彩").click(timeout=2)
            game_text = self.s(text="玩法").get_text()
            assert_presence(self, expect='玩法', actual=game_text, case='进入"M6-5分彩"', scenes='进入游戏')
        except:
            print('第一次点击失败了')
            self.s(text="M6-5分彩").click(timeout=2)
            game_text = self.s(text="玩法").get_text()
            assert_presence(self, expect='玩法', actual=game_text, case='进入"M6-5分彩"', scenes='进入游戏')
        try:

            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
        except:
            print('没有阴影')

    def star5_driect_duplex(self):
        # self.s.implicitly_wait = 5
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35, num30_39_2=35)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-直选-直选复式')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35, num30_39_2=35)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-直选-直选复式', scenes='玩法:时时彩-M6_5分彩-五星-直选-直选复式'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-直选-直选复式')

    def star5_driect_selection(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='直选', betstyle_3='五星组合')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-直选-五星组合', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35, num30_39_2=35)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-直选-五星组合', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-直选-五星组合',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-直选-五星组合', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-直选-五星组合')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='直选', betstyle_3='五星组合')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35, num30_39_2=35)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-直选-五星组合', scenes='玩法:时时彩-M6_5分彩-五星-直选-五星组合',
                                             keys='组合'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-直选-五星组合',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-直选-五星组合', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-直选-五星组合')

    def star5_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='12345', style='M6_5分彩-五星-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='12345')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-直选-直选单式')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='12345', style='M6_5分彩-五星-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='12345')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-直选-直选单式', scenes='玩法:时时彩-M6_5分彩-五星-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-直选-直选单式')

    def star5_group_120(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选120')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选120', num=0, exnum='0')  # 页面选号断言
        for i in range(5):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-组选-组选120', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-组选-组选120',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选120', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选120')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选120')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选120', num=0, exnum='0')  # 页面选号断言

        for i in range(5):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-组选-组选120',
                                             scenes='玩法:时时彩-M6_5分彩-五星-组选-组选120',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-组选-组选120',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选120', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选120')

    def star5_group_60(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选60')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选60', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        for i in range(11, 14):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-组选-组选60', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-组选-组选60',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选60', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选60')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选60')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选60', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        for i in range(11, 14):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-组选-组选60',
                                             scenes='玩法:时时彩-M6_5分彩-五星-组选-组选60',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-组选-组选60',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选60', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选60')

    def star5_group_30(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选30')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选30', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        for i in range(0, 2):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-组选-组选30', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-组选-组选30',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选30', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选30')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选30')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选30', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        for i in range(0, 2):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-组选-组选30',
                                             scenes='玩法:时时彩-M6_5分彩-五星-组选-组选30',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-组选-组选30',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选30', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选30')

    def star5_group_20(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选20')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选20', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        for i in range(14, 16):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-组选-组选20', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-组选-组选20',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选20', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选20')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选20')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选20', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        for i in range(14, 16):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-组选-组选20',
                                             scenes='玩法:时时彩-M6_5分彩-五星-组选-组选20',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-组选-组选20',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选20', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选20')

    def star5_group_10(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选10')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选10', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-组选-组选10', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-组选-组选10',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选10', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选10')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选10')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选10', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-组选-组选10',
                                             scenes='玩法:时时彩-M6_5分彩-五星-组选-组选10',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-组选-组选10',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选10', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选10')

    def star5_group_5(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选5')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选5', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-组选-组选5', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-组选-组选5',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选5', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选5')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='组选', betstyle_3='组选5')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-组选-组选5', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-组选-组选5',
                                             scenes='玩法:时时彩-M6_5分彩-五星-组选-组选5',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-组选-组选5',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-组选-组选5', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-组选-组选5')

    def star5_other_TGsum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='其他', betstyle_3='龙虎和')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-其他-龙虎和', num=0, exnum='龙')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-其他-龙虎和', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-其他-龙虎和',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-其他-龙虎和', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-其他-龙虎和')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='其他', betstyle_3='龙虎和')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-其他-龙虎和', num=0, exnum='龙')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-其他-龙虎和',
                                             scenes='玩法:时时彩-M6_5分彩-五星-其他-龙虎和',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-其他-龙虎和',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-其他-龙虎和', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-其他-龙虎和')

    def star5_other_dxds(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='五星', betstyle_2='其他', betstyle_3='总和大小单双')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-其他-总和大小单双', num=0, exnum='大')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-其他-总和大小单双', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-五星-其他-总和大小单双',
                                         playmenthod='玩法:时时彩-M6_5分彩-五星-其他-总和大小单双', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-五星-其他-总和大小单双')
        choose_betstyle(self, betstyle_1='五星', betstyle_2='其他', betstyle_3='总和大小单双')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-五星-其他-总和大小单双', num=0, exnum='大')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-五星-其他-总和大小单双',
                                             scenes='玩法:时时彩-M6_5分彩-五星-其他-总和大小单双',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-五星-其他-总和大小单双',
                                             playmenthod='玩法:时时彩-M6_5分彩-五星-其他-总和大小单双', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-五星-其他-总和大小单双')

    def top4_direct_duplex(self):
        self.s.wait_activity = 5
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=3, num10_19=14, num20_29=25, num30_39_1=36)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-前四-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-直选-直选复式')
        choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=3, num10_19=14, num20_29=25, num30_39_1=36)

        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-前四-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-直选-直选复式')

    def top4_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前四-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='1234')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-五星-前四-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-直选-直选单式')

        choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前四-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='1234')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-直选-直选单式',
                                             scenes='玩法:时时彩-M6_5分彩-前四-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-直选-直选单式')

    def top4_direct_selection(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='前四组合')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-直选-前四组合', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前四-直选-前四组合', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-直选-前四组合',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-直选-前四组合', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-直选-前四组合')

        choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='前四组合')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-直选-前四组合', scenes='玩法:时时彩-M6_5分彩-前四-直选-前四组合',
                                             keys='组合'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-直选-前四组合',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-直选-前四组合', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-直选-前四组合')

    def top4_group_slection24(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选24')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-组选-组合24', num=0, exnum='0')  # 页面选号断言
        for i in range(4):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前四-组选-组选24', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-组选-组选24',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选24', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选24')

        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选24')  # 选择玩法
        for i in range(4):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=i).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-组选-组选24', scenes='玩法:时时彩-M6_5分彩-前四-组选-组选24',
                                             keys='组合'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-组选-组选24',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选24', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选24')

    def top4_group_slection12(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选12')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-组选-组合12', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=11).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前四-组选-组选12', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-组选-组选12',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选12', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选12')

        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选12')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=11).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-组选-组选12', scenes='玩法:时时彩-M6_5分彩-前四-组选-组选12',
                                             keys='组合'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-组选-组选12',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选12', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选12')

    def top4_group_slection6(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选6')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-组选-组选6', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前四-组选-组选6', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-组选-组选6',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选6', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选6')

        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选6')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-组选-组选6', scenes='玩法:时时彩-M6_5分彩-前四-组选-组选6',
                                             keys='组合'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-组选-组选6',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选6', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选6')

    def top4_group_slection4(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选4')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前四-组选-组选4', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前四-组选-组选4', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前四-组选-组选4',
                                         playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选4', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选4')

        choose_betstyle(self, betstyle_1='前四', betstyle_2='组选', betstyle_3='组选4')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前四-组选-组选4', scenes='玩法:时时彩-M6_5分彩-前四-组选-组选4',
                                             keys='组合'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-前四-组选-组选4',
                                             playmenthod='玩法:时时彩-M6_5分彩-前四-组选-组选4', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前四-组选-组选4')

    def top3_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选复式')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-直选-直选复式', scenes='玩法:时时彩-M6_5分彩-前三-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选复式')

    def top3_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前三-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='123')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选单式')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='123')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-直选-直选单式', scenes='玩法:时时彩-M6_5分彩-前三-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选单式')

    def top3_direct_selection(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='前三组合')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-直选-前三组合', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-直选-前三组合', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-直选-前三组合',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-直选-前三组合', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-前三组合')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='前三组合')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-直选-前三组合', scenes='玩法:时时彩-M6_5分彩-前三-直选-前三组合',
                                             keys='组合',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-直选-前三组合',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-直选-前三组合', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-前三组合')

    # 前三直选跨度
    def top3_direct_span(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-直选-直选跨度', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-直选-直选跨度',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选跨度')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-直选-直选跨度', scenes='玩法:时时彩-M6_5分彩-前三-直选-直选跨度',
                                             keys_2='跨度',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-直选-直选跨度',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选跨度')

    # 前三直选跨度
    def top3_direct_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-直选-直选跨度', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-直选-直选跨度',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选跨度')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-直选-直选跨度',
                                             scenes='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', keys_2='跨度',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-直选-直选跨度',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-直选-直选跨度', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-直选-直选跨度')
        # 前三直选跨度

    def top3_group3_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-组选-组三复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-组选-组三复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-组选-组三复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组三复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组三复式')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-组选-组三复式', keys_2='组三复式',
                                             scenes='玩法:时时彩-M6_5分彩-前三-组选-组三复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-组选-组三复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组三复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组三复式')

    def top3_group3_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前三-组选-组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='122')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-组选-组三单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-组选-组三单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组三单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组三单式')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='122')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-组选-组三单式',
                                             scenes='玩法:时时彩-M6_5分彩-前三-组选-组三单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-组选-组三单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组三单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组三单式')

    def top3_group6_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-组选-组六复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-组选-组六复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-组选-组六复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组六复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组六复式')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-组选-组六复式',
                                             scenes='玩法:时时彩-M6_5分彩-前三-组选-组六复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-组选-组六复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组六复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组六复式')

    def top3_group6_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前三-组选-组六单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='142')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-组选-组六单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-组选-组六单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组六单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组六单式')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='142')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-组选-组六单式',
                                             scenes='玩法:时时彩-M6_5分彩-前三-组选-组六单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-组选-组六单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组六单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组六单式')

    def top3_group_mix(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前三-组选-混合组选')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-组选-混合组选', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-组选-混合组选',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-组选-混合组选', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-混合组选')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-组选-混合组选',
                                             scenes='玩法:时时彩-M6_5分彩-前三-组选-混合组选',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-组选-混合组选',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-组选-混合组选', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-混合组选')

    def top3_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-组选-组选和值', num=0, exnum='1')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前三-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前三-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组选和值')

        choose_betstyle(self, betstyle_1='前三', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前三-组选-组选和值', keys_2='前三组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-前三-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前三-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-前三-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前三-组选-组选和值')

    def mid3_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选复式')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-中三-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选复式')

    def mid3_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-中三-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='134')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选单式')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='134')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-直选-直选单式',
                                             scenes='玩法:时时彩-M6_5分彩-中三-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选单式')

    def mid3_direct_selection(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='中三组合')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-直选-中三组合', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-直选-中三组合', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-直选-中三组合',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-直选-中三组合', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-中三组合')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='中三组合')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-直选-中三组合', keys='组合',
                                             scenes='玩法:时时彩-M6_5分彩-中三-直选-中三组合',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-直选-中三组合',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-直选-中三组合', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-中三组合')

    def mid3_direct_span(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-直选-直选跨度', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-直选-直选跨度', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-直选-直选跨度',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选跨度', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选跨度')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-直选-直选跨度', keys_2='跨度',
                                             scenes='玩法:时时彩-M6_5分彩-中三-直选-直选跨度',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-直选-直选跨度',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选跨度', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选跨度')

    def mid3_direct_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-直选-直选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-直选-直选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选和值')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-直选-直选和值', keys_2='中三直选和值',
                                             scenes='玩法:时时彩-M6_5分彩-中三-直选-直选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-直选-直选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选和值')

    def mid3_group3_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-组选-组三复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-组选-组三复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-组选-组三复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组三复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组三复式')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-组选-组三复式', keys_2='组三复式',
                                             scenes='玩法:时时彩-M6_5分彩-中三-组选-组三复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-组三复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组三复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组三复式')

    def mid3_group3_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-中三-组选-组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-组选-组三单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-组选-组三单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组三单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组三单式')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-组选-组三单式',
                                             scenes='玩法:时时彩-M6_5分彩-中三-组选-组三单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-组三单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组三单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组三单式')

    def mid3_group6_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-组选-组六复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-组选-组六复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-组选-组六复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组六复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组六复式')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-组选-组六复式',
                                             scenes='玩法:时时彩-M6_5分彩-中三-组选-组六复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-组六复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组六复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组六复式')

    def mid3_group6_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-中三-组选-组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='146')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-组选-组六单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-组选-组六单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组六单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组六单式')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='145')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-组选-组六单式',
                                             scenes='玩法:时时彩-M6_5分彩-中三-组选-组六单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-组六单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组六单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组六单式')

    def mid3_group_mix(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-中三-组选-混合组选')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='166')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-组选-混合组选', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-组选-混合组选',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-组选-混合组选', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-混合组选')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='155')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-组选-混合组选',
                                             scenes='玩法:时时彩-M6_5分彩-中三-组选-混合组选',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-混合组选',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-组选-混合组选', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-混合组选')

    def mid3_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-组选-组三复式', num=0, exnum='1')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组选和值')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-组选-组选和值', keys_2='中三组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-中三-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-组选-组选和值')

    def last3_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后三-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-直选复式')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-后三-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-直选复式')

    def last3_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-后三-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='134')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-直选单式')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='134')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-直选-直选单式',
                                             scenes='玩法:时时彩-M6_5分彩-后三-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-直选单式')

    def last3_direct_selection(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='后三组合')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后三-直选-后三组合', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-直选-后三组合', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-直选-后三组合',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-直选-后三组合', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-后三组合')
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='后三组合')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13, num20_29=24)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-直选-后三组合', keys='组合',
                                             scenes='玩法:时时彩-M6_5分彩-后三-直选-后三组合',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-直选-后三组合',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-直选-后三组合', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-后三组合')

    def last3_direct_span(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后三-直选-直选跨度', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-直选-直选跨度', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-直选-直选跨度',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-直选-直选跨度', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-直选跨度')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='直选', betstyle_3='直选跨度')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-直选-直选跨度', keys_2='跨度',
                                             scenes='玩法:时时彩-M6_5分彩-后三-直选-直选跨度',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-直选-直选跨度',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-直选-直选跨度', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-直选-直选跨度')

    def last3_direct_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-中三-直选-直选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-中三-直选-直选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选和值')

        choose_betstyle(self, betstyle_1='中三', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-中三-直选-直选和值', keys_2='中三直选和值',
                                             scenes='玩法:时时彩-M6_5分彩-中三-直选-直选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-直选-直选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-中三-直选-直选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-中三-直选-直选和值')

    def last3_group3_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-中三-组选-组三复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-组选-组三复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-组选-组三复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组三复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组三复式')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-组选-组三复式', keys_2='组三复式',
                                             scenes='玩法:时时彩-M6_5分彩-后三-组选-组三复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-组选-组三复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组三复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组三复式')

    def last3_group3_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-后三-组选-组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-组选-组三单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-组选-组三单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组三单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组三单式')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-组选-组三单式',
                                             scenes='玩法:时时彩-M6_5分彩-后三-组选-组三单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-组选-组三单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组三单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组三单式')

    def last3_group6_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后三-组选-组六复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-组选-组六复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-组选-组六复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组六复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组六复式')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-组选-组六复式',
                                             scenes='玩法:时时彩-M6_5分彩-后三-组选-组六复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-组选-组六复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组六复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组六复式')



    def last3_group6_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-后三-组选-组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='146')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-组选-组六单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-组选-组六单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组六单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组六单式')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='145')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-组选-组六单式',
                                             scenes='玩法:时时彩-M6_5分彩-后三-组选-组六单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-组选-组六单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组六单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组六单式')

    def last3_group_mix(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-后三-组选-混合组选')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='166')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-组选-混合组选', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-组选-混合组选',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-组选-混合组选', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-混合组选')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='155')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-组选-混合组选',
                                             scenes='玩法:时时彩-M6_5分彩-后三-组选-混合组选',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-中三-组选-混合组选',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-组选-混合组选', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-混合组选')

    def last3_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后三-组选-组三复式', num=0, exnum='1')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后三-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后三-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组选和值')

        choose_betstyle(self, betstyle_1='后三', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后三-组选-组选和值', keys_2='后三组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-后三-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后三-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-后三-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后三-组选-组选和值')

    def top2_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后三-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前二-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前二-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前二-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前二-直选-直选复式')

        choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前二-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-前二-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前二-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前二-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前二-直选-直选复式')

    def top2_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前二-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='13')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前二-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前二-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前二-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前二-直选-直选单式')

        choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='13')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前二-直选-直选单式',
                                             scenes='玩法:时时彩-M6_5分彩-前二-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前二-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前二-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前二-直选-直选单式')

    def top2_direct_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前二-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前二-直选-直选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前二-直选-直选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-前二-直选-直选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前二-直选-直选和值')

        choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前二-直选-直选和值', keys_2='前二直选和值',
                                             scenes='玩法:时时彩-M6_5分彩-前二-直选-直选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前二-直选-直选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-前二-直选-直选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前二-直选-直选和值')


    def top2_group_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前二', betstyle_2='组选', betstyle_3='组选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前二-组选-组选复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前二-组选-组选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前二-组选-组选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前二-组选-组选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前二-组选-组选复式')

        choose_betstyle(self, betstyle_1='前二', betstyle_2='组选', betstyle_3='组选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前二-组选-组选复式',
                                             scenes='玩法:时时彩-M6_5分彩-前二-组选-组选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前二-组选-组选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前二-组选-组选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前二-组选-组选复式')

    def top2_group_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前二', betstyle_2='组选', betstyle_3='组选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-前二-组选-组选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='14')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前二-组选-组选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前二-组选-组选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-前二-组选-组选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前二-组选-组选单式')

        choose_betstyle(self, betstyle_1='前二', betstyle_2='组选', betstyle_3='组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='14')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前二-组选-组选单式',
                                             scenes='玩法:时时彩-M6_5分彩-前二-组选-组选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前二-组选-组选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-前二-组选-组选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前二-组选-组选单式')

    def top2_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='前二', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前二-组选-组三复式', num=0, exnum='1')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-前二-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-前二-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-前二-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-前二-组选-组选和值')

        choose_betstyle(self, betstyle_1='前二', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-前二-组选-组选和值', keys_2='前二组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-前二-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-前二-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-前二-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-前二-组选-组选和值')


    def last2_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后二', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后二-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后二-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后二-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后二-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后二-直选-直选复式')

        choose_betstyle(self, betstyle_1='后二', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后二-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-后二-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后二-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后二-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后二-直选-直选复式')

    def last2_direct_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后二', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-后二-直选-直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='13')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后二-直选-直选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后二-直选-直选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后二-直选-直选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后二-直选-直选单式')

        choose_betstyle(self, betstyle_1='后二', betstyle_2='直选', betstyle_3='直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='13')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后二-直选-直选单式',
                                             scenes='玩法:时时彩-M6_5分彩-后二-直选-直选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后二-直选-直选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后二-直选-直选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后二-直选-直选单式')


    def last2_direct_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后二', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后二-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后二-直选-直选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后二-直选-直选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-后二-直选-直选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后二-直选-直选和值')

        choose_betstyle(self, betstyle_1='后二', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后二-直选-直选和值', keys_2='后二直选和值',
                                             scenes='玩法:时时彩-M6_5分彩-后二-直选-直选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后二-直选-直选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-后二-直选-直选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后二-直选-直选和值')
    def last2_group_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后二', betstyle_2='组选', betstyle_3='组选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后二-组选-组选复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后二-组选-组选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后二-组选-组选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后二-组选-组选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后二-组选-组选复式')

        choose_betstyle(self, betstyle_1='后二', betstyle_2='组选', betstyle_3='组选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后二-组选-组选复式',
                                             scenes='玩法:时时彩-M6_5分彩-后二-组选-组选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后二-组选-组选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后二-组选-组选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后二-组选-组选复式')


    def last2_group_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后二', betstyle_2='组选', betstyle_3='组选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-后二-组选-组选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='14')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后二-组选-组选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后二-组选-组选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-后二-组选-组选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后二-组选-组选单式')

        choose_betstyle(self, betstyle_1='后二', betstyle_2='组选', betstyle_3='组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='14')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后二-组选-组选单式',
                                             scenes='玩法:时时彩-M6_5分彩-后二-组选-组选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后二-组选-组选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-后二-组选-组选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后二-组选-组选单式')



    def last2_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='后二', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-后二-组选-组选和值', num=0, exnum='1')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-后二-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-后二-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-后二-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-后二-组选-组选和值')

        choose_betstyle(self, betstyle_1='后二', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-后二-组选-组选和值', keys_2='前二组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-后二-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-后二-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-后二-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-后二-组选-组选和值')

    def M6_5_position(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='定位胆', betstyle_2='定位胆',instance2=1, betstyle_3='定位胆', instance3=2)  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-定位胆-定位胆-定位胆', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6,num10_19=13,num20_29=25,num30_39_1=36,num30_39_2=37)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-定位胆-定位胆-定位胆', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-定位胆-定位胆-定位胆',
                                         playmenthod='玩法:时时彩-M6_5分彩-定位胆-定位胆-定位胆', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-定位胆-定位胆-定位胆')
        choose_betstyle(self, betstyle_1='定位胆', betstyle_2='定位胆',instance2=1, betstyle_3='定位胆', instance3=2) # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=13, num20_29=25, num30_39_1=36, num30_39_2=37)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-定位胆-定位胆-定位胆', scenes='玩法:时时彩-M6_5分彩-定位胆-定位胆-定位胆',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-定位胆-定位胆-定位胆', playmenthod='玩法:时时彩-M6_5分彩-定位胆-定位胆-定位胆',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-定位胆-定位胆-定位胆')



    def random_position_5star_1(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='五星',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-五星-一码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-五星-一码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-五星-一码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-五星-一码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-五星-一码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='五星',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-五星-一码不定位', scenes='玩法:时时彩-M6_5分彩-不定位-五星-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-五星-一码不定位', playmenthod='玩法:时时彩-M6_5分彩-不定位-五星-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-五星-一码不定位')

    def random_position_5star_2(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='五星', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-五星-二码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=6,num10_19=8)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-五星-二码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-五星-二码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-五星-二码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-五星-二码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='五星', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6,num10_19=9)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-五星-二码不定位',
                                             scenes='玩法:时时彩-M6_5分彩-不定位-五星-二码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-五星-二码不定位',
                                             playmenthod='玩法:时时彩-M6_5分彩-不定位-五星-二码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-五星-二码不定位')


    def random_position_5star_3(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='五星', instance2=1, betstyle_3='三码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-五星-三码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=6,num10_19=8,num20_29=4)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-五星-三码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-五星-三码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-五星-三码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-五星-三码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='五星', instance2=1, betstyle_3='三码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6,num10_19=9,num20_29=8)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-五星-三码不定位',
                                             scenes='玩法:时时彩-M6_5分彩-不定位-五星-三码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-五星-三码不定位',
                                             playmenthod='玩法:时时彩-M6_5分彩-不定位-五星-三码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-五星-三码不定位')




    def random_position_top4_1(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前四',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-前四-一码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-前四-一码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-前四-一码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-前四-一码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-前四-一码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前四',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-前四-一码不定位', scenes='玩法:时时彩-M6_5分彩-不定位-前四-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-前四-一码不定位', playmenthod='玩法:时时彩-M6_5分彩-不定位-前四-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-前四-一码不定位')


    def random_position_last4_1(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='后四',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-后四-一码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-后四-一码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-后四-一码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-后四-一码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-后四-一码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前四',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-后四-一码不定位', scenes='玩法:时时彩-M6_5分彩-不定位-后四-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-后四-一码不定位', playmenthod='玩法:时时彩-M6_5分彩-不定位-后四-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-后四-一码不定位')



    def random_position_top3_1(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前三',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-前三-一码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-前三-一码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-前三-一码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-前三-一码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-前三-一码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前三',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-前三-一码不定位', scenes='玩法:时时彩-M6_5分彩-不定位-前三-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-前三-一码不定位', playmenthod='玩法:时时彩-M6_5分彩-不定位-前三-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-前三-一码不定位')

    def random_position_top3_2(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前三', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-前三-二码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=8)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-前三-二码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-前三-二码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-前三-二码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-前三-二码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前三', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=9)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-前三-二码不定位',
                                             scenes='玩法:时时彩-M6_5分彩-不定位-前三-二码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-前三-二码不定位',
                                             playmenthod='玩法:时时彩-M6_5分彩-不定位-前三-二码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-前三-二码不定位')

    def random_position_last3_1(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='后三',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-后三-一码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-后三-一码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-后三-一码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-后三-一码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-后三-一码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='前三',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-后三-一码不定位', scenes='玩法:时时彩-M6_5分彩-不定位-后三-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-后三-一码不定位', playmenthod='玩法:时时彩-M6_5分彩-不定位-后三-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-后三-一码不定位')

    def random_position_last3_2(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='后三', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-后三-二码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=8)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-后三-二码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-后三-二码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-后三-二码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-后三-二码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='后三', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=9)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-后三-二码不定位',
                                             scenes='玩法:时时彩-M6_5分彩-不定位-后三-二码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-后三-二码不定位',
                                             playmenthod='玩法:时时彩-M6_5分彩-不定位-后三-二码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-后三-二码不定位')

    def random_position_mid3_1(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='中三',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-中三-一码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self,num0_9=6)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-中三-一码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-中三-一码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-中三-一码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-中三-一码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='中三',instance2=1,betstyle_3='一码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-中三-一码不定位', scenes='玩法:时时彩-M6_5分彩-不定位-中三-一码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-中三-一码不定位', playmenthod='玩法:时时彩-M6_5分彩-不定位-中三-一码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-中三-一码不定位')

    def random_position_mid3_2(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='中三', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-不定位-中三-二码不定位', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=8)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-不定位-中三-二码不定位', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-不定位-中三-二码不定位',
                                         playmenthod='玩法:时时彩-M6_5分彩-不定位-中三-二码不定位', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-中三-二码不定位')
        choose_betstyle(self, betstyle_1='不定位', betstyle_2='中三', instance2=1, betstyle_3='二码不定位')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=6, num10_19=9)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-不定位-中三-二码不定位',
                                             scenes='玩法:时时彩-M6_5分彩-不定位-中三-二码不定位',
                                             case1='添加注单下注',
                                             gamename1='时时彩-M6_5分彩-不定位-中三-二码不定位',
                                             playmenthod='玩法:时时彩-M6_5分彩-不定位-中三-二码不定位',
                                             case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-不定位-中三-二码不定位')
    def random2_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选2', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选2-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选2-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选2-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选2-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-直选-直选复式')

        choose_betstyle(self, betstyle_1='任选2', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选2-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-任选2-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选2-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选2-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-直选-直选复式')


    def random2_dricet_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选2', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选2-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选2-直选-直选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选2-直选-直选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选2-直选-直选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-直选-直选和值')

        choose_betstyle(self, betstyle_1='任选2', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选2-直选-直选和值', keys_2='任性2直选和值',
                                             scenes='玩法:时时彩-M6_5分彩-任选2-直选-直选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选2-直选-直选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选2-直选-直选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-直选-直选和值')





    def random2_group_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选2', betstyle_2='组选', betstyle_3='组选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选2-组选-组选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=3)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选2-组选-组选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选2-组选-组选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选2-组选-组选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-组选-组选复式')

        choose_betstyle(self, betstyle_1='任选2', betstyle_2='组选', betstyle_3='组选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=3)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选2-组选-组选复式',
                                             scenes='玩法:时时彩-M6_5分彩-任选2-组选-组选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选2-组选-组选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选2-组选-组选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-组选-组选复式')


    def random2_group_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选2', betstyle_2='组选', betstyle_3='组选单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-任选2-组选-组选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='16')
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选2-组选-组选单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选2-组选-组选单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选2-组选-组选单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-组选-组选单式')

        choose_betstyle(self, betstyle_1='任选2', betstyle_2='组选', betstyle_3='组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='15')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选2-组选-组选单式',
                                             scenes='玩法:时时彩-M6_5分彩-任选2-组选-组选单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选2-组选-组选单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选2-组选-组选单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-组选-组选单式')


    def random2_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选2', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选2-组选-组选和值', num=0, exnum='1')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选2-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选2-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选2-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-组选-组选和值')

        choose_betstyle(self, betstyle_1='任选2', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选2-组选-组选和值',keys_2='任选2组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-任选2-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选2-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选2-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选2-组选-组选和值')

    def random3_direct_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选3-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13,num20_29=23,num30_39_1=36,num30_39_2=37)

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-直选-直选复式')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=13,num20_29=23,num30_39_1=36,num30_39_2=37)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-直选-直选复式',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-直选-直选复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-直选-直选复式')


    def random3_dircet_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选3-直选-直选和值', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-直选-直选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-直选-直选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-直选-直选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-直选-直选和值')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='直选', betstyle_3='直选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-直选-直选和值', keys_2='任性3直选和值',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-直选-直选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-直选-直选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-直选-直选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-直选-直选和值')


    def random3_group3_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-前三-组选-组三复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-组选-组三复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-组选-组三复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组三复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组三复式')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组三复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-组选-组三复式', keys_2='组三复式',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-组选-组三复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-组选-组三复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组三复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组三复式')

    def random3_group3_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-任选3-组选-组三单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='122')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-组选-组三单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-组选-组三单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组三单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组三单式')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组三单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='122')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-组选-组三单式',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-组选-组三单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-组选-组三单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组三单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组三单式')

    def random3_group6_duplex(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选3-组选-组六复式', num=0, exnum='0')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-组选-组六复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-组选-组六复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组六复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组六复式')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组六复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-组选-组六复式',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-组选-组六复式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-组选-组六复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组六复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组六复式')

    def random3_group6_single(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-任选3-组选-组六单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='142')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-组选-组六单式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-组选-组六单式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组六单式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组六单式')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组六单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='142')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-组选-组六单式',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-组选-组六单式',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-组选-组六单式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组六单式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组六单式')

    def random3_group_mix(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        page_text_avaliable(self, text='1234', style='M6_5分彩-任选3-组选-混合组选')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-组选-混合组选', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-组选-混合组选',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-混合组选', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-混合组选')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='混合组选')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='144')
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-组选-混合组选',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-组选-混合组选',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-组选-混合组选',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-混合组选', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-混合组选')

    def random3_group_sum(self):
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选3-组选-组选和值', num=0, exnum='1')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()

        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选3-组选-组选和值', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选3-组选-组选和值',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组选和值', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组选和值')

        choose_betstyle(self, betstyle_1='任选3', betstyle_2='组选', betstyle_3='组选和值')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选3-组选-组选和值', keys_2='任选3组选和值',
                                             scenes='玩法:时时彩-M6_5分彩-任选3-组选-组选和值',
                                             case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选3-组选-组选和值',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选3-组选-组选和值', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选3-组选-组选和值')

    def random4_driect_duplex(self):
        # self.s.implicitly_wait = 5
        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选4', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        page_number_avaliable(self, style='时时彩-M6_5分彩-任选4-直选-直选复式', num=0, exnum='0')  # 页面选号断言
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35, num30_39_2=35)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-任选4-直选-直选复式', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-任选4-直选-直选复式',
                                         playmenthod='玩法:时时彩-M6_5分彩-任选4-直选-直选复式', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-任选4-直选-直选复式')

        check_if_in_offical(self, text='五星-直选-直选复式', style='M6_5分彩')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='任选4', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
        M6_5_star5_direct_num_page(self, num0_9=2, num10_19=11, num20_29=22, num30_39_1=35, num30_39_2=35)
        # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
        add_betlist_verify_balance_back_game(self, style1='时时彩-M6_5分彩-任选4-直选-直选复式', scenes='玩法:时时彩-M6_5分彩-任选4-直选-直选复式'
                                             , case1='添加注单下注', gamename1='时时彩-M6_5分彩-任选4-直选-直选复式',
                                             playmenthod='玩法:时时彩-M6_5分彩-任选4-直选-直选复式', case2='添加注单金额验证',
                                             gamename2='时时彩', style2='M6-5分彩', menthod='时时彩-M6_5分彩-任选4-直选-直选复式')

    def gametown_M6_5_Integration(self):
        check_if_in_gametown(self, text='整合', style='时时彩-M6_5分彩')
        shadow_click(self)
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        self.s.swipe(fx=40,fy=1300,tx=40,ty=500)
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=1000)
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=17).click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=600)
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=600)
        self.s(text='龙').click()
        self.s(text='小',instance=0).click()
        self.s(text='小',instance=1).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-娱乐城-两面', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-娱乐城-两面',
                                         playmenthod='玩法:时时彩-M6_5分彩-娱乐城-两面', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-娱乐城-两面')

    def gametown_M6_5_TG(self):
        check_if_in_gametown(self, text='整合', style='时时彩-M6_5分彩')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='龙虎斗')  # 选择玩法
        self.s(text='龙', instance=0).click()
        self.s(text='龙', instance=1).click()
        self.s(text='龙', instance=2).click()
        self.s(text='和', instance=3).click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=800)
        self.s(text='龙', instance=1).click()
        self.s(text='龙', instance=2).click()
        self.s(text='和', instance=3).click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=800)
        self.s(text='龙', instance=1).click()
        self.s(text='虎', instance=2).click()
        self.s(text='和', instance=3).click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=800)
        self.s(text='和', instance=3).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-娱乐城-龙虎斗', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-娱乐城-龙虎斗',
                                         playmenthod='玩法:时时彩-M6_5分彩-娱乐城-龙虎斗', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-娱乐城-龙虎斗')

    def gametown_M6_5_ball1_ball5(self):
        for i in ['第一球','第二球','第三球','第四球','第五球']:
            check_if_in_gametown(self, text='整合', style='时时彩-M6_5分彩')
            shadow_click(self)
            choose_betstyle(self, betstyle_1=i)  # 选择玩法
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
            self.s(text='大', instance=0).click()
            self.s(text='小', instance=1).click()
            self.s.swipe(fx=40, fy=1300, tx=40, ty=400)
            self.s(text='顺子', instance=0).click()
            self.s(text='顺子', instance=1).click()
            self.s(text='豹子', instance=2).click()
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-娱乐城-%s'%i, case1='一键投注',
                                             gamename1='时时彩-M6_5分彩-娱乐城-%s'%i,
                                             playmenthod='玩法:时时彩-M6_5分彩-娱乐城-%s'%i, case2='一键投注金额验证',
                                             gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-娱乐城-%s'%i)

    def gametown_M6_5_one_in5(self):
        check_if_in_gametown(self, text='整合', style='时时彩-M6_5分彩')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='全五中ㄧ')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-娱乐城-全五中一', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-娱乐城-全五中一',
                                         playmenthod='玩法:时时彩-M6_5分彩-娱乐城-全五中一', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-娱乐城-全五中一')


    def gametown_M6_5_niuniu(self):
        check_if_in_gametown(self, text='整合', style='时时彩-M6_5分彩')
        shadow_click(self)
        choose_betstyle(self, betstyle_1='时时彩牛牛')  # 选择玩法
        self.s(text='牛大', instance=0).click()
        self.s(text='牛小', instance=0).click()
        self.s(text='牛双', instance=0).click()
        self.s(text='无牛', instance=0).click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:时时彩-M6_5分彩-娱乐城-时时彩牛牛', case1='一键投注',
                                         gamename1='时时彩-M6_5分彩-娱乐城-时时彩牛牛',
                                         playmenthod='玩法:时时彩-M6_5分彩-娱乐城-时时彩牛牛', case2='一键投注金额验证',
                                         gamename2='时时彩', style='M6-5分彩', menthod='时时彩-M6_5分彩-娱乐城-时时彩牛牛')

if __name__ == '__main__':
    M = M65()
    M.star5_driect_duplex()
    M.star5_driect_selection()
    M.star5_direct_single()
    # M.star5_group_120()
    # M.star5_group_60()
    # M.star5_group_30()
    # M.star5_group_20()
    # M.star5_group_10()
    # M.star5_group_5()
    # M.star5_other_TGsum()
    # M.star5_other_dxds()
    #
    # M.top4_direct_duplex()
    # M.top4_direct_single()
    # M.top4_direct_selection()
    # M.top4_group_slection24()
    # M.top4_group_slection12()
    # M.top4_group_slection6()
    # M.top4_group_slection4()
    #
    # M.top3_direct_duplex()
    # M.top3_direct_single()
    # M.top3_direct_selection()
    # M.top3_direct_span()
    # M.top3_group3_duplex()
    # M.top3_group3_single()
    # M.top3_group6_duplex()
    # M.top3_group6_single()
    # M.top3_group_mix()
    # M.top3_group_sum()
    #
    # M.mid3_direct_duplex()
    # M.mid3_direct_single()
    # M.mid3_direct_selection()
    # M.mid3_direct_span()
    # M.mid3_direct_sum()
    # M.mid3_group3_duplex()
    # M.mid3_group3_single()
    # M.mid3_group6_duplex()
    # M.mid3_group6_single()
    # M.mid3_group_mix()
    # M.mid3_group_sum()
    #
    # M.last3_direct_duplex()
    # M.last3_direct_single()
    # M.last3_direct_selection()
    # M.last3_direct_span()
    # M.mid3_direct_sum()
    # M.last3_group3_duplex()
    # M.last3_group3_single()
    # M.last3_group6_duplex()
    # M.last3_group6_single()
    # M.last3_group_mix()
    # M.last3_group_sum()
    #
    # M.top2_direct_duplex()
    # M.top2_direct_single()
    # M.top2_direct_sum()
    # M.top2_group_duplex()
    # M.top2_group_single()
    # M.top2_group_sum()
    #
    # M.last2_direct_duplex()
    # M.last2_direct_single()
    # M.last2_direct_sum()
    # M.last2_group_duplex()
    # M.last2_group_single()
    # M.last2_group_sum()
    #
    # M.M6_5_position()
    #
    # M.random_position_5star_1()
    # M.random_position_5star_2()
    # M.random_position_5star_3()
    # M.random_position_top4_1()
    # M.random_position_last4_1()
    # M.random_position_top3_1()
    # M.random_position_top3_2()
    # M.random_position_last3_1()
    # M.random_position_last3_2()
    # M.random_position_mid3_1()
    # M.random_position_mid3_2()
    #
    # M.random2_direct_duplex()
    # M.random2_dricet_sum()
    # M.random2_group_duplex()
    # M.random2_group_sum()
    # M.random2_group_single()
    #
    # M.random3_direct_duplex()
    M.random3_dircet_sum()
    # M.random3_group3_duplex()
    # M.random3_group3_single()
    # M.random3_group6_duplex()
    # M.random3_group6_single()
    # M.random3_group_mix()
    # M.random3_group_sum()
    #
    # M.random4_driect_duplex()

    # M.gametown_M6_5_Integration()
    # M.gametown_M6_5_TG()
    # M.gametown_M6_5_ball1_ball5()
    # M.gametown_M6_5_one_in5()
    # M.gametown_M6_5_niuniu()