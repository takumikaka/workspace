# -*- coding: utf-8 -*-


from processers.read_json import readJson
from processers.random_lst import randomLst

class analyzeData(object):
    def __init__(self):
        self.read_json = readJson()
        self.random_lst = randomLst()

    def key_lst(self):
        key_lst = []
        data = self.read_json.run()
        for i in range(len(data)):
            key_lst.append(data[i]['des'])
        return key_lst

    def run(self):
        key_lst = self.key_lst()
        Flag = True
        while Flag:
            word = self.random_lst.run()
            if word in key_lst:
                print(word)
                Flag = False
