# coding:UTF-8 -*-

import os

f = os.popen(r"adb devices")
content = f.read()
f.close()

print(content)

s = content.split("\n")
new_content = [x for x in s if x != ""]
print(new_content)

devices = []
for i in new_content:
    dev = i.split("\tdevice")
    if len(dev) >= 2:
        devices.append(dev[0])

if not devices:
    print("手机没连上")
else:
    print("当前手机设备: {0}".format(devices))
