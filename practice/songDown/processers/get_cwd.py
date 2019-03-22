# -*- coding: utf-8 -*-

import os

############################################################################

class getCwd(object):
    def __init__(self):
        pass

    # 获取工程路径
    def get_cwd(self):
        return os.getcwd()

    # 转为list
    def strTolist(self, str):
        return str.split('/')

    # list去空格及无用文件名
    def delUncode(self, lst):

        for i in lst:
            if '' == i or 'processer' == i:
                lst.remove(i)
        return lst

    def run(self):

        str_pwd = self.get_cwd()
        lst = self.strTolist(str_pwd)
        lst = self.delUncode(lst)
        pwd = '/' + '/'.join(lst) + '/'
        print(pwd)
        return pwd

############################################################################
