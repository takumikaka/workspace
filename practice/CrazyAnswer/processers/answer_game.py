# -*- coding: utf-8 -*-
import random
from processers.read_json import readJson

class answerGame(object):
    def __init__(self):
        self.read_json = readJson()
        self.lst_one = ['A', 'B', 'C', 'D']
        self.lst_two = ['A', 'B', 'C']
        self.lst_answer_one = ['A', 'B', 'C', 'D']
        self.lst_answer_two = ['A', 'B', 'C']

    def get_random(self):
        return random.randint(1, 1000)

    def get_dict_answer(self, lst_choice, lst_answer, dict, num, i):
        

    def run(self):
        dict_data = self.read_json.run()
        len_dict = len(dict_data)
        num = self.get_random()
        for i in range(len_dict):
            if dict_data[i]['id'] == str(num):
                print(dict_data[i]['des'])
                if len(dict_data[i]) == 6:
                    lst_option = [dict_data[i]['option1'], dict_data[i]['option2'], dict_data[i]['option3']]
                    random.shuffle(lst_option)
                    dict_answer = {}
                    for j in range(3):
                        print("{0} : {1}".format(self.lst_two[j], lst_option[j]))
                        dict_answer[self.lst_two[j]] = lst_option[j]
                    input_num = input("输入你的选项: ")
                    Flag = True
                    while Flag:
                        if input_num in self.lst_answer_two:
                            value_data = dict_answer[input_num]
                            for k, v in dict_data[i].items():
                                if v == value_data:
                                    if k == 'option1':
                                        print("真棒!")
                                    else:
                                        print("遗憾！错了")
                            Flag = False
                        else:
                            input_num = input("输入你的选项: ")
                            Flag = True
                if len(dict_data[i]) == 7:
                    lst_option = [dict_data[i]['option1'], dict_data[i]['option2'], dict_data[i]['option3'], dict_data[i]['option4']]
                    random.shuffle(lst_option)
                    dict_answer = {}
                    for j in range(4):
                        print("{0} : {1}".format(self.lst_one[j], lst_option[j]))
                        dict_answer[self.lst_one[j]] = lst_option[j]
                    input_num = input("输入你的选项: ")
                    Flag = True
                    while Flag:
                        if input_num in self.lst_answer_one:
                            value_data = dict_answer[input_num]
                            for k, v in dict_data[i].items():
                                if v == value_data:
                                    if k == 'option1':
                                        print("真棒!")
                                    else:
                                        print("遗憾！错了")
                            Flag = False
                        else:
                            input_num = input("输入你的选项: ")
                            Flag = True
