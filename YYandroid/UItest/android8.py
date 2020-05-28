import os, subprocess
from time import sleep
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction




def Android8app():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'Appium'
    # 包名 aapt apk路径 |findstr 'package'
    desired_caps['appPackage'] = 'com.yy.sport'
    # 类名 'launchable'
    desired_caps['appActivity'] = 'com.yy.launch_module.activity.SplashActivity'
    # 指定设备的编号
    desired_caps['udid'] = '192.168.181.102:5555'
    # 发送请求给appium服务器，特征是以上caps
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(10)
    return driver

def allowvisit(self):
        # 允许访问
        self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        sleep(3)