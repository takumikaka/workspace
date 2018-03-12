# -*- coding: utf-8 -*-

from processers.get_dict import getDict
from processers.save_files import saveFile
import config
import os

class compDict(object):
    def __init__(self):
        self.get_dict = getDict()
        self.save_file = saveFile()

    def run(self):
        # dict1 网页数据
        # dict2 要求数据

        dict1 = self.get_dict.get_dict_html()
        dict2 = self.get_dict.get_dict_json()
        for key in dict2.keys():
            if key not in dict1:
                content = '缺失的数据打点如下:'
                st_json = '要求数据: {0}:{1}'.format(key, dict2[key])
                self.save_file.save_file(content)
                self.save_file.save_file(st_json)

        dict2.pop(key)

        for key in dict2.keys():
            if dict1[key] != dict2[key]:
                content = '差异的数据打点如下:'
                st_json = '要求数据: {0}:{1}'.format(key, dict2[key])
                st_html = '网页数据: {0}:{1}'.format(key, dict1[key])
                self.save_file.save_file(content)
                self.save_file.save_file(st_json)
                self.save_file.save_file(st_html)
            else:
                content = '相同的数据打点如下:'
                st_json = '要求数据: {0}:{1}'.format(key, dict2[key])
                st_html = '网页数据: {0}:{1}'.format(key, dict1[key])
                self.save_file.save_file(content)
                self.save_file.save_file(st_json)
                self.save_file.save_file(st_html)

# 不同数据用不同main运行？
# 存入不同txt查看？
# 做个菜单选择内，可以选择，可以输入
