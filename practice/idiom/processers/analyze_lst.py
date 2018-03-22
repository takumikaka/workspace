# -*- coding: utf-8 -*-

from processers.analyze_dit import anylizeDit

class analyzeLst(object):
    def __init__(self):
        self.analyze_dit = anylizeDit()
        self.lst = []

    def str_Tolist(self, str):
        for i in str:
            self.lst.append(i)
        return self.lst

    def run(self):
        lst = self.analyze_dit.run()
        string = ''.join(lst)
        lst = self.str_Tolist(string)
        return lst
