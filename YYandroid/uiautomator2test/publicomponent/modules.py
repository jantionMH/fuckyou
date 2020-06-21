from uiautomator2test.publicomponent.assertion import assert_equal_bet, add_list_and_assert
from uiautomator2test.publicomponent.bettingwidget import oneclick_bet, add_list_bet
from uiautomator2test.publicomponent.others import game_back_to_check_balance, get_c_balance_and_check, \
    balance_back_to_game, random_add_5
import time,os


def onclick_verify_balance_back_game(self, scenes, case1, gamename1, playmenthod, case2, gamename2, style, menthod):
    # 录制整段视频
    now1 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    filename1 = '%s.mp4' % now1
    self.s.screenrecord('../data/%s' % filename1)

    # time.sleep(0.5)


    # 一键投注
    bets = oneclick_bet(self)


    # 断言：一键投注动作
    assert_equal_bet(self, scenes=scenes, case=case1)

    # 断言：返回上级
    game_back_to_check_balance(self, gamename=gamename1)
    # 结束录制，文件名参数传入断言

    return_stop=self.s.screenrecord.stop()
    if return_stop==True:
        print('T')
    elif return_stop==False:
        print("F")
        os.system('taskkill /F /IM Nox.exe')
        time.sleep(10)
        os.popen(r'C:\Program Files (x86)\Nox\bin\Nox.exe')
        time.sleep(60)
    print('停止视频线程',return_stop)
    # 断言：一键投注验证金额
    get_c_balance_and_check(self, amount=bets[0], beforeamount=bets[1], playmenthod=playmenthod,
                            case=case2,video=filename1)
    # 返回页面
    balance_back_to_game(self, gamename=gamename2, style=style, menthod=menthod)


def add_betlist_verify_balance_back_game(self, style1, scenes, case1, gamename1, playmenthod, case2, gamename2, style2,
                                         menthod, keys=None, keys_2=None):
    # 录制整段视频
    now1 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    filename1 = '%s.mp4' % now1
    self.s.screenrecord('../data/%s' % filename1)



    # 添加注单并断言
    n = add_list_and_assert(self, style=style1)

    # 随机加5注并断言
    random_add_5(self, style=style1, key=keys, n1=n[0], key_2=keys_2, filenamebefore=n[1])


    # 确认下注
    betsadd = add_list_bet(self)

    # 断言：下注成功
    assert_equal_bet(self, scenes=scenes, case=case1)

    # 返回上级
    game_back_to_check_balance(self, gamename=gamename1)
    # 结束录制，文件名参数传入断言
    return_stop = self.s.screenrecord.stop()
    if return_stop == True:
        print('T')
    elif return_stop == False:
        print("F")
        os.system('taskkill /F /IM Nox.exe')
        time.sleep(10)
        os.popen(r'C:\Program Files (x86)\Nox\bin\Nox.exe')
        time.sleep(60)
    print('停止视频线程状态', return_stop)

    # 断言：添加注单验证金额
    get_c_balance_and_check(self, amount=betsadd[0], beforeamount=betsadd[1], playmenthod=playmenthod,
                            case=case2,video=filename1)

    # 返回页面
    balance_back_to_game(self, gamename=gamename2, style=style2, menthod=menthod)
