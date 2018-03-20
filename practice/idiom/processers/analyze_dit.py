# -*- coding: utf-8 -*-


from processers.get_dit import getDit

class anylizeDit(object):
    def __init__(self):
        self.get_dit = getDit()
        self.get_lst = []

    def run(self):
        dit = self.get_dit.get_dit()
        lst = dit['words_result']
        for i in range(len(lst)):
            self.get_lst.append(lst[i]['words'])
        return self.get_lst
