# coding:UTF-8 -*-

import os

def send_command_msg():
    f = os.popen(r"adb shell pm list package")
    cont_result = f.read()
    f.close()
    return cont_result

def split_content(str):
    new_str = str.split("\n")
    return new_str

def get_pack_info(new_str, str):
    new_list = [x for x in new_str if str in x]
    return new_list

def get_info_name(new_list):
    for package_name in new_list:
        package_name = package_name.split("package:")
    return package_name[1]

def get_package_name():
    cont_result = send_command_msg()
    new_str = split_content(cont_result)
    str = ""
    new_list = get_pack_info(new_str, str)
    package_name = get_info_name(new_list)
    print("想要查找的包名为: {0}".format(package_name))
