# -*- coding: utf-8 -*-

from processers.check_list import checkList

class compareList(object):

    def __init__(self):
        self.check_list = checkList()
        #two is litgame_room
        self.get_list_two = self.check_list.get_list_two()
        #one is litgame_hall
        self.get_list_one = self.check_list.get_list_one()
        self.list = []

    def run(self):
        for i in self.get_list_two:
            for j in self.get_list_one:
                if i == j:
                    self.list.append(i)
        print(self.list)
