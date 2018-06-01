# -*- coding: utf-8 -*-

import time
import random

class listReplace:
    def __init__(self):
        self.list = []

    def inputStr(self):
        input_str = input("Enter str:")
        return input_str

    def appendList(self, str, list):
        list.append(str)
        return list

    def replaceList(self, str, list):
        list[1] = str
        return list

    def printInfo(self, list):
        len_list = len(list)
        num_one = random.randint(3, 10)
        num_two = random.randint(3, 10)
        if len_list >= 2:
            for i in range(num_one):
                print("Downlaod[{0}]: {1}%...".format(list[0], int((i+1)/num_one*100)))
            for i in range(num_two):
                print("Downlaod[{0}]: {1}%...".format(list[1], int((i+1)/num_two*100)))
        else:
            for i in range(num_one):
                print("Downlaod[{0}]: {1}%...".format(list[0], int((i+1)/num_one*100)))

    def run(self):
        choice_one = self.inputStr()
        self.appendList(choice_one, self.list)
        print(self.list)
        self.printInfo(self.list)
        choice_two = self.inputStr()
        self.appendList(choice_two, self.list)
        print(self.list)
        self.printInfo(self.list)
        choice_three = self.inputStr()
        self.replaceList(choice_three, self.list)
        print(self.list)
        self.printInfo(self.list)


def main():
    action = listReplace()
    action.run()

if __name__ == '__main__':
    main()
