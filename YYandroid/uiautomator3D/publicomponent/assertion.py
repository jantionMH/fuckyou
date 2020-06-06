import time

now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))


def assert_equal_bet(self, case, scenes):
    t = self.s.toast.get_message()

    if t == '投注成功':
        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + '%s' % scenes + ',' + case + ',' + '测试成功' + ',' + '无' + ',' + '无' + '\n')
    else:

        self.s.screenshot('../../report/screenshot/%s.png' % now)
        with open('../data/result.csv', mode='a') as f:
            f.write(
                now + ',' + '%s' % scenes + ',' + case + ',' + "失败" + ',' + '%s.png' % now + ',' + '未收到投注成功提示' + '\n')


def assert_presence(self, expect, actual, case, scenes):
    if expect == actual:

        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + '%s' % scenes + ',' + case + ',' + '测试成功' + ',' + '无' + ',' + '无' + '\n')
    else:
        print('测试失败')
        self.s.screenshot('../UItest/report/screenshot/%s.png' % now)
        with open('../data/result.csv', mode='a') as f:
            f.write(
                now + ',' + '%s' % scenes + ',' + case + ',' + "失败" + ',' + '%s.png' % now + ',' + 'expect:%s,type:%s,actul:%s,type:%s' % (
                expect, type(expect), actual, type(actual)) + '\n')


# 数字页面选号断言
def page_number_avaliable(self, style, num, exnum):
    """
    num:页面元素的下标
    exnum:num所对应的值
    """
    # 页面选号断言
    num_text = self.s(resourceId='com.yy.sport:id/tv_ball', instance=num).get_text()
    assert_presence(self, expect=exnum, actual=num_text, scenes='玩法:%s' % style, case='页面选号')

def page_text_avaliable(self,text,style):
    # 页面断言
    self.s(resourceId='com.yy.sport:id/tv_text').set_text(text)
    page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
    assert_presence(self, expect=text, actual=page_text_2, case='页面输入', scenes='玩法:%s'%style)



# 添加注单并断言

def add_list_and_assert(self,style):
    self.s(text='添加注单').click()
    page_text_1 = self.s(text='投注单').get_text()
    assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:%s'%style, case='添加注单')