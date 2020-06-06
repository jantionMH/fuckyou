import uiautomator2

from uiautomator3D.publicomponent.assertion import assert_presence, assert_equal_bet, page_number_avaliable, \
    add_list_and_assert, page_text_avaliable
from uiautomator3D.publicomponent.bettingwidget import oneclick_bet, add_list_bet
from uiautomator3D.publicomponent.others import game_back_to_check_balance, balance_back_to_game, \
    get_c_balance_and_check, check_if_in_gametown, check_if_in_offical, choose_betstyle, random_add_5, \
    gamtown_11c5_randomchoose, gametown_11c5_TG


class login_to_11c5:
    def __init__(self):
        phone = uiautomator2.connect('127.0.0.1:62001')
        print(phone.device_info)
        phone.app_start('com.yy.sport')
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

        login_text = self.s(text="M6体育").get_text()
        assert_presence(self, expect='M6体育', actual=login_text, case='登录测试', scenes='进入首页')

        self.s(description="娱乐").click()
        self.s().must_wait(2)
        self.s.swipe(fx=448, fy=1350, tx=448, ty=250, duration=0.5)
        self.s().must_wait(2)
        self.s(resourceId="com.yy.sport:id/home_imageview2", instance=4).click()

        caipiao_text = self.s(text="彩票").get_text()
        assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')

        self.s(text="十一选五").click()
        self.s().must_wait = 1
        self.s(text="上海11选5").click(timeout=1)

        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='进入上海11选5', scenes='进入游戏')

    def top3_direct_duplex(self):

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前三直选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=18).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=28).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前三直选复式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前三直选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前三直选复式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三直选复式')

        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=18).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=28).click()
        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前三直选复式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前三直选复式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前三直选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前三直选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前三直选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三直选复式')

    def top3_direct_single(self):
        check_if_in_offical(self, text='三码-直选-前三直选复式', style='上海11选5')  # 检查当前页面是否为官方玩法页面
        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03 05', style='上海11选5-前三直选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前三直选单式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前三直选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前三直选单式',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三直选复式')

        choose_betstyle(self, betstyle_1='三码', betstyle_2='直选', betstyle_3='前三直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前三直选单式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前三直选单式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前三直选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前三直选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前三直选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三直选单式')

    def top3_group_duplex(self):
        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前三组选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前三组选复式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前三组选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前三组选复式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三组选复式')

        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前三组选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前三组选复式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前三组选复式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前三组选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前三组选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前三组选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三组选复式')

    def top3_group_single(self):
        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03 05', style='上海11选5-前三组选单式')  # 检查文本框可输入

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前三组选单式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前三组选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前三组选单式',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三组选单式')

        choose_betstyle(self, betstyle_1='三码', betstyle_2='组选', betstyle_3='前三组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03 06')

        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前三组选单式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前三组选单式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前三组选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前三组选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前三组选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前三组选单式')

    def top2_direct_duplex(self):
        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前二直选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前二直选复式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前二直选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前二直选复式',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二直选复式')

        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()

        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前二直选复式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前二直选复式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前二直选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前二直选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前二直选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二直选复式')

    def top2_direct_single(self):
        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03', style='上海11选5-前二直选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前二直选单式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前二直选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前二直选单式',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二直选单式')

        choose_betstyle(self, betstyle_1='二码', betstyle_2='直选', betstyle_3='前二直选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')
        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前二直选单式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前二直选单式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前二直选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前二直选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前二直选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二直选单式')

    def top2_group_duplex(self):
        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选复式')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-前二组选复式', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前二组选复式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前二组选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前二组选复式',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二组选复式')

        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选复式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前二组选复式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前二组选复式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前二组选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前二组选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前二组选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二组选复式')

    def top2_group_single(self):
        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选单式')  # 选择玩法
        page_text_avaliable(self, text='01 03', style='上海11选5-前二组选单式')  # 检查文本框可输入
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-前二组选单式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-前二组选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-前二组选单式',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二组选单式')

        choose_betstyle(self, betstyle_1='二码', betstyle_2='组选', betstyle_3='前二组选单式')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='01 03')
        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-前二组选单式')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-前二组选单式')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-前二组选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-前二组选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-前二组选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='前二组选单式')

    def position_11c5(self):

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='定位胆', instance=0).click()
        self.s(text='定位胆', instance=2).click()
        page_number_avaliable(self, style='上海11选5-定位胆', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-定位胆', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-定位胆')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-定位胆',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='定位胆')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='定位胆', instance=0).click()
        self.s(text='定位胆', instance=2).click()

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-定位胆')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-定位胆')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-定位胆', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-定位胆')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-定位胆',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='定位胆')

    def random_position_11c5(self):

        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', betstyle_3='前三位')  # 选择玩法
        page_number_avaliable(self, style='上海11选5-不定位', num=0, exnum='01')  # 页面选号断言
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-不定位', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-不定位')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-不定位',
                                case='一键投注金额验证')
        # 返回页面并断言
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='不定位')

        choose_betstyle(self, betstyle_1='不定位', betstyle_2='不定位', betstyle_3='前三位')  # 选择玩法
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 添加注单并断言
        add_list_and_assert(self, style='上海11选5-不定位')
        # 随机加5注并断言
        random_add_5(self, style='上海11选5-不定位')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:上海11选5-不定位', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '上海11选5-不定位')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:上海11选5-不定位',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='不定位')

    def gametown_11c5_two_sides(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-两面', num=0, exnum='大')

        self.s(text='小', instance=0).click()
        self.s(text='大', instance=1).click()
        self.s(text='小', instance=2).click()
        self.s().swipe('up', steps=10)
        self.s(text='小', instance=1).click()
        self.s(text='小', instance=2).click()
        self.s(text='小', instance=3).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-两面', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-两面')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-两面',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-两面')

    def gametown_11c5_ball_1(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='第一球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第一球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-第一球', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-第一球')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-第一球',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第一球')

    def gametown_11c5_ball_2(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='第二球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第二球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-第二球', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-第二球')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-第二球',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第二球')

    def gametown_11c5_ball_3(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='第三球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第三球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-第三球', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-第三球')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-第三球',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第三球')

    def gametown_11c5_ball_4(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='第四球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第四球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-第四球', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-第四球')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-第四球',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第四球')

    def gametown_11c5_ball_5(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='第五球')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-第五球', num=0, exnum='1')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(text='大', instance=0).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-第五球', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-第五球')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-第五球',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-第五球')

    def gametown_11c5_ball_random(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='任选')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-任选', num=0, exnum='1')
        gamtown_11c5_randomchoose(self)
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-任选', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-任选')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-任选',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-任选')


    def gametown_11c5_ball_TG(self):
        check_if_in_gametown(self, text='两面', style='上海11选5-娱乐城')
        choose_betstyle(self, betstyle_1='龙虎斗')  # 选择玩法
        # 页面选号
        page_number_avaliable(self, style='上海11选5-娱乐城-龙虎斗', num=0, exnum='龙')
        gametown_11c5_TG(self)


        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:上海11选5-娱乐城-龙虎斗', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '上海11选5-娱乐城-龙虎斗')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:上海11选5-娱乐城-龙虎斗',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='十一选五', style='上海11选5', menthod='上海11选5-娱乐城-龙虎斗')
if __name__ == '__main__':
    lt_11c5 = login_to_11c5()
    # lt_11c5.top3_direct_duplex()
    # lt_11c5.top3_direct_single()
    # lt_11c5.top3_group_duplex()
    # lt_11c5.top3_group_single()
    # lt_11c5.top2_direct_duplex()
    # lt_11c5.top2_direct_single()
    # lt_11c5.top2_group_duplex()
    # lt_11c5. top2_group_single()
    # lt_11c5.position_11c5()
    # lt_11c5.random_position_11c5()
    # lt_11c5.gametown_11c5_two_sides()
    # lt_11c5.gametown_11c5_ball_1()
    # lt_11c5.gametown_11c5_ball_2()
    # lt_11c5.gametown_11c5_ball_3()
    # lt_11c5.gametown_11c5_ball_4()
    # lt_11c5.gametown_11c5_ball_5()
    # lt_11c5.gametown_11c5_ball_random()
    lt_11c5.gametown_11c5_ball_TG()
