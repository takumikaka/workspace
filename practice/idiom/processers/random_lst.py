# -*- coding: utf-8 -*-


import random

class randomLst(object):
    def __init__(self):
        self.lst = ['人', '一', '天', '无', '空', '切', '万', '瞪', '人', '呆', '手', '目']
        self.first_lst = []

    def run(self):
        random.shuffle(self.lst)
        self.first_lst = []
        for i in range(4):
            self.first_lst.append(self.lst[i])
        first_lst = ''.join(self.first_lst)
        return first_lst
