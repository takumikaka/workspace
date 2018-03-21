# -*- coding: utf-8 -*-

from processers.get_cwd import getCwd
import time
import os

class screenShoot(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.pwd_part_two = 'pics/'

    def abs_path(self, pwd):
        path = os.path.abspath(pwd)
        return path

    def run(self):
        pwd_part_one = self.get_cwd.run()
        path =self.abs_path(pwd_part_one + self.pwd_part_two)
        os.popen('adb wait-for-device')
        os.popen('adb shell screencap -p /sdcard/screenshoot.png')
        os.popen('adb pull /sdcard/screenshoot.png ' + path + '/')
        time.sleep(2)
        print('屏幕截取成功')

def main():
    action = screenShoot()
    action.run()

if __name__ == '__main__':
    main()
