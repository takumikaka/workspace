# -*- coding: utf-8 -*-

import sys
from processers.get_cwd import getCwd
from processers.cross_lst import crossLst

class saveFile(object):
    def __init__(self):
        self.get_cwd = getCwd()
        self.cross_lst = crossLst()

    def save_file(self, data, num):
        file_name = self.get_cwd.run() + 'resource/files/autocheck_' + str(num) + '.txt'
        f = open(file_name,'a')
        f.write(data + '\n')
        f.close()

    def run(self):
        data_one, data_two, data_three, data_four, data_five = self.cross_lst.run()
        self.save_file(data_one, 1)
        self.save_file(data_two, 2)
        self.save_file(data_three, 3)
        self.save_file(data_four, 4)
        self.save_file(data_five, 5)
