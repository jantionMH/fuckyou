import uiautomator2

from uiautomator2test.publicomponent.assertion import assert_equal_bet, assert_presence
from uiautomator2test.publicomponent.bettingwidget import oneclick_bet, add_list_bet
from uiautomator2test.publicomponent.others import game_back_to_check_balance, get_c_balance_and_check, \
    balance_back_to_game


class login_to_game3d:

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

        self.s(text="3D彩").click()
        self.s().must_wait = 1
        self.s(text="福彩3D").click()

        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='进入3D福彩投注页面', scenes='进入游戏')

    def game_3d_basic(self):
        """
        基础就是默认的玩法：3星-直选-直选复式
        """
        try:
            page_text = self.s(text='三星-直选-直选复式').get_text()
            assert_presence(self, expect='三星-直选-直选复式', actual=page_text, case='进入官方玩法页面', scenes="玩法:3D游戏-官方玩法")

        except:
            self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
            self.s(text='官方玩法').click()

        num_text = self.s(text='8', instance=2).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D-3星直选复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D-3星直选复式', case='一键投注')
        # 断言：返回上级
        game_back_to_check_balance(self, '3D-3星直选复式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D-3星直选复式', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D')
        self.s().must_wait = 2
        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:3D-3星直选复式')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()
        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星直选复式', case='添加注单')
        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星直选复式', case='随机添加5注')
        # 确认下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D-3星直选复式', case='注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D-3星直选复式')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-3星直选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D',menthod='3D-3星直选复式')

    def game_3d_3star_direct_selection_single(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='直选单式').click()
        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('111')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='111', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-3星直选单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, case='一键投注', scenes='玩法：3D游戏-3星直选单式')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星直选单式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D-3星直选单式', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星直选复式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='直选单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星直选单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星直选单式', case='随机添加5注')
        # 添加注单下注
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, case='注单下注', scenes='玩法:3D-3星直选单式')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星直选单式')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-3星直选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星直选复式')

    def game_3d_3star_direct_selection_sum(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='直选和值').click()

        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D-3星直选和值', case='页面选号')

        self.s(text='4').click()
        self.s(text='16').click()
        self.s(text='27').click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D-3星直选和值', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D-3星直选和值')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D-3星直选和值', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星直选和值')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='直选和值').click()
        self.s(text='4').click()
        self.s(text='16').click()
        self.s(text='27').click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星直选和值', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星直选和值', case='随机添加5注')
        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D-3星直选和值', case='添加注单下注')

        # 返回上级:包含断言
        game_back_to_check_balance(self, '3D-3星直选和值')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-3星直选和值',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星直选和值')

    def game_3d_3star_group_selection_3snigle(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组三单式').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('111')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='111', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-3星组三单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, case='一键投注', scenes='玩法：3D游戏-3星组三单式')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星组三单式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-3星组三单式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组三单式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组三单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星组三单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星组三单式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D-3星组三单式', case='添加注单')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星组三单式')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-3星组三单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组三单式')

    def game_3d_3star_group_selection_3duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组三复式').click()
        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D-3星组三复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D-3星组三复式', case='一键投注')
        # 返回上级断言
        game_back_to_check_balance(self, '3D-3星组三复式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D-3星组三复式', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组三复式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组三复式').click()

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星组三复式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星组三复式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D-3星组三复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D-3星组三复式')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-3星组三复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组三复式')

    def game_3d_3star_group_selection_6snigle(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组六单式').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('111')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='111', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-3星组六单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法：3D游戏-3星组六单式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星组六单式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-3星组六单式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组六单式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组六单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星组六单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星组六单式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法：3D游戏-3星组六单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星组六单式')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-3星组六单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组六单式')

    def game_3d_3star_group_selection_6duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组六复式').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-3星组六复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-3星组六复式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星组六复式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-3星组六复式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组六复式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组六复式').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-3星组六复式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-3星组六复式', case='随机添加5注')
        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D-3星组六复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-3星组六复式')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-3星组六复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-3星组六复式')

    def game_3d_3star_group_selection_mix_duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='混合组选').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('111')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='111', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-混合组选')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法：3D游戏-混合组选', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-混合组选')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-混合组选', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-混合组选')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='混合组选').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='226,223,456')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-混合组选', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-混合组选', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法：3D游戏-混合组选', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-混合组选')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-混合组选',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-混合组选')

    def game_3d_3star_group_selection_sum_duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组选和值').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-组选和值', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=19).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-组选和值', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-组选和值')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-组选和值', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-组选和值')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='组选').click()
        self.s(text='组选和值').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=19).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=24).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-组选和值', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-组选和值', case='随机添加5注')
        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-组选和值', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-组选和值')

        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-组选和值',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-组选和值')

    def game_3d_2star_top2_direct_duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='前二直选复式').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-2星前二直选复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-2星前二直选复式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二直选复式')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-2星前二直选复式', case='一键投注')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二直选复式')
        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:33D游戏-2星前二直选复式')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='前二直选复式').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D游戏-2星前二直选复式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D游戏-2星前二直选复式', case='随机添加5注')
        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-2星前二直选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二直选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-2星前二直选复式',
                                case='添加注单')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二直选复式')

    def game_3d_2star_top2_direct_single(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='前二直选单式').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('11')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='11', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-2星前二直选单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法：3D游戏-2星前二直选单式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二直选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-2星前二直选单式', case='一键投注')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二直选单式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='前二直选单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D游戏-2星前二直选单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D游戏-2星前二直选单式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法：3D游戏-2星前二直选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二直选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-2星前二直选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二直选单式')

    def game_3d_2star_last2_direct_duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='后二直选复式').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-2星后二直选复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-2星后二直选复式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二直选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-2星后二直选复式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二直选复式')
        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:3D游戏-2星后二直选复式')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='后二直选复式').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-2星后二直选复式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-2星后二直选复式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-2星后二直选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二直选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-2星后二直选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二直选复式')

    def game_3d_2star_last2_direct_single(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='后二直选单式').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('11')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='11', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-2星后二直选单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='86')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法：3D游戏-后二直选单式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二直选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-2星后二直选单式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二直选单式')
        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:3D游戏-2星后二直选单式')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='后二直选单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='86')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-2星后二直选单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-2星后二直选单式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法：3D游戏-2星后二直选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二直选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-2星后二直选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二直选单式')

    def game_3d_2star_top2_group_duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='前二组选复式').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-2星前二组选复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-2星前二组选复式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二组选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-2星前二组选复式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二组选复式')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='前二组选复式').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-2星前二组选复式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-2星前二组选复式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-2星前二组选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二组选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-2星前二组选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二组选复式')

    def game_3d_2star_top2_group_single(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='前二组选单式').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('11')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='11', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-2星前二组选单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法：3D游戏-2星前二组选单式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二组选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-2星前二组选单式', case='一键投注')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二组选单式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='前二组选单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='22,23,46')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-2星前二组选单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-2星前二组选单式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法：3D游戏-2星前二组选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星前二组选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-2星前二组选单式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星前二组选单式')

    def game_3d_2star_last2_group_duplex(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='后二组选复式').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-2星后二组选复式', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-2星后二组选复式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二组选复式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-2星后二组选复式', case='一键投注')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二组选复式')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='后二组选复式').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-2星后二组选复式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-2星后二组选复式', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-2星后二组选复式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二组选复式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-2星后二组选复式',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二组选复式')

    def game_3d_2star_last2_group_single(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='后二组选单式').click()

        # 页面断言
        self.s(resourceId='com.yy.sport:id/tv_text').set_text('11')
        page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
        assert_presence(self, expect='11', actual=page_text_2, case='页面输入', scenes='玩法：3D游戏-2星后二组选单式')

        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='92,73,46')
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法：3D游戏-2星后二组选单式', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二组选单式')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法：3D游戏-2星后二组选单式',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二组选单式')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二星').click()
        self.s(text='组选').click()
        self.s(text='后二组选单式').click()
        self.s(resourceId='com.yy.sport:id/tv_text').send_keys(text='92,73,46')

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-2星后二组选单式', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-2星后二组选单式', case='随机添加5注')
        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法：3D游戏-2星后二组选单式', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '3D游戏-2星后二组选单式')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法：3D游戏-2星后二组选单式',
                                case='添加注单验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-2星后二组选单式')

    def position(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='定位胆', instance=0).click()
        self.s(text='定位胆', instance=2).click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-定位胆', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=25).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-定位胆', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '定位胆')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-定位胆', case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-定位胆')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='定位胆', instance=0).click()
        self.s(text='定位胆', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=25).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-定位胆', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-定位胆', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-定位胆', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '定位胆')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-定位胆',
                                case='添加注单验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-定位胆')

    def random_postion_1(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='不定位', instance=0).click()
        self.s(text='一码不定位').click()
        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-一码不定位', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-一码不定位', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '一码不定位')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-一码不定位',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-一码不定位')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='不定位', instance=0).click()
        self.s(text='一码不定位').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-一码不定位', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-一码不定位', case='随机添加5注')
        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-一码不定位', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '一码不定位')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='3d游戏3星一码不定位',
                                case='添加注单验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-一码不定位')

    def random_postion_2(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='不定位', instance=0).click()
        self.s(text='二码不定位').click()

        # 页面选号断言
        num_text = self.s(text='8', instance=0).get_text()
        assert_presence(self, expect='8', actual=num_text, scenes='玩法:3D游戏-二码不定位', case='页面选号')

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-二码不定位', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '二码不定位')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-二码不定位',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-二码不定位')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='不定位', instance=0).click()
        self.s(text='二码不定位').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-二码不定位', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-二码不定位', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-二码不定位', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '二码不定位')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-一码不定位',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-二码不定位')

    def dxds_top2(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='大小单双', instance=0).click()
        self.s(text='前二大小单双').click()

        # 页面选号断言
        num_text = self.s(text='单', instance=0).get_text()
        assert_presence(self, expect='单', actual=num_text, scenes='玩法:3D游戏-前二大小单双', case='页面选号')

        self.s(text='单', instance=0).click()
        self.s(text='大', instance=1).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-前二大小单双', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '前二大小单双')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-前二大小单双',
                                case='一键投注金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-前二大小单双')


        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='大小单双', instance=0).click()
        self.s(text='前二大小单双').click()
        self.s(text='单', instance=0).click()
        self.s(text='大', instance=1).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-前二大小单双', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-前二大小单双', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-前二大小单双', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '前二大小单双')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D游戏-前二大小单双',
                                case='添加注单金额验证')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-前二大小单双')

    def dxds_last2(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='大小单双', instance=0).click()
        self.s(text='后二大小单双').click()
        # 页面选号断言
        num_text = self.s(text='单', instance=0).get_text()
        assert_presence(self, expect='单', actual=num_text, scenes='玩法:3D游戏-后二大小单双', case='页面选号')

        self.s(text='双', instance=0).click()
        self.s(text='小', instance=1).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D游戏-后二大小单双', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '后二大小单双')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D游戏-后二大小单双', case='一键投注')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-后二大小单双')
        game_text = self.s(text="玩法").get_text()
        assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:3D游戏-后二大小单双')

        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='大小单双', instance=0).click()
        self.s(text='后二大小单双').click()
        self.s(text='双', instance=0).click()
        self.s(text='小', instance=1).click()

        self.s(text='添加注单').click()
        page_text_1 = self.s(text='投注单').get_text()
        assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:3D-后二大小单双', case='添加注单')

        self.s(text='+机选5注').click()
        betlist_count = self.s(resourceId='com.yy.sport:id/tv_bet_content').count
        assert_presence(self, expect=6, actual=betlist_count, scenes='玩法:3D-后二大小单双', case='随机添加5注')

        # 添加注单
        betsadd = add_list_bet(self)
        # 断言：下注成功
        assert_equal_bet(self, scenes='玩法:3D游戏-后二大小单双', case='添加注单下注')
        # 返回上级
        game_back_to_check_balance(self, '后二大小单双')
        # 断言：添加注单验证金额
        get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod='玩法:3D-后二大小单双',
                                case='添加注单')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D-后二大小单双')

    def gametown_3D_position_1(self):
        try:
            page_text = self.s(text='一字定位').get_text()
            assert_presence(self, expect='一字定位', actual=page_text, case='进入娱乐城页面', scenes="玩法:3D娱乐城一字定位-百")

        except:
            self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
            self.s(text='娱乐城玩法').click()

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(text='单').click()
        self.s(text='合数').click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城一字定位-百', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城一字定位-百')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城一字定位-百',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城一字定位-百')

        # 切换到娱乐城
        try:
            page_text = self.s(text='一字定位').get_text()
            assert_presence(self, expect='一字定位', actual=page_text, case='进入娱乐城页面', scenes="玩法:3D娱乐城一字定位")

        except:
            self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
            self.s(text='娱乐城玩法').click()

        self.s(text='十定位').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(text='单').click()
        self.s(text='合数').click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城一字定位-十', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城一字定位-十')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城一字定位-十',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城一字定位-十')

        # 切换到娱乐城
        try:
            page_text = self.s(text='一字定位').get_text()
            assert_presence(self, expect='一字定位', actual=page_text, case='进入娱乐城页面', scenes="玩法:3D娱乐城一字定位")

        except:
            self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
            self.s(text='娱乐城玩法').click()
        self.s(text='个定位').click()

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(text='单').click()
        self.s(text='合数').click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城一字定位-个', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城一字定位-个')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城一字定位-个',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城一字定位-个')


    def gametown_3d_duplex_1(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='一字组合').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城一字组合', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城一字组合')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城一字组合', case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城一字组合')


    def gametown_3d_positon_2(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二字定位').click()
        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='97x').click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-二字定位', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-二字定位')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-二字定位',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-二字定位')


    def gametown_3d_duplex_2(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二字组合').click()
        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='97').click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-二字组合', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-二字组合')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-二字组合',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-二字组合')


    def gametown_3d_sum_2(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二字和数').click()
        self.s().swipe('up', steps=10)
        self.s(text='17').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=22).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-二字和数-百十和数', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-二字和数-百十和数')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-二字和数-百十和数',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-二字和数-百十和数')


        # 百个和数
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二字和数').click()
        self.s(text='百个和数').click()
        self.s().swipe('up', steps=10)
        self.s(text='17').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=22).click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-二字和数-百个和数', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-二字和数-百个和数')
        self.s().must_wait = 2
        caipiao_text = self.s(text="彩票").get_text()
        assert_presence(self, expect='彩票', actual=caipiao_text, case='返回上级页面', scenes='玩法:3D娱乐城-二字和数-百个和数')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-二字和数-百个和数',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-二字和数-百个和数')

        # 十个和数
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='二字和数').click()
        self.s(text='十个和数').click()
        self.s().swipe('up', steps=10)
        self.s(text='17').click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=22).click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-二字和数-十个和数', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-二字和数-十个和数')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-二字和数-十个和数',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-二字和数-十个和数')


    def gametown_3d_position_3(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='三字定位').click()
        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='097').click()
        self.s(text='098').click()
        self.s(text='099').click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-三字定位', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-三字定位')
        self.s().must_wait = 2
        caipiao_text = self.s(text="彩票").get_text()
        assert_presence(self, expect='彩票', actual=caipiao_text, case='返回上级页面', scenes='玩法:3D娱乐城-三字定位')

        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-三字定位',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-三字定位')


    def gametown_3d_deplex_3(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='三字组合').click()
        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='097').click()
        self.s(text='098').click()
        self.s(text='099').click()
        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-三字组合', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-三字组合')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-三字组合',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-三字组合')


    def gametown_3d_sum_3(self):
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
        self.s(text='三字和数').click()
        self.s().swipe('up', steps=10)
        self.s.swipe(fx=448, fy=1300, tx=448, ty=100)
        self.s(text='26').click()
        self.s(text='23').click()

        # 一键投注
        bets = oneclick_bet(self)
        # 断言：一键投注动作
        assert_equal_bet(self, scenes='玩法:3D娱乐城-三字和数', case='一键投注')
        # 返回上级
        game_back_to_check_balance(self, '3D娱乐城-三字和数')
        # 断言：一键投注验证金额
        get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod='玩法:3D娱乐城-三字和数',
                                case='一键投注验证金额')
        # 返回页面
        balance_back_to_game(self, gamename='3D彩', style='福彩3D', menthod='3D娱乐城-三字和数')


    # if __name__ == '__main__':
    #     ltg = login_to_game3d()
    #     '''
    #     3star
    #     '''
    #     ltg.game_3d_basic()
    #     ltg.game_3d_3star_direct_selection_single()
    # ltg.game_3d_3star_direct_selection_sum()
    # ltg.game_3d_3star_group_selection_3snigle()
    # ltg.game_3d_3star_group_selection_3duplex()
    # ltg.game_3d_3star_group_selection_6snigle()
    # ltg.game_3d_3star_group_selection_6duplex()
    # ltg.game_3d_3star_group_selection_mix_duplex()
    # ltg.game_3d_3star_group_selection_sum_duplex()

    '''
    2star
    '''
    # ltg.game_3d_2star_top2_direct_duplex()
    # ltg.game_3d_2star_top2_direct_single()
    # ltg.game_3d_2star_last2_direct_duplex()
    # ltg.game_3d_2star_last2_direct_single()
    # ltg.game_3d_2star_top2_group_single()
    # ltg.game_3d_2star_top2_group_duplex()
    # ltg.game_3d_2star_last2_group_single()
    # ltg.game_3d_2star_last2_group_duplex()
    '''
    定位胆
    
    '''
    # ltg.position()
    """
    不定位
    """
    # ltg.random_postion_1()
    # ltg.random_postion_2()
    """
    大小单双
    """
    # ltg.dxds_top2()
    # ltg.dxds_last2()
