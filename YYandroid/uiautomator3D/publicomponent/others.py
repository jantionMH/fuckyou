import time,random

from uiautomator3D.publicomponent.assertion import assert_equal_bet, assert_presence
from uiautomator3D.publicomponent.bettingwidget import oneclick_bet


def game_back_to_check_balance(self, gamename):
    self.s().must_wait(2)
    self.s(resourceId='com.yy.sport:id/iv_back').click()
    caipiao_text = self.s(text="彩票").get_text()
    assert_presence(self, expect='彩票', actual=caipiao_text, case='返回上级页面', scenes='玩法:%s' % gamename)
    self.s(text='彩票管理').click()


def balance_back_to_game(self, gamename, style,menthod):
    self.s(text='彩票').click()
    self.s(text="%s" % gamename).click()
    self.s().must_wait(timeout=2)
    self.s(text="%s" % style).click()
    print('返回游戏投注页面')
    self.s().must_wait = 2
    game_text = self.s(text="玩法").get_text()
    assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:%s'%(menthod))

def get_c_balance_and_check(self, amount, beforeamount, playmenthod, case):
    self.s().must_wait(2)
    c_balance = self.s(resourceId='com.yy.sport:id/iv_user_balance').get_text()
    c = c_balance.replace(',', '')

    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if float(beforeamount) - float(amount) == float(c):
        print('%s验证成功' % case)
        result = '成功'

        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + '%s' % playmenthod + ',' + case + ',' + result + ',' + '无' + ',' + '无' + '\n')
    else:
        print('%s验证失败' % case)
        filename = '%s.png' % now
        self.s.screenshot('../report/screenshot/%s' % filename)
        with open('../data/result.csv', mode='a') as f:
            f.write(
                now + ',' + '%s' % playmenthod + ',' + case + ',' + "失败" + ',' + filename + ',' + '结账前:%s下注额%s减法得到%s实际结账后:%s' % (
                    beforeamount, amount, float(beforeamount) - float(amount), c) + '\n')


def check_if_in_gametown(self, text, style):
    '''
    text：页面的断言元素，一般可用玩法的默认字段，如：两面
    '''
    try:
        page_text = self.s(text='%s' % text).get_text()
        assert_presence(self, expect='%s' % text, actual=page_text, case='进入娱乐城页面', scenes="玩法:%s" % style)

    except:
        self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
        self.s(text='娱乐城玩法').click()


def check_if_in_offical(self, text, style):
    try:
        page_text = self.s(text='%s' % text).get_text()
        assert_presence(self, expect='%s' % text, actual=page_text, case='进入官方玩法页面', scenes="玩法:%s" % style)
    except:
        self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
        self.s(text='官方玩法').click()


# 选择玩法类型，分三段选择
def choose_betstyle(self, betstyle_1, betstyle_2=None, betstyle_3=None):
    self.s(resourceId='com.yy.sport:id/lin_center_title').click()
    self.s(text='%s' % betstyle_1).click()
    if betstyle_2 ==None:
        pass
    else:
       self.s(text='%s' % betstyle_2).click()
    if betstyle_3== None:
       pass
    else:
        self.s(text='%s' % betstyle_3).click()




def random_add_5(self, style):
    n1 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
    self.s(text='+机选5注').click()
    n2=self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
    assert_presence(self, expect=int(n2), actual=int(n1)+5, scenes='玩法:%s' % style, case='随机添加5注')



def gamtown_11c5_randomchoose(self):
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()

    self.s(resourceId='com.yy.sport:id/tv_ball', instance=11).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
    self.s(scrollable=True).scroll.to(text='三中三')

    self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
    self.s(scrollable=True).scroll.to(text='五中五')
    # 第四框
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    self.s.swipe(fx=40, fy=1000, tx=40, ty=600)
    # 第五
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
    self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
    # 第六
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
    # 第七
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
    self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=10).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=11).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()

def gametown_11c5_TG(self):
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=0).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    # self.s(scrollable=True).scroll.to(text='百十    第三球VS第四球')
    self.s.swipe(fx=40, fy=1000, tx=40, ty=400)
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    self.s.swipe(fx=40, fy=1300, tx=40, ty=400)
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
