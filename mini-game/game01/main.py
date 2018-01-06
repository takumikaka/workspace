# -*- coding: utf-8 -*-

import random
import time
from csv2dict import row_csv2dict

############################################################################
def red(text):
	return '\033[91m{0}\033[00m'.format(text)

def green(text):
	return '\033[92m{0}\033[00m'.format(text)

def yellow(text):
	return '\033[93m{0}\033[00m'.format(text)
#############################################################################
'''
1. record life---done
2. get words and random.words---done
3. record scores---done
4. game start and game end---done
5. first game display---done
6. end game content---done
7. read csv---done
'''

class Action(object):

    def __init__(self):
        pass

    def _Clock(self):
        for i in range(1, 4):
            print(4 - i)
            time.sleep(1)

    def _Check_FirstorNot(self, first_flog):
        if first_flog == False:
            time.sleep(1)
            print("Next Stage!")
            self._Clock()
        else:
            time.sleep(1)


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

    def _Unduplition_list(self, l1):
        unduplicatlist = list(set(l1))
        return unduplicatlist

    def _Check_life(self, life, life_flog):
        if life_flog == False:
            life = life - 1
        else:
            pass
        return life

    def _Check_score(self, score, life_flog):
        if life_flog == True:
            score = score + 50
        else:
            pass
        return score

    def _Check_level(self, score):
        if score >= 500:
            print("That's great! You're more than 99%.")
        elif score >= 200 and score < 500:
            print("Come on! You're more than 70%.")
        else:
            print("What a pity! You're more than 20%.")

    def run(self):
        first_flog = True
        print("Are your ready!")
        self._Clock()
        print("Game Start!")
        print("*"*80)
        life = 3
        life_flog = True
        score = 0

        while life > 0:
            print("Your Life is: {0}".format(life))
            print("Your Score is: {0}\n".format(score))
            self._Check_FirstorNot(first_flog)
            list = self._Base_List()
            #dict = self._Base_Dict()
            dict = row_csv2dict("game01.csv")
            key_list = self._Get_KeyList(dict)
            random.shuffle(key_list)
            key = key_list[0]
            changekeytolist = self._Change_KeytoList(key)
            randombaselist = self._Random_BaseList(list)
            choicelist = self._Get_ChoicList(changekeytolist, randombaselist)
            unduplicatlist = self._Unduplition_list(choicelist)
            print("The choice list: {0}".format(unduplicatlist))
            value = dict[key]
            print("The sentence: {0}".format(value))
            str = input("Enter your answer:")
            if str == key:
                print("Your are very clever! The answer is: {0}".format(key))
                print("*"*80)
                time.sleep(1)
                life = self._Check_life(life,life_flog)
                score = self._Check_score(score, life_flog)
                first_flog = False
            else:
                print("What a pity! The answer is: {0}".format(key))
                print("*"*80)
                time.sleep(1)
                life_flog = False
                life = self._Check_life(life, life_flog)
                score = self._Check_score(score, life_flog)
                first_flog = False

        time.sleep(1)
        print("Game over!")
        print("Your score is: {0}".format(score))
        self._Check_level(score)

##############################################################################

def main():
    action = Action()
    action.run()

if __name__=="__main__":
    main()
