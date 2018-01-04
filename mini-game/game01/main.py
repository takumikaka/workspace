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

class Action(object):

    def __init__(self):
        pass

    def _Base_List(self):
        list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z',
        ]
        return list

    def _Base_dict(self):
        dict = {"dag": "a person who does not look attractive or who behaves in a way that is not attractive",
                "hello": "used when meeting or greeting someone",
                "boy": "a male child or, more generally, a male of any age",
                "girl": "a female child or young woman, especially one still at school",
                }
        return dict

    def _Get_keylist(self, dict):
        key_list = []
        for key in dict.keys():
            key_list.append(key)
        return key_list

    def run(self):
        list = self._Base_List()
        dict = self._Base_dict()
        key_list = self._Get_keylist(dict)
        random.shuffle(key_list)
        key = key_list[0]
        value = dict[key]
        print(value)


##############################################################################

def main():
    action = Action()
    action.run()

if __name__=="__main__":
    main()
