# coding:UTF-8 -*-

import time
import threading

def run():
    print("this is test....")

def tick():
    run()
    timer = threading.Timer(5, tick)
    timer.start()

def main():
    tick()

main()
