# coding:UTF-8 -*-

import os

def send_command_msg():
    f = os.popen(r"adb devices")
    cont_result = f.read()
    f.close()
    return cont_result

def split_content(str):
    new_str = str.split("\n")
    return new_str

def del_blank(str):
    new_list = [x for x in str if x != ""]
    return new_list

def get_device_info(new_list):
    devices = []
    for i in new_list:
        dev = i.split("\tdevice")
        if len(dev) >= 2:
            devices.append(dev[0])
    return devices

def get_adb_comm_dev():
    cont_result = send_command_msg()
    print(cont_result)
    new_str = split_content(cont_result)
    new_list = del_blank(new_str)
    devices = get_device_info(new_list)
    if not devices:
        print("手机未链接!")
    else:
        print("连接的设备为: {0}".format(devices))
