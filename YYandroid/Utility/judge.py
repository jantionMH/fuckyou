from appium import webdriver
import time


def assert_not_null(actual, case, scenes):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if len(actual) != 0:

        filename = '%s.png' % now
        # driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + scenes + ',' + case + ',' + '失败' + ',' + filename + ',' + "期望:失败列表为空,实际:%s,type%s" % (
                    actual, type(actual)) + '\n')
        print('失败' + ',' + scenes + ',' + case)
    elif len(actual) == 0:

        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + scenes + ',' + case + ',' + '成功' + ',' + '无' + ',' + '无' + '\n')

def assert_equal_el(driver, expect, actual, case, scenes):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if expect == actual:
        result = '成功'


        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + scenes + ',' + case + ',' + result + ',' + '无' + ',' + '无' + '\n')
    else:
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(
                now + ',' + scenes + ',' + case + ',' + result + ',' + filename + ',' + "期望:%s,type%s,实际:%s,type%s" % (
                    expect, type(expect), actual, type(actual)) + '\n')


def asser_equal_nu(driver, current, bet_number, after_bet, case, scenes):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if current - bet_number == after_bet:
        with open('../data/result.csv', mode='a+')as f:
            f.write(now + ',' + scenes + ',' + case + ',' + "成功" +',' +'无' + ',' + '无' + '\n')
    else:
        cucal = current - bet_number
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode='a+')as f:
            f.write(
                now + ',' + scenes + ',' + case + ',' + "失败" + ',' + filename + ',' + '结账前:%s下注额%s减法得到%s实际结账后:%s' % (
                current, bet_number, cucal, after_bet) + '\n')


def assert_more_than(driver, expect, actual, scenes, case):
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    if actual > expect:
        result = '成功'
        with open('../data/result.csv', mode='a+') as f:
            f.write(now + ',' + scenes + ',' + case + ',' + result + ',' + '无' + ','+'无' + '\n')
    else:
        result = '失败'
        filename = '%s.png' % now
        driver.get_screenshot_as_file("../UItest/report/screenshot/%s" % filename)
        with open('../data/result.csv', mode="a+") as f:
            f.write(now + ',' + scenes + ',' + case + ',' + result + ',' + filename + '\n')


# def capture(filename):
# ImageGrab.grab().save('../data' + filename)

def creat_report():

    content="""
         <table witdth=1000 border=1 cellspacing=0>
                  <tr bgcolor=yellow border=1>
                  <td >BB彩票 Android 自動化測試報告</td>
                  </tr>
                  <tr bgcolor=orange>
                  
                  <td width=20% >测试时间</td>
                  <td width=10% >测试场景</td>
                  <td width=35%>测试用例</td>
                  <td width=10%>测试结果</td>
                  <td witdth=25%>错误截图</td>
                  
                  
                  </tr>
    """

    with open('../data/result.csv', mode='r')as f:
        result = f.readlines()
        print(result)
        for line in result:
            print(line)
            if ',' not in line:

                content+="<tr>"
                content+="<td width=15%%>%s</td\n>"%line
                content += "</tr>"

            if ',' in line:
                content += "<tr>"

                content += "<td width=15%%>%s</td\n>" % line.strip().split(',')[0]
                content += "<td width=30%%>%s</td\n>" % line.strip().split(',')[1]
                content += "<td width=20%%>%s</td\n>" % line.strip().split(',')[2]
                r = line.strip().split(',')[3]
                if r == '测试成功' or r == '成功':
                    content += "<td bgcolor=green width=10%%>%s</td\n>" % line.strip().split(',')[3]
                else:
                    content += "<td bgcolor=red width=10%%>%s</td\n>" % line.strip().split(',')[3]
                h = line.strip().split(',')[4]
                if h == '无':
                    content += "<td width=10%%>%s</td\n>" % h
                elif '/' in h:
                    content += "<td width=10%%><a href='./%s%s'>%s,%s</td\n>" % (
                    h.split('/')[0], h.split('/')[1], h.split('/')[0], h.split('/')[1])
                else:
                    content += "<td width=10%%><a href='./%s'>%s</td\n>" % (h, h)
                v = line.strip().split(',')[5]
                if v == '无':
                    content += "<td width=15%%>%s</td\n>" % v
                elif '/' in v:
                    content += " <td width=15%%><a href='./%s'>%s<a href='./%s'>%s</td>" % (
                    v.split('/')[0], v.split('/')[0], v.split('/')[1], v.split('/')[1])

                else:
                    content += "<td width=15%%><a href='./%s'>%s</td\n>" % (v, v)
                content += "</tr>"
    content += '</table>'
    print(content)
    with open('../UItest/report/report.html', 'w+')as f:
        f.write(content)


def get_html():
    content = """
       
      <table witdth=1000 border=1 cellspacing=0>
          <tr bgcolor=yellow border=1>
          <td >BB彩票 Android 自動化測試報告</td>
          </tr>
          <tr bgcolor=orange>
          
          <td width=20% >测试时间</td>
          <td width=10% >测试场景</td>
          <td width=35%>测试用例</td>
          <td width=10%>测试结果</td>
          <td witdth=25%>错误截图</td>
          
          
          </tr>
    """

    with open('../data/result.csv', mode='r')as f:
        result = f.readlines()
        print(result)
        for line in result:
            content += "<tr>"

            content += "<td width=20%%>%s</td\n>" % line.strip().split(',')[0]
            content += "<td width=25%%>%s</td\n>" % line.strip().split(',')[1]
            content += "<td width=35%%>%s</td\n>" % line.strip().split(',')[2]

            r = line.strip().split(',')[3]
            if r == '测试成功':
                content += "<td bgcolor=green width=15%%>%s</td\n>" % line.strip().split(',')[3]
            else:
                content += "<td bgcolor=red width=15%%>%s</td\n>" % line.strip().split(',')[3]
            h = line.strip().split(',')[4]
            if h == '无':
                content += "<td width=20%%>%s</td\n>" % h
            else:
                content += "<td width=20%%><a href='../UItest/report/screenshot/%s'>%s</td\n>" % (h, h)

            content += "</tr>"

    content += '</table>'
    print(content)

    with open('../UItest/report/report.html', 'w+')as f:
        f.write(content)


def get_emial_html():
    content = """

      <table witdth=1000 border=1 cellspacing=0>
         
          <tr bgcolor=orange>
          <td width=15% >测试时间</td>
          <td width=30% >测试场景</td>
          <td width=20%>测试用例</td>
          <td width=10%>测试结果</td>
          <td witdth=10%>错误截图</td>
          <td width=15%>错误视频</td>
          </tr>
    """

    with open('../data/result.csv', mode='r')as f:
        result = f.readlines()


        for line in result:
            content += "<tr>"

            content += "<td width=15%%>%s</td\n>" % line.strip().split(',')[0]
            content += "<td width=30%%>%s</td\n>" % line.strip().split(',')[1]
            content += "<td width=20%%>%s</td\n>" % line.strip().split(',')[2]
            r = line.strip().split(',')[3]
            if r == '测试成功' or r=='成功':
                content += "<td bgcolor=green width=10%%>%s</td\n>" % line.strip().split(',')[3]
            else:
                content += "<td bgcolor=red width=10%%>%s</td\n>" % line.strip().split(',')[3]
            h = line.strip().split(',')[4]
            if h == '无':
                content += "<td width=10%%>%s</td\n>" % h
            elif '/' in h:
                content += "<td width=10%%><a href='./%s%s'>%s,%s</td\n>" % (h.split('/')[0],h.split('/')[1], h.split('/')[0],h.split('/')[1])
            else:
                content += "<td width=10%%><a href='./%s'>%s</td\n>" % (h, h)
            v=line.strip().split(',')[5]
            if v=='无':
                content += "<td width=15%%>%s</td\n>" % v
            elif '/'in v:
               content += " <td width=15%%><a href='./%s'>%s<a href='./%s'>%s</td>" %(v.split('/')[0],v.split('/')[0],v.split('/')[1],v.split('/')[1])

            else:
                content += "<td width=15%%><a href='./%s'>%s</td\n>" % (v,v)
            content += "</tr>"

    content += '</table>'
    print(content)

    with open('../UItest/report/demoreport11_5.html', 'w+')as f:
        f.write(content)


def fileex():
    with open('../data/result.csv', mode='r')as f:
        result = f.readlines()
        print(result[0].strip().split(','))
        print(result[0].strip().split(',')[5])


if __name__ == '__main__':
    # creat_report()
    get_emial_html()
    # get_html()
    # fileex()
