# -*- coding: utf-8 -*-

from processers.get_dict import getDict
from processers.save_files import saveFile
import config
import os

class compDict(object):
    def __init__(self):
        self.get_dict = getDict()
        self.save_file = saveFile()
        self.miss_lst = []
        self.diff_lst = []
        self.same_lst = []
        self.content_miss = config.CONTENT_MISS
        self.content_diff = config.CONTENT_DIFF
        self.content_same = config.CONTENT_SAME

    def run(self):
        # dict1 网页数据
        # dict2 要求数据

        dict1 = self.get_dict.get_dict_html()
        dict2 = self.get_dict.get_dict_json()
        for key in dict2.keys():
            if key not in dict1:
                st_json = '要求数据: {0}:{1}'.format(key, dict2[key])
                self.miss_lst.append(st_json)
                #self.save_file.save_file(st_json)

        dict2.pop(key)

        for key in dict2.keys():
            if dict1[key] != dict2[key]:
                st_json = '要求数据: {0}:{1}'.format(key, dict2[key])
                st_html = '网页数据: {0}:{1}'.format(key, dict1[key])
                self.diff_lst.append(st_json)
                self.diff_lst.append(st_html)
                #self.save_file.save_file(content)
                #self.save_file.save_file(st_json)
                #self.save_file.save_file(st_html)
            else:
                st_json = '要求数据: {0}:{1}'.format(key, dict2[key])
                st_html = '网页数据: {0}:{1}'.format(key, dict1[key])
                self.same_lst.append(st_json)
                self.same_lst.append(st_html)
                #self.save_file.save_file(content)
                #self.save_file.save_file(st_json)
                #self.save_file.save_file(st_html)

        self.save_file.save_file(self.content_miss)
        self.save_file.save_file(str(self.miss_lst))
        self.save_file.save_file(self.content_diff)
        self.save_file.save_file(str(self.diff_lst))
        self.save_file.save_file(self.content_same)
        self.save_file.save_file(str(self.same_lst))

# 不同数据用不同main运行？
# 存入不同txt查看？
# 做个菜单选择内，可以选择，可以输入
