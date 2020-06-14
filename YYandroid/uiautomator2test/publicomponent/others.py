import time, random

from uiautomator2test.publicomponent.assertion import assert_equal_bet, assert_presence
from uiautomator2test.publicomponent.bettingwidget import oneclick_bet


def game_back_to_check_balance(self, gamename):
    self.s().must_wait(2)

    #点击返回箭头
    self.s(resourceId='com.yy.sport:id/iv_back').click()
    caipiao_text = self.s(text="彩票").get_text()
    self.s(text='彩票管理').click()

    assert_presence(self, expect='彩票', actual=caipiao_text, case='返回上级页面', scenes='玩法:%s' % gamename)



def balance_back_to_game(self, gamename, style, menthod):

    time.sleep(2)
    self.s(text='彩票').click()
    time.sleep(2)
    self.s(text="%s" % gamename).click()

    try:
      self.s().must_wait(timeout=2)
      time.sleep(2)
      self.s(text="%s" % style).click()

      print('返回游戏投注页面')
      self.s().must_wait = 2

    except:
        self.s().must_wait(timeout=2)
        time.sleep(2)
        self.s(text="%s" % style).click()
        # 结束录制，文件名参数传入断言
        time.sleep(2)
        self.s.screenrecord.stop()
        print('返回游戏投注页面')
        self.s().must_wait = 2


    game_text = self.s(text="玩法").get_text()
    assert_presence(self, expect='玩法', actual=game_text, case='返回投注页面', scenes='玩法:%s' % (menthod))


def get_c_balance_and_check(self, amount, beforeamount, playmenthod, case,video):

    c_balance = self.s(resourceId='com.yy.sport:id/iv_user_balance').get_text()
    c = c_balance.replace(',', '')


    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if float(beforeamount) - float(amount) == float(c):
        print(case)
        result = '测试成功'

        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + '%s' % playmenthod + ',' + case + ',' + result + ',' + '无' + ',' + video + '\n')
    else:
        print(case)
        filename = '%s.png' % now
        self.s.screenshot('../UItest/report/screenshot/%s' % filename)
        with open('../data/result.csv', mode='a') as f:
            f.write(
                now + ',' + '%s' % playmenthod + ',' + case + ',' + "失败" + ',' + filename + ',' +video+','+ '结账前:%s下注额%s减法得到%s实际结账后:%s' % (
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
    try:

        self.s.click(x=430, y=770)
        self.s.click(x=430, y=770)
        self.s.click(x=430, y=770)
        self.s.click(x=430, y=770)
    except:
        print('没有阴影')


def check_if_in_offical(self, text, style):
    try:
        page_text = self.s(text='%s' % text).get_text()
        assert_presence(self, expect='%s' % text, actual=page_text, case='进入官方玩法页面', scenes="玩法:%s" % style)
    except:
        self.s(resourceId='com.yy.sport:id/iv_right_menu').click()
        self.s(text='官方玩法').click()
        try:

            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)
        except:
            self.s.click(x=430, y=770)
            self.s.click(x=430, y=770)

            try:
                self.s.click(x=430, y=770)
                self.s.click(x=430, y=770)
            except:
                print('没有阴影')


# 选择玩法类型，分三段选择
def choose_betstyle(self, betstyle_1, betstyle_2=None, instance2=None, betstyle_3=None, instance3=None):
    try:
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()
    except:
        self.s(resourceId='com.yy.sport:id/lin_center_title').click()

    self.s(text=betstyle_1).click()
    print('选择玩法')
    # if betstyle_2 ==None:
    #     pass
    # else:
    #    self.s(text='%s' % betstyle_2).click()
    # if betstyle_3== None:
    #    pass
    # else:
    #     self.s(text='%s' % betstyle_3).click()
    if betstyle_2 == None and instance2 == None:
        pass
    elif instance2 == None:
        self.s(text=betstyle_2).click()
    else:
        self.s(text=betstyle_2, instance=instance2).click()
    if betstyle_3 == None and instance3 == None:
        pass
    elif instance3 == None:
        self.s(text=betstyle_3).click()
    else:
        self.s(text=betstyle_3, instance=instance3).click()


def random_add_5(self, style,n1,filenamebefore,key=None,key_2=None):
    if key==None and key_2==None:
        print('无key')
        n3=self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
        print('点击添加注单后',n3)
        if n3!=n1:
            now0 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            filename = '%s.png' % now0
            self.s.screenshot('../UItest/report/screenshot/%s' % filename)
            with open('../data/result.csv', mode='a') as f:
                f.write(
                    now0 + ',' + '添加注单后' + ',' + '验证注单数量' + ',' + "失败" + ',' + filename+'/'+filenamebefore + ',' + '添加注单前后数量不一致'+'\n')

        self.s(text='+机选5注').click()

        n2 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
        print('添加5注后',n2)
        print('添加前',n1)

        assert_presence(self, expect=int(n2), actual=int(n1) + 5, scenes='玩法:%s' % style, case='随机添加5注')
    elif key=='组合':
        print('组合key')
        n3 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
        if n3 != n1:
            now2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            filename = '%s.png' % now2
            self.s.screenrecord('../data/%s' % filename)
            with open('../data/result.csv', mode='a') as f:
                f.write(
                    now2+ ',' + '添加注单后' + ',' + '验证注单数量' + ',' + "失败" + ',' + filename + '/' + filenamebefore + ',' + '添加注单前后数量不一致' + '\n')


        self.s(text='+机选5注').click()
        n2 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()

        assert_presence(self, expect=int(n2), actual=int(n1)*6, scenes='玩法:%s' % style, case='随机添加5注')

    elif key_2 in ["跨度",'前三直选和值','前三组选和值','中三直选和值','中三组选和值','后三直选和值','后三组选和值'
        ,'后二直选和值','后二组选和值','任选2直选和值','任选2组选和值','任选3直选和值','任选3组选和值','任选4直选和值','组三复式']:
        print('请注意这是特殊玩法玩法')

        n3 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
        print('点击添加注单后', n3)
        if n3 != n1:
            now4 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            filename = '%s.png' % now4
            self.s.screenshot('../data/%s' % filename)
            with open('../data/result.csv', mode='a') as f:
                f.write(
                    now4 + ',' + '添加注单后' + ',' + '验证注单数量' + ',' + "失败" + ',' + filename + '/' + filenamebefore + ',' + '添加注单前后数量不一致' + '\n')

        self.s(text='+机选5注').click()

    # elif key_2=='组三复式':
    #     print('组三复式')
    #     # 录制视频
    #     now5 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    #     videofilename3 = '%s.mp4' % now5
    #     self.s.screenrecord('../data/%s' % videofilename3)
    #     time.sleep(2)
    #     n3 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
    #     # 结束录制，文件名参数传入断言
    #     time.sleep(2)
    #     self.s.screenrecord.stop()
    #     assert_presence(self, expect=n1, actual=n3, case='注单的数量', scenes='玩法:%s' % style,video=videofilename3,video_2=exvideo)
    #
    #     # 录制视频
    #     now6= time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    #     videofilename4 = '%s.mp4' % now6
    #     self.s.screenrecord('../data/%s' % videofilename4)
    #     time.sleep(2)
    #     self.s(text='+机选5注').click()
    #     n2 = self.s(resourceId='com.yy.sport:id/tv_betNum').get_text()
    #     # 结束录制，文件名参数传入断言
    #     time.sleep(2)
    #     self.s.screenrecord.stop()
    #     assert_presence(self, expect=12, actual=int(n2), scenes='玩法:%s' % style, case='随机添加5注',video=videofilename4,video_2=exvideo)



def gamtown_11c5_randomchoose(self):
    self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()

    self.s(resourceId='com.yy.sport:id/tv_ball', instance=11).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
    # self.s(scrollable=True).scroll.to(text='三中三')
    #
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
    # self.s(scrollable=True).scroll.to(text='五中五')
    # # 第四框
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    # self.s.swipe(fx=40, fy=1000, tx=40, ty=600)
    # # 第五
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
    # self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
    # # 第六
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    # self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
    # # 第七
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=4).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=5).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=9).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=1).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=2).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=3).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()
    # self.s.swipe(fx=40, fy=1000, tx=40, ty=500)
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=14).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=15).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=16).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=6).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=10).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=11).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=12).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=13).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=7).click()
    # self.s(resourceId='com.yy.sport:id/tv_ball', instance=8).click()


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


def pk10_luckship_bet_page(self, num1_9=None, num10_18=None, num20_29=None, num30_39_1=None, num30_39_2=None,
                           num9_1=None, num18_10=None, num29_20=None, num39_30_1=None, num39_30_2=None):
    self.s.implicitly_wait = 5
    # 冠军
    if num9_1 == None:

        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num1_9).click()
    else:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num1_9).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num9_1).click()
    # # 亚军
    if num18_10 == None and num10_18 == None:
        pass
    elif num18_10 == None:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num10_18).click()

    else:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num10_18).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num18_10).click()
    # # 季军
    if num29_20 == None and num20_29 == None:
        pass
    elif num29_20 == None:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num20_29).click()
    else:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num20_29).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num29_20).click()
    # # 第四
    if num39_30_1 == None and num30_39_1 == None:
        pass
    elif num39_30_1 == None:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num30_39_1).click()
    else:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num30_39_1).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num39_30_1).click()
    self.s.swipe(fx=20, fy=1300, tx=20, ty=600)
    if num39_30_2 == None and num30_39_2 == None:
        pass
    elif num39_30_2 == None:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num30_39_2).click()
    else:
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num30_39_2).click()
        self.s(resourceId='com.yy.sport:id/tv_ball', instance=num39_30_2).click()

def M6_5_star5_direct_num_page(self,num0_9=None,num10_19=None,num20_29=None,num30_39_1=None,num30_39_2=None):
            self.s(resourceId='com.yy.sport:id/tv_ball', instance=num0_9).click()
            if num10_19==None:
                pass
            else:
                 self.s(resourceId='com.yy.sport:id/tv_ball', instance=num10_19).click()
            if num20_29==None:
               pass
            else:
               self.s(resourceId='com.yy.sport:id/tv_ball', instance=num20_29).click()
            if num30_39_1==None:
                pass

            else:
                self.s(resourceId='com.yy.sport:id/tv_ball', instance=num30_39_1).click()

            if num30_39_2==None:
                pass
            else:
                self.s.swipe(fx=40, fy=1300, tx=40, ty=500)
                self.s.swipe(fx=40, fy=1300, tx=40, ty=500)

                self.s(resourceId='com.yy.sport:id/tv_ball', instance=num30_39_2).click()


def marksix_unitprice(self):
    self.s(resourceId='com.yy.sport:id/et_input_recreation_multiple').click()
    self.s(resourceId='com.yy.sport:id/tv_number', instance=5).click()
    self.s(resourceId='com.yy.sport:id/tv_number', instance=6).click()


def shadow_click(self):
    try:

        self.s.click(x=430, y=770)
        self.s.click(x=430, y=770)
        self.s.click(x=430, y=770)
    except:
        print('没有阴影')
