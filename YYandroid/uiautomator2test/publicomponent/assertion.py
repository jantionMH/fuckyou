import time


def assert_equal_bet(self, case, scenes,video):
    t = self.s.toast.get_message()
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if t == '投注成功':
        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + '%s' % scenes + ',' + case + ',' + '测试成功' + ',' + '无' + ',' + '无' + '\n')
    else:
        filename = '%s.png' % now
        self.s.screenshot('../UItest/report/screenshot/%s' % filename)
        with open('../data/result.csv', mode='a') as f:
            f.write(
                now + ',' + '%s' % scenes + ',' + case + ',' + "失败" + ',' + filename + ','+video+'未收到投注成功提示' + '\n')


def assert_presence(self, expect, actual, case, scenes, video=None,video_2=None, key=None):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if expect == actual:
        print('测试成功,预期=实际')
        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + '%s' % scenes + ',' + case + ',' + '测试成功' + ',' + '无' + ',' + '无' + '\n')
    elif expect != actual:
        print('测试失败')
        filename = '%s.png' % now
        self.s.screenshot('../UItest/report/screenshot/%s' % filename)
        with open('../data/result.csv', mode='a') as f:
            f.write(
                now + ',' + '%s' % scenes + ',' + case + ',' + "失败" + ',' + filename+ ',' + video+'/'+video_2 + '\n')


# 数字页面选号断言
def page_number_avaliable(self, style, num, exnum):
    """
    num:页面元素的下标
    exnum:num所对应的值
    """
    # 页面选号断言
    num_text = self.s(resourceId='com.yy.sport:id/tv_ball', instance=num).get_text()
    assert_presence(self, expect=exnum, actual=num_text, scenes='玩法:%s' % style, case='页面选号')


def page_text_avaliable(self, text, style):
    # 页面断言
    self.s(resourceId='com.yy.sport:id/tv_text').set_text(text)
    page_text_2 = self.s(resourceId='com.yy.sport:id/tv_text').get_text()
    assert_presence(self, expect=text, actual=page_text_2, case='页面输入', scenes='玩法:%s' % style)


# 添加注单并断言

def add_list_and_assert(self, style):
    self.s.wait_timeout = 5
    # 录制视频
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    videofilename = '%s.mp4' % now
    self.s.screenrecord('../data/%s' % videofilename)
    #截图
    now0 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    filename = '%s.png' % now0
    self.s.screenshot('../UItest/report/screenshot/%s' % filename)
    n1 = self.s(text='已选').sibling(className='android.widget.TextView', instance=1).get_text()
    print('添加前的注单数', n1)
    time.sleep(1)
    self.s(text='添加注单').click()
    page_text_1 = self.s(text='投注单').get_text()
    # 结束录制，文件名参数传入断言
    time.sleep(3)
    self.s.screenrecord.stop()
    assert_presence(self, expect='投注单', actual=page_text_1, scenes='玩法:%s' % style, case='添加注单', video=videofilename)
    return n1, filename,videofilename
