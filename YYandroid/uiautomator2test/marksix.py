import uiautomator2
import time
from uiautomator2test.publicomponent.assertion import assert_presence, page_number_avaliable
from uiautomator2test.publicomponent.modules import onclick_verify_balance_back_game, \
    add_betlist_verify_balance_back_game
from uiautomator2test.publicomponent.others import choose_betstyle, marksix_unitprice


class HongkongMarksix:
    def __init__(self):
        phone = uiautomator2.connect('127.0.0.1:62001')
        phone.reset_uiautomator()
        phone.watcher("ok").when(
            xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").when(xpath="//android.widget.Button[@resource-id='android:id/button1' and @text='OK']").click()
        phone.watcher.start()
        phone.app_start('com.yy.sport', stop=True)
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
        self.s(text="六合彩").click()
        self.s().must_wait = 1
        self.s(text="香港六合彩").click(timeout=2)
        try:
            game_text = self.s(text="玩法").get_text()
            assert_presence(self, expect='玩法', actual=game_text, case='进入"香港六合彩"', scenes='进入游戏')
        except:
            print('第一次点击失败了')
            self.s(text="香港六合彩").click(timeout=2)
            game_text = self.s(text="玩法").get_text()
            assert_presence(self, expect='玩法', actual=game_text, case='进入"香港六合彩"', scenes='进入游戏')

    def specialnum(self):
        self.s(text='01').click()
        self.s(text='08').click()
        self.s(text='15').click()
        self.s(text='25').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=400)
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s(text='特大').click()
        self.s(text='特合小').click()
        self.s(text='特后肖').click()
        self.s.service('uiautomator').stop()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-特码', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-特码',
                                         playmenthod='玩法:六合彩-香港六合彩-特码', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-特码')

    def twosides(self):
        choose_betstyle(self, betstyle_1='两面')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-两面', num=0, exnum='特大')  # 页面选号断言
        self.s(text='特合小').click()
        self.s(text='特尾小').click()
        self.s(text='特家肖').click()
        self.s(text='特野肖').click()
        self.s(text='特总双').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-特码', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-特码',
                                         playmenthod='玩法:六合彩-香港六合彩-特码', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-特码')

    def colorwave(self):
        choose_betstyle(self, betstyle_1='色波')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-色波', num=0, exnum='01')  # 页面选号断言
        self.s(text='01').click()
        self.s(text='05').click()
        self.s(text='03').click()
        self.s.service('uiautomator').stop()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-色波', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-色波',
                                         playmenthod='玩法:六合彩-香港六合彩-色波', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-色波')

        choose_betstyle(self, betstyle_1='色波')  # 选择玩法
        self.s(text='半波').click()
        self.s(text='红小').click()
        self.s(text='蓝大').click()
        self.s(text='绿大').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-色波-半波', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-色波-半波',
                                         playmenthod='玩法:六合彩-香港六合彩-色波-半波', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-色波-半波')

        choose_betstyle(self, betstyle_1='色波')  # 选择玩法
        self.s(text='半半波').click()
        self.s(text='红小单').click()
        self.s(text='蓝大双').click()
        self.s(text='绿大双').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-色波-半半波', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-色波-半半波',
                                         playmenthod='玩法:六合彩-香港六合彩-色波-半半波', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-色波-半半波')

    def special_animal(self):
        choose_betstyle(self, betstyle_1='特肖')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-特肖', num=0, exnum='01')  # 页面选号断言
        self.s(text='牛').click()
        self.s(text='羊').click()
        self.s(text='虎').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-特肖', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-特肖',
                                         playmenthod='玩法:六合彩-香港六合彩-特肖', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-特肖')

    def head_tail_num(self):
        choose_betstyle(self, betstyle_1='头尾数')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-头尾数', num=0, exnum='0头')  # 页面选号断言
        self.s(text='3头').click()
        self.s(text='7尾').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-头尾数', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-头尾数',
                                         playmenthod='玩法:六合彩-香港六合彩-头尾数', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-头尾数')

    def hexiao(self):
        choose_betstyle(self, betstyle_1='合肖')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-合肖', num=0, exnum='01')  # 页面选号断言
        self.s(text='牛').click()
        self.s(text='羊').click()
        self.s(text='虎').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-合肖', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-合肖',
                                         playmenthod='玩法:六合彩-香港六合彩-合肖', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-合肖')

    def zheng_code(self):
        choose_betstyle(self, betstyle_1='正码')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-正码', num=0, exnum='01')  # 页面选号断言
        self.s(text='01').click()
        self.s(text='07').click()
        self.s(text='12').click()
        self.s(text='18').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=800)
        self.s(text='34').click()
        self.s(text='35').click()
        self.s(text='38').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=800)
        self.s(text='总小').click()
        self.s(text='总单').click()
        self.s(text='总双').click()
        marksix_unitprice(self)
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-正码', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-正码',
                                         playmenthod='玩法:六合彩-香港六合彩-正码', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-正码')

    def zheng_code_te(self):
        listname = [{'正一特': '一'}, {'正二特': '二'}, {'正三特': '三'}, {'正四特': '四'}, {'正五特': '五'}, {'正六特': '六'}]

        for i in listname:
            choose_betstyle(self, betstyle_1='正码特')  # 选择玩法
            page_number_avaliable(self, style='六合彩-香港六合彩-正码', num=0, exnum='01')  # 页面选号断言
            self.s(text=list(i.keys())[0]).click()
            self.s(text='01').click()
            self.s(text='07').click()
            self.s(text='12').click()
            self.s(text='18').click()
            self.s.swipe(fx=40, fy=1300, tx=40, ty=800)
            self.s(text='30').click()
            self.s(text='40').click()
            self.s(text='45').click()
            self.s(text='41').click()
            self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
            self.s(text='正%s大' % list(i.values())[0]).click()
            self.s(text='正%s红' % list(i.values())[0]).click()
            self.s(text='正%s绿' % list(i.values())[0]).click()
            marksix_unitprice(self)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-正码-%s' % list(i.keys())[0], case1='一键投注',
                                             gamename1='六合彩-香港六合彩-正码-%s' % list(i.keys())[0],
                                             playmenthod='玩法:六合彩-香港六合彩-正码-%s' % list(i.keys())[0], case2='一键投注金额验证',
                                             gamename2='六合彩', style='香港六合彩',
                                             menthod='六合彩-香港六合彩-正码-%s' % list(i.keys())[0])

    def zheng_code_1_6(self):
        listname = ['正码一', '正码二', '正码三', '正码四', '正码五', '正码六']
        for i in listname:
            choose_betstyle(self, betstyle_1='正码1~6')  # 选择玩法
            page_number_avaliable(self, style='六合彩-香港六合彩-正码1~6', num=0, exnum='大码')  # 页面选号断言
            self.s(text=i).click()
            self.s(text='大码').click()
            self.s(text='小码').click()
            self.s(text='单码').click()
            self.s(text='尾小').click()
            self.s(text='绿波').click()
            marksix_unitprice(self)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-正码1-6', case1='一键投注',
                                             gamename1='六合彩-香港六合彩-正码1-6',
                                             playmenthod='玩法:六合彩-香港六合彩-正码1-6', case2='一键投注金额验证',
                                             gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-正码1-6')

    def continuou_animal(self):
        listname = ['二连肖', '三连肖', '四连肖', '五连肖']
        for i in listname:
            choose_betstyle(self, betstyle_1='连肖')  # 选择玩法
            page_number_avaliable(self, style='六合彩-香港六合彩-连肖', num=0, exnum='01')  # 页面选号断言
            self.s(text=i).click()
            self.s(text='鼠').click()
            self.s(text='虎').click()
            self.s(text='牛').click()
            self.s(text='蛇').click()
            self.s(text='狗').click()
            marksix_unitprice(self)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-连肖', case1='一键投注',
                                             gamename1='六合彩-香港六合彩-连肖',
                                             playmenthod='玩法:六合彩-香港六合彩-连肖', case2='一键投注金额验证',
                                             gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-连肖')
    def ptxw(self):
        listname = [{'平特一肖':['鼠','虎','牛','蛇','狗']}, {'平特尾数':['0尾','2尾','5尾','7尾','9尾']}]
        for i in listname:
            choose_betstyle(self, betstyle_1='平特肖尾')  # 选择玩法
            page_number_avaliable(self, style='六合彩-香港六合彩-平特肖尾', num=0, exnum='01')  # 页面选号断言
            for j in list(i.values())[0]:
                self.s(text=list(i.keys())[0]).click()
                self.s(text=j).click()
            marksix_unitprice(self)
            # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
            onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-平特肖尾', case1='一键投注',
                                             gamename1='六合彩-香港六合彩-平特肖尾',
                                             playmenthod='玩法:六合彩-香港六合彩-平特肖尾', case2='一键投注金额验证',
                                             gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-平特肖尾')
    def choose_miss(self):
        choose_betstyle(self, betstyle_1='自选不中')  # 选择玩法
        page_number_avaliable(self, style='六合彩-香港六合彩-自选不中', num=0, exnum='01')  # 页面选号断言
        self.s(text='01').click()
        self.s(text='13').click()
        self.s(text='25').click()
        self.s(text='21').click()
        self.s.swipe(fx=40, fy=1300, tx=40, ty=300)
        self.s(text='26').click()
        self.s(text='38').click()
        self.s(text='49').click()
        # 一键投注+返回上级+一键投注验证金额+返回页面+4个断言断言
        onclick_verify_balance_back_game(self, scenes='玩法:六合彩-香港六合彩-自选不中', case1='一键投注',
                                         gamename1='六合彩-香港六合彩-自选不中',
                                         playmenthod='玩法:六合彩-香港六合彩-自选不中', case2='一键投注金额验证',
                                         gamename2='六合彩', style='香港六合彩', menthod='六合彩-香港六合彩-自选不中')


        self.s.service('uiautomator').stop()

if __name__ == '__main__':
    HK = HongkongMarksix()
    HK.specialnum()
    HK.twosides()
    HK.colorwave()
    HK.special_animal()

    HK.head_tail_num()
    HK.hexiao()
    HK.zheng_code()
    HK.zheng_code_te()
    HK.zheng_code_1_6()
    HK.continuou_animal()
    HK.ptxw()
    HK.choose_miss()