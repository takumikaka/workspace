# coding:UTF-8 -*-

import os

def send_command_msg():
    f = os.popen(r"adb shell dumpsys meminfo xxx.xxx.xxx")
    cont_result = f.read()
    f.close()
    return cont_result

def write_str_tofile(str):
    with open("meminfo.txt", "a+") as f:
        f.write(str)
        f.close()

def check_file_cont():
    with open("meminfo.txt", "rb+") as f:
        if f.read() is None:
            f.close()
        else:
            f.seek(0)
            f.truncate()
            f.close()


def run():
    cont_result = send_command_msg()
    #check_file_cont()
    print("开始写入文件...")
    write_str_tofile(cont_result)
    print("文件写入完毕...")
