import uiautomator2
import time

from uiautomator3D.publicomponent.assertion import assert_presence, page_number_avaliable, assert_equal_bet
from uiautomator3D.publicomponent.bettingwidget import oneclick_bet
from uiautomator3D.publicomponent.modules import onclick_verify_balance_back_game, add_betlist_verify_balance_back_game
from uiautomator3D.publicomponent.others import check_if_in_offical, choose_betstyle, game_back_to_check_balance, \
    get_c_balance_and_check, balance_back_to_game, pk10_luckship_bet_page, check_if_in_gametown


class Luckship:


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
            try:
              caipiao_text = self.s(text="彩票").get_text()
              assert_presence(self, expect='彩票', actual=caipiao_text, case='进入彩票模块', scenes='进入首页')
            except:
                self.s(resourceId="com.yy.sport:id/home_imageview2", instance=4).click()
            self.s(text="PK10").click()
            self.s().must_wait = 1
            self.s(text="幸运飞艇").click(timeout=2)
            try:
               game_text = self.s(text="玩法").get_text()
               assert_presence(self, expect='玩法', actual=game_text, case='进入PK10-幸运飞艇', scenes='进入游戏')
            except:
                print('第一次点击失败了')
                self.s(text="幸运飞艇").click(timeout=2)
                game_text = self.s(text="玩法").get_text()
                assert_presence(self, expect='玩法', actual=game_text, case='进入PK10-幸运飞艇', scenes='进入游戏')

        def top5_position(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='前五', betstyle_2='定位胆', betstyle_3='定位胆',instance3=1)  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-前五-定位胆-定位胆', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1, num9_1=9, num10_18=10, num18_10=18, num20_29=20, num29_20=29, num30_39_1=30, num39_30_1=39,
                                   num30_39_2=30, num39_30_2=39)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self,scenes='玩法:PK10-幸运飞艇-前五-定位胆-定位胆',case1='一键投注',
                                             gamename1='PK10-幸运飞艇-前五-定位胆-定位胆',
                                             playmenthod='玩法:PK10-幸运飞艇-前五-定位胆-定位胆',case2='一键投注金额验证',
                                             gamename2='PK10',style='幸运飞艇',menthod='PK10-幸运飞艇-前五-定位胆-定位胆')
            choose_betstyle(self, betstyle_1='前五', betstyle_2='定位胆', betstyle_3='定位胆', instance3=1)  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1, num9_1=9, num10_18=10, num18_10=18, num20_29=20, num29_20=29,
                                   num30_39_1=30, num39_30_1=39,
                                   num30_39_2=30, num39_30_2=39)
            #添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-前五-定位胆-定位胆', scenes='玩法:PK10-幸运飞艇-前五-定位胆-定位胆', case1='添加注单下注',
                                                 gamename1='PK10-幸运飞艇-前五-定位胆-定位胆',playmenthod='玩法:PK10-幸运飞艇-前五-定位胆-定位胆', case2='添加注单金额验证',
                                                 gamename2='PK10',style2='幸运飞艇', menthod='PK10-幸运飞艇-前五-定位胆-定位胆')

        def top5_direct_duplex(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='前五', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-前五-直选-直选复式', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15,  num20_29=26, num30_39_1=38, num30_39_2=39)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-前五-直选-直选复式', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-前五-直选-直选复式',
                                             playmenthod='玩法:PK10-幸运飞艇-前五-直选-直选复式', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-前五-直选-直选复式')
            choose_betstyle(self, betstyle_1='前五', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15,  num20_29=26, num30_39_1=38, num30_39_2=39)
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-前五-直选-直选复式', scenes='玩法:PK10-幸运飞艇-前五-直选-直选复式'
                                                 ,case1='添加注单下注', gamename1='PK10-幸运飞艇-前五-直选-直选复式',
                                                 playmenthod='玩法:PK10-幸运飞艇-前五-直选-直选复式', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-前五-直选-直选复式')

        def last5_position(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='后五', betstyle_2='定位胆', betstyle_3='定位胆', instance3=1)  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-后五-定位胆-定位胆', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1, num9_1=9, num10_18=10, num18_10=18, num20_29=20, num29_20=29,
                                   num30_39_1=30, num39_30_1=39,
                                   num30_39_2=30, num39_30_2=39)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-后五-定位胆-定位胆', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-后五-定位胆-定位胆',
                                             playmenthod='玩法:PK10-幸运飞艇-后五-定位胆-定位胆', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-后五-定位胆-定位胆')
            choose_betstyle(self, betstyle_1='后五', betstyle_2='定位胆', betstyle_3='定位胆', instance3=1)  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1, num9_1=9, num10_18=10, num18_10=18, num20_29=20, num29_20=29,
                                   num30_39_1=30, num39_30_1=39,
                                   num30_39_2=30, num39_30_2=39)
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-后五-定位胆-定位胆', scenes='玩法:PK10-幸运飞艇-后五-定位胆-定位胆',
                                                 case1='添加注单下注',
                                                 gamename1='PK10-幸运飞艇-后五-定位胆-定位胆',
                                                 playmenthod='玩法:PK10-幸运飞艇-后五-定位胆-定位胆', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-后五-定位胆-定位胆')

        def top4_direct_duplex(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-前四-直选-直选复式', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15, num20_29=26, num30_39_1=38)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-前四-直选-直选复式', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-前四-直选-直选复式',
                                             playmenthod='玩法:PK10-幸运飞艇-前四-直选-直选复式', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-前四-直选-直选复式')
            choose_betstyle(self, betstyle_1='前四', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15, num20_29=26, num30_39_1=38)
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-前四-直选-直选复式', scenes='玩法:PK10-幸运飞艇-前四-直选-直选复式'
                                                 , case1='添加注单下注', gamename1='PK10-幸运飞艇-前四-直选-直选复式',
                                                 playmenthod='玩法:PK10-幸运飞艇-前四-直选-直选复式', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-前四-直选-直选复式')


        def top3_direct_duplex(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-前三-直选-直选复式', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15, num20_29=26)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-前三-直选-直选复式', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-前三-直选-直选复式',
                                             playmenthod='玩法:PK10-幸运飞艇-前三-直选-直选复式', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-前三-直选-直选复式')
            choose_betstyle(self, betstyle_1='前三', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15, num20_29=26)
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-前三-直选-直选复式', scenes='玩法:PK10-幸运飞艇-前三-直选-直选复式'
                                                 , case1='添加注单下注', gamename1='PK10-幸运飞艇-前三-直选-直选复式',
                                                 playmenthod='玩法:PK10-幸运飞艇-前三-直选-直选复式', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-前三-直选-直选复式')

        def top2_direct_duplex(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-前二-直选-直选复式', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-前二-直选-直选复式', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-前二-直选-直选复式',
                                             playmenthod='玩法:PK10-幸运飞艇-前二-直选-直选复式', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-前二-直选-直选复式')
            choose_betstyle(self, betstyle_1='前二', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1, num10_18=15)
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-前二-直选-直选复式', scenes='玩法:PK10-幸运飞艇-前二-直选-直选复式'
                                                 , case1='添加注单下注', gamename1='PK10-幸运飞艇-前二-直选-直选复式',
                                                 playmenthod='玩法:PK10-幸运飞艇-前二-直选-直选复式', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-前二-直选-直选复式')
        def top1_direct_duplex(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='前一', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-前一-直选-直选复式', num=0, exnum='01')  # 页面选号断言
            pk10_luckship_bet_page(self, num1_9=1)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-前一-直选-直选复式', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-前一-直选-直选复式',
                                             playmenthod='玩法:PK10-幸运飞艇-前一-直选-直选复式', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-前一-直选-直选复式')
            choose_betstyle(self, betstyle_1='前一', betstyle_2='直选', betstyle_3='直选复式')  # 选择玩法
            pk10_luckship_bet_page(self, num1_9=1)
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-前一-直选-直选复式', scenes='玩法:PK10-幸运飞艇-前一-直选-直选复式'
                                                 , case1='添加注单下注', gamename1='PK10-幸运飞艇-前一-直选-直选复式',
                                                 playmenthod='玩法:PK10-幸运飞艇-前一-直选-直选复式', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-前一-直选-直选复式')
        def dxds(self):
            check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
            choose_betstyle(self, betstyle_1='大小单双', betstyle_2='大小单双',instance2=1, betstyle_3='大小单双',instance3=2)  # 选择玩法
            page_number_avaliable(self, style='PK10-幸运飞艇-大小单双-大小单双-大小单双', num=0, exnum='大')  # 页面选号断言
            self.s(text='大',instance=0).click()
            self.s(text='单',instance=1).click()
            self.s(text='小',instance=2).click()
            self.s(text='大',instance=3).click()
            self.s(text='双',instance=4).click()
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-大小单双-大小单双-大小单双', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-大小单双-大小单双-大小单双',
                                             playmenthod='玩法:PK10-幸运飞艇-大小单双-大小单双-大小单双', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-大小单双-大小单双-大小单双')

            choose_betstyle(self, betstyle_1='大小单双', betstyle_2='大小单双',instance2=1, betstyle_3='大小单双',instance3=2)
            page_number_avaliable(self, style='PK10-幸运飞艇-大小单双-大小单双-大小单双', num=0, exnum='大')  # 页面选号断言
            self.s(text='大', instance=0).click()
            self.s(text='单', instance=1).click()
            self.s(text='小', instance=2).click()
            self.s(text='大', instance=3).click()
            self.s(text='双', instance=4).click()
            # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
            add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-大小单双-大小单双-大小单双', scenes='玩法:PK10-幸运飞艇-大小单双-大小单双-大小单双'
                                                 , case1='添加注单下注', gamename1='PK10-幸运飞艇-大小单双-大小单双-大小单双',
                                                 playmenthod='玩法:PK10-幸运飞艇-大小单双-大小单双-大小单双', case2='添加注单金额验证',
                                                 gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-大小单双-大小单双-大小单双')
        def TG_all(self):
            import random

            list_game=['冠军','亚军','季军','第四名','第五名']
            for i in list_game:
                list = ['龙,0', '虎,0']
                check_if_in_offical(self, text='前五-定位胆-定位胆', style='幸运飞艇')  # 检查当前页面是否为官方玩法页面
                choose_betstyle(self, betstyle_1='龙虎', betstyle_2='龙虎', betstyle_3=i)  # 选择玩法
                page_number_avaliable(self, style='PK10-幸运飞艇-龙虎-龙虎-%s'%i, num=0, exnum='龙')  # 页面选号断言
                self.s(text=random.choice(list).split(',')[0], instance=random.choice(list).split(',')[1]).click()
                # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
                onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-龙虎-龙虎-%s'%i, case1='一键投注',
                                                 gamename1='PK10-幸运飞艇-龙虎-龙虎-%s'%i,
                                                 playmenthod='玩法:PK10-幸运飞艇-龙虎-龙虎-%s'%i, case2='一键投注金额验证',
                                                 gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-龙虎-龙虎-%s'%i)
                choose_betstyle(self, betstyle_1='龙虎', betstyle_2='龙虎', betstyle_3=i)  # 选择玩法
                self.s(text=random.choice(list).split(',')[0], instance=random.choice(list).split(',')[1]).click()
                # 添加注单+随机5注+确认下注+返回上级+验证金额+返回游戏+6个断言
                add_betlist_verify_balance_back_game(self, style1='PK10-幸运飞艇-龙虎-龙虎-%s'%i, scenes='玩法:PK10-幸运飞艇-龙虎-龙虎-%s'%i
                                                     , case1='添加注单下注', gamename1='PK10-幸运飞艇-龙虎-龙虎-%s'%i,
                                                     playmenthod='玩法:PK10-幸运飞艇-龙虎-龙虎-%s'%i, case2='添加注单金额验证',
                                                     gamename2='PK10', style2='幸运飞艇', menthod='PK10-幸运飞艇-龙虎-龙虎-%s'%i)
        def gametown_PK10_two_sides(self):
            check_if_in_gametown(self, text='两面', style='PK10-幸运飞艇')
            choose_betstyle(self, betstyle_1='两面')  # 选择玩法
            self.s(text="大", instance=0).click()
            self.s(text="1V10虎", instance=0).click()
            self.s(text="2V9虎", instance=0).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=600)
            self.s(text='3V8虎',instance=0).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=600)
            self.s(text='4V7虎', instance=0).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=600)
            self.s(text='5V6虎', instance=0).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=600)
            self.s(text='单', instance=1).click()
            self.s(text='小', instance=2).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=300)
            self.s(text='小', instance=1).click()
            self.s(text='双', instance=2).click()
            self.s(text='单', instance=3).click()
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-娱乐城-两面', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-娱乐城-两面',
                                             playmenthod='玩法:PK10-幸运飞艇-娱乐城-两面', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-娱乐城-两面')

        def gametown_PK10_guess_sum(self):
            check_if_in_gametown(self, text='两面', style='PK10-幸运飞艇')
            choose_betstyle(self, betstyle_1='猜和值')  # 选择玩法
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-娱乐城-猜和值-冠亚', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-娱乐城-猜和值-冠亚',
                                             playmenthod='玩法:PK10-幸运飞艇-娱乐城-猜和值-冠亚', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-娱乐城-猜和值-冠亚')
            choose_betstyle(self, betstyle_1='猜和值')  # 选择玩法
            self.s(text='冠亚季和值').click()
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=20).click()
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-娱乐城-猜和值-冠亚季和值', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-娱乐城-猜和值-冠亚季和值',
                                             playmenthod='玩法:PK10-幸运飞艇-娱乐城-猜和值-冠亚季和值', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-娱乐城-猜和值-冠亚季和值')
            choose_betstyle(self, betstyle_1='猜和值')  # 选择玩法
            self.s(text='首尾和值').click()
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-娱乐城-猜和值-首尾和值', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-娱乐城-猜和值-首尾和值',
                                             playmenthod='玩法:PK10-幸运飞艇-娱乐城-猜和值-首尾和值', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-娱乐城-猜和值-首尾和值')

        def gametown_PK10_champion_tenth(self):
            check_if_in_gametown(self, text='两面', style='PK10-幸运飞艇')
            choose_betstyle(self, betstyle_1='第1-10名')  # 选择玩法
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=10).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=10).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=400)
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
            time.sleep(1)
            #第五
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
            self.s.swipe(fx=40, fy=1000, tx=40, ty=900)
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=400)
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=400)
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-娱乐城-猜和值-第1-10名', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-娱乐城-猜和值-第1-10名',
                                             playmenthod='玩法:PK10-幸运飞艇-娱乐城-猜和值-第1-10名', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-娱乐城-猜和值-第1-10名')
        def gametown_luckship_TG(self):
            import random
            choose_betstyle(self, betstyle_1='龙虎斗')  # 选择玩法
            list=['龙','虎']
            for i in range(4):
                self.s(text=random.choice(list), instance=i).click()
            self.s.swipe(fx=40, fy=1000, tx=40, ty=400)
            self.s(text=random.choice(list), instance=3).click()
            onclick_verify_balance_back_game(self, scenes='玩法:PK10-幸运飞艇-娱乐城-猜和值-龙虎斗', case1='一键投注',
                                             gamename1='PK10-幸运飞艇-娱乐城-猜和值-龙虎斗',
                                             playmenthod='玩法:PK10-幸运飞艇-娱乐城-猜和值-龙虎斗', case2='一键投注金额验证',
                                             gamename2='PK10', style='幸运飞艇', menthod='PK10-幸运飞艇-娱乐城-猜和值-龙虎斗')
if __name__ == '__main__':
    L=Luckship()
    L.top5_position()
    L.top5_direct_duplex()
    L.last5_position()
    L.top4_direct_duplex()
    L.top3_direct_duplex()
    L. top2_direct_duplex()
    L.top1_direct_duplex()
    L.dxds()
    L.TG_all()
    L.gametown_PK10_two_sides()
    L.gametown_PK10_guess_sum()
    L.gametown_PK10_champion_tenth()
    L.gametown_luckship_TG()