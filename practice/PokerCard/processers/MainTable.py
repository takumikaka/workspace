# -*- coding: utf-8 -*-

from processers.PokerCard import PokerCard
from processers.SetList import SetList

class MainTable(object):

    def __init__(self):
        self.poker_card = PokerCard()
        self.set_list = SetList()

    def random_pokers(self):
        poker_list = self.poker_card.Poker_list()
        random_pokerlist = self.set_list.Random_PokerList(poker_list)
        return random_pokerlist

    def del_list(self, list):
        del list[0]
        return list

    def get_PokersDict(self):
        poker_dict = self.poker_card.Poker_dict()
        return poker_dict

    def run(self):
        random_pokerlist = self.random_pokers()
        print("随机后列表为:{0}".format(random_pokerlist))

        new_pokerlist = self.del_list(random_pokerlist)
        print("删除后列表为:{0}".format(new_pokerlist))

        poker_dict = self.get_PokersDict()
        print("获取字典信息:{0}".format(poker_dict))
