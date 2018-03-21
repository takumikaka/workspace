# -*- coding: utf-8 -*-

from processers.get_cwd import getCwd
import time
import os
from subprocess import call

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
        call('adb shell screencap -p /sdcard/screenshoot.png', shell=True)
        os.popen('adb pull /sdcard/screenshoot.png ' + path + '/')
        print('屏幕截取成功')

def main():
    action = screenShoot()
    action.run()

if __name__ == '__main__':
    main()
