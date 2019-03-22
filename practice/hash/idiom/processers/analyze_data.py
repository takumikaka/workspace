# -*- coding: utf-8 -*-


from processers.read_json import readJson
from processers.random_lst import randomLst
from processers.get_cwd import getCwd
import os

class analyzeData(object):
    def __init__(self):
        self.read_json = readJson()
        self.random_lst = randomLst()
        self.get_cwd = getCwd()
        self.pwd_part_one = self.get_cwd.run()
        self.pwd_part_two_pic1 = 'pics/screenshoot.png'
        self.pwd_part_two_pic2 = 'pics/crop_screenshoot.png'

    def key_lst(self):
        key_lst = []
        data = self.read_json.run()
        for i in range(len(data)):
            key_lst.append(data[i]['des'])
        return key_lst

    def del_pics(self):
        path_pic1 = self.pwd_part_one + self.pwd_part_two_pic1
        path_pic2 = self.pwd_part_one + self.pwd_part_two_pic2
        os.remove(path_pic1)
        os.remove(path_pic2)

    def run(self):
        self.del_pics()
        key_lst = self.key_lst()
        Flag = True
        while Flag:
            word = self.random_lst.run()
            if word in key_lst:
                print(word)
                Flag = False
