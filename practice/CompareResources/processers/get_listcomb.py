# -*- coding: utf-8 -*-

from processers.read_filename import readFilename
import copy

class getListcomb(object):

    def __init__(self):
        self.read_filename = readFilename()
        self.name_list = self.read_filename.run()
        self.new_list = []

    def combine(self):
        one = [0] * 2
        def next_c(li = 0, ni = 0):
            if ni == 2:
                self.new_list.append(copy.copy(one))
                return
            for lj in range(li, len(self.name_list)):
                one[ni] = self.name_list[lj]
                next_c(lj + 1, ni + 1)
        next_c()
        return self.new_list
