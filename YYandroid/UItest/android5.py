import os, subprocess
from time import sleep
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction



def android5app():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'Appium'
    # <包名 aapt apk路径 |findstr 'package'>
    desired_caps['appPackage'] = 'com.yy.sport'
    # <类名 'launchable'>
    desired_caps['appActivity'] = 'com.yy.launch_module.activity.SplashActivity'
    # <指定设备的编号>
    desired_caps['udid'] = '127.0.0.1:62001'
    #<是否重置>
    desired_caps['no-reset']=False
    # <发送请求给appium服务器，特征是以上caps>
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(10)

    return driver
