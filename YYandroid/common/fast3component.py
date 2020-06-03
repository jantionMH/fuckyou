from Utility.judge import assert_equal_el
import time

def avaliable_num(driver,upmethodtitle):
    # 断言页面是否可选号
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    try:
       numtext = driver.find_elements_by_id('com.yy.sport:id/tv_ball')[15].text
       # print(type(numtext), '所选元素%s' % numtext)
       assert_equal_el(driver, expect='18', actual=numtext, case="页面选号", scenes='玩法:%s'%upmethodtitle)
    except:
        driver.get_screenshot_as_file('../UItest/report/screenshot/%s.png'%now)

        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + "玩法:%s"%upmethodtitle + ',' + "页面选号" + ',' + '失败' + ',' + now + ',' + '页面有误请检查截图' + '\n')
