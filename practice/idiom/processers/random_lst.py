# -*- coding: utf-8 -*-


import random
from processers.analyze_lst import analyzeLst

class randomLst(object):
    def __init__(self):
        self.analyze_lst = analyzeLst()
        self.lst = self.analyze_lst.run()
        self.first_lst = []

    def run(self):
        random.shuffle(self.lst)
        self.first_lst = []
        for i in range(4):
            self.first_lst.append(self.lst[i])
        first_lst = ''.join(self.first_lst)
        return first_lst
