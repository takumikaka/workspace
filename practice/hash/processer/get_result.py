# -*- coding: utf-8 -*-


from processer.dHash import class_dHash
from processer.open_xls import openXls

############################################################################

class class_get_result(object):
    def __init__(self):
        self.class_dhash = class_dHash()
        self.open_xls = openXls()

    # 汉明距离大于20，则图片之间差异过大
    def get_result(self, lst, data):
        for i in range(0, len(lst)):
            if lst[i] > 20:
                name = data[i][0] + data[i][1]
                print('第{0}行的机型{1}的设配有问题'.format(i+1, name))
                #print(lst[i])

    def run(self):
        lst = self.class_dhash.run()
        data = self.open_xls.run()
        self.get_result(lst, data)



############################################################################
