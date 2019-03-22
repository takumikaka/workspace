# -*- coding: utf-8 -*-

from appium import webdriver
import time

class MiniGame(object):

    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.0.0'
        self.desired_caps['deviceName'] = 'FFKDU17817002833'
        #第一次运行需要改为true
        self.desired_caps['unicodeKeyboard'] = False
        self.desired_caps['resetKeyboard'] = False
        self.desired_caps['appPackage'] = 'com.immomo.momo'
        self.desired_caps['appActivity'] = 'com.immomo.momo.android.activity.WelcomeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def start_momo(self):
        #启动权限申请
        self.driver.find_element_by_id('com.immomo.momo:id/iv_confirm').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(0.5)
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

        #点击登录进行账号输入
        time.sleep(5)
        self.driver.find_element_by_id('com.immomo.momo:id/btn_login').click()
        self.driver.find_element_by_id('com.immomo.momo:id/login_et_momoid').send_keys('9999002')
        self.driver.find_element_by_id('com.immomo.momo:id/login_et_pwd').send_keys('9999002@momo')
        self.driver.find_element_by_id('com.immomo.momo:id/btn_ok').click()
        time.sleep(5)

    def start_minigame(self):
        #进入更多页面
        self.driver.find_element_by_id('com.immomo.momo:id/maintab_layout_profile').click()
        time.sleep(5)
        #开始滑动屏幕
        screen = self.get_size()
        self.driver.swipe(int(screen[0]*0.01), int(screen[1]*0.5), int(screen[0]*0.01), int(screen[1]*0.25), 1000)
        time.sleep(5)
        #点击游戏中心
        self.driver.tap([(int(screen[0]*0.24), int(screen[1]*0.7)),], 500)
        time.sleep(5)
        #点击手游
        self.driver.tap([(int(screen[0]*0.54), int(screen[1]*0.95)),], 500)
        time.sleep(5)
        #点击棋牌帮
        self.driver.tap([(int(screen[0]*0.9), int(screen[1]*0.4)),], 500)
        time.sleep(5)
        #滑动屏幕并点击一起玩游戏-qa4,每次启动，请先检查一下这项位置
        self.driver.swipe(int(screen[0]*0.01), int(screen[1]*0.5), int(screen[0]*0.01), int(screen[1]*0.25), 1000)
        time.sleep(5)
        self.driver.tap([(int(screen[0]*0.6), int(screen[1]*0.7)),], 500)

    def enter_minigame(self):
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        self.driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        time.sleep(10)
        screen = self.get_size()
        self.driver.tap([(int(screen[0]*0.09), int(screen[1]*0.06)),], 500)
        time.sleep(5)
        self.driver.tap([(int(screen[0]*0.7), int(screen[1]*0.56)),], 500)

    def enter_yuewangame(self):
        screen = self.get_size()
        time.sleep(5)
        self.driver.tap([(int(screen[0]*0.6), int(screen[1]*0.35)), ], 500)
        time.sleep(5)
        self.driver.tap([(int(screen[0]*0.09), int(screen[1]*0.06)),], 500)
        time.sleep(5)
        self.driver.tap([(int(screen[0]*0.7), int(screen[1]*0.56)),], 500)

def main():
    action = MiniGame()
    x, y = action.get_size()
    print(x, y)
    action.start_momo()
    action.start_minigame()
    action.enter_minigame()
    for i in range(50):
        action.enter_yuewangame()

if __name__ == '__main__':
    main()
