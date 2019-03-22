# -*- coding: utf-8 -*-

import random

class SetList(object):

    def __init__(self):
        pass

    def Random_PokerList(self, list_one):
        random_pokerlist = list_one
        for i in range(2):
            random.shuffle(random_pokerlist)
        return random_pokerlist
