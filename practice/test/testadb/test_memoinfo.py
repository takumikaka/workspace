# coding:UTF-8 -*-

import time
import threading
from comm_adb_devices import *
from comm_adb_pm_package import *
from comm_adb_dumpsys_meminfo import *

def get_info():
    run()

def tick():
    get_info()
    timer = threading.Timer(5, tick)
    timer.start()
    print("*"*50)

def main():
    get_adb_comm_dev()
    get_package_name()
    tick()

main()
