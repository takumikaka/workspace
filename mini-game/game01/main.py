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
    
    def run(self):
        list = self._Base_List()
        print(list)
    
##############################################################################

def main():
    action = Action()
    action.run()
    
if __name__=="__main__":
    main()
