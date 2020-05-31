import random, time


def hhhmenthod(driver):
    for i in range(10):
        r = random.randrange(3, 19)
        time.sleep(0.5)
        driver.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='%d']" % r).click()
    time.sleep(2)


def dxds(driver):
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[0].click()
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[1].click()
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[2].click()
    driver.find_elements_by_id("com.yy.sport:id/tv_ball")[3].click()


def s3g(driver):
    driver.find_element_by_id("com.yy.sport:id/tv_ball").click()


def s3s(driver):
    r = random.choice(["com.yy.sport:id/tv_menu_all", "com.yy.sport:id/tv_menu_da", "com.yy.sport:id/tv_menu_xiao",
                       "com.yy.sport:id/tv_menu_ji", "com.yy.sport:id/tv_menu_ou"])

    driver.find_element_by_id("%s" % r).click()


def d3dt(driver):
    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.view.View[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.view.View["
                                 "1]/android.widget.RelativeLayout[%s]/android.view.View["
                                 "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % 2).click()

    driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout["
                                 "1]/android.view.View[1]/android.widget.RelativeLayout["
                                 "1]/android.widget.LinearLayout[1]/android.view.View["
                                 "1]/android.widget.RelativeLayout[%s]/android.view.View["
                                 "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % 5).click()
    driver.find_element_by_xpath(
        "//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout["
        "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
        "1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout["
        "1]/android.widget.LinearLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.widget.LinearLayout["
        "1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout["
        "1]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.RelativeLayout["
        "2]/android.widget.LinearLayout[1]/android.view.View[1]/android.widget.RelativeLayout[%s]/android.view.View["
        "1]/android.widget.LinearLayout[1]/android.widget.TextView[1]" % 3).click()


# 对于12个元素在同一frame下的胆码1拖码2的不重复选择
def d2td(driver):
    total = driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    print(len(total))
    r = random.choice([0, 2, 4])
    total[r].click()
    for i in range(2):
        r1 = random.choice([7, 9, 11])
        total[r1].click()
        time.sleep(1)

def gametownchossenum(driver):
    listofelpage=driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    print(len(listofelpage))
    listr=[]
    for i in range(len(listofelpage)-10):
       listc=['大','小','单','双',3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
       r=random.choice(listc)
       driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.yy.sport:id/tv_ball' and @text='%s']"%r).click()
       listr.append(r)
    return listr
def gametownchooseserial1(driver):
    #页面元素总数
    listofelpage = driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    print(len(listofelpage))
    for i in range(len(listofelpage) - 10):
        r=random.randrange(18)
        listofelpage[r].click()

def gametownchooseserial2(driver):
    #页面元素总数
    listofelpage = driver.find_elements_by_id("com.yy.sport:id/tv_ball")
    print(len(listofelpage))
    for i in range(len(listofelpage)):
        r=random.randrange(len(listofelpage))
        listofelpage[r].click()