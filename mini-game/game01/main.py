# -*- coding: utf-8 -*-

import random

############################################################################
def red(text):
	return '\033[91m{0}\033[00m'.format(text)

def green(text):
	return '\033[92m{0}\033[00m'.format(text)

def yellow(text):
	return '\033[93m{0}\033[00m'.format(text)
#############################################################################
'''
1. record life
2. get words and random.words
3. record scores
4. game start and game end
'''

class Action(object):

    def __init__(self):
        pass

    # def Base_list
    def _Base_List(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z',
        ]
        return list

    # def Base_dict
    def _Base_Dict(self):
        dict = {"dag": "a person who does not look attractive or who behaves in a way that is not attractive",
                "hello": "used when meeting or greeting someone",
                "boy": "a male child or, more generally, a male of any age",
                "girl": "a female child or young woman, especially one still at school",
                }
        return dict

    # get key_list
    def _Get_KeyList(self, dict):
        key_list = []
        for key in dict.keys():
            key_list.append(key)
        return key_list

    def _Change_KeytoList(self, key):
        list = []
        for i in key:
            list.append(i)
        return list

    def _Random_BaseList(self, list):
        list = random.sample(list, 5)
        return list

    def _Get_ChoicList(self, list1, list2):
        list = list1 + list2
        n = len(list)
        randomlist = random.sample(list, n)
        return randomlist

    def run(self):
        list = self._Base_List()
        dict = self._Base_Dict()
        key_list = self._Get_KeyList(dict)
        random.shuffle(key_list)
        key = key_list[0]
        changekeytolist = self._Change_KeytoList(key)
        randombaselist = self._Random_BaseList(list)
        choicelist = self._Get_ChoicList(changekeytolist, randombaselist)
        print(choicelist)
        '''
        value = dict[key]
        print(value)
        str = input("Enter the str:")
        if str == key:
            print("successful!")
        else:
            print("error")
        '''


##############################################################################

def main():
    action = Action()
    action.run()

if __name__=="__main__":
    main()
