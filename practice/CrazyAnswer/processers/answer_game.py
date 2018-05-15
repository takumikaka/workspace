# -*- coding: utf-8 -*-
import random
import time
from processers.read_json import readJson
from processers.get_score import getScore

class answerGame(object):
    def __init__(self):
        self.read_json = readJson()
        self.get_score = getScore()
        self.lst_one = ['A', 'B', 'C', 'D']
        self.lst_two = ['A', 'B', 'C']
        self.lst_answer_one = ['A', 'B', 'C', 'D']
        self.lst_answer_two = ['A', 'B', 'C']
        self.lst_score = []

    def get_random(self):
        return random.randint(1, 1000)

    def get_answer(self, lst_choice, lst_option, num):
        dict_answer = {}
        for j in range(num):
            print("{0} : {1}".format(lst_choice[j], lst_option[j]))
            dict_answer[lst_choice[j]] = lst_option[j]
        return dict_answer

    def comp_result(self, input_num, lst_answer, dict_answer, dict, i, time_result):
        Flag = True
        while Flag:
            if input_num in lst_answer:
                value_data = dict_answer[input_num]
                for k, v in dict[i].items():
                    if v == value_data:
                        if k == 'option1':
                            score = self.get_score.get_one_score(time_result)
                            print("真棒! 得分: {0}".format(int(score)))
                        else:
                            print("遗憾！错了")
                            score = 0
                Flag = False
            else:
                input_num = input("输入你的选项: ")
                Flag = True
        return score

    def get_dict_answer_one(self, lst_choice_one, lst_answer_one, lst_choice_two, lst_answer_two, dict, i, time_orig):
        if len(dict[i]) == 6:
            lst_option = [dict[i]['option1'], dict[i]['option2'], dict[i]['option3']]
            random.shuffle(lst_option)
            dict_answer = self.get_answer(lst_choice_one, lst_option, 3)
            input_num = input("输入你的选项: ")
            time_one = int(time.time())
            time_result = time_one - time_orig
            score = self.comp_result(input_num, lst_answer_one, dict_answer, dict, i, time_result)
        else:
            lst_option = [dict[i]['option1'], dict[i]['option2'], dict[i]['option3'], dict[i]['option4']]
            random.shuffle(lst_option)
            dict_answer = self.get_answer(lst_choice_two, lst_option, 4)
            input_num = input("输入你的选项: ")
            time_two = int(time.time())
            time_result = time_two - time_orig
            score = self.comp_result(input_num, lst_answer_two, dict_answer, dict, i, time_result)
        return score

    def run(self):
        dict_data = self.read_json.run()
        len_dict = len(dict_data)
        num = self.get_random()
        for i in range(len_dict):
            if dict_data[i]['id'] == str(num):
                print(dict_data[i]['des'])
                time_orig = int(time.time())
                score = self.get_dict_answer_one(self.lst_one, self.lst_two, self.lst_answer_one, self.lst_answer_two, dict_data, i, time_orig)

        print(score)
