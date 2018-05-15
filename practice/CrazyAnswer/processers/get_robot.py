# -*- coding: utf-8 -*-

import time
import random
from processers.get_score import getScore

class getRobot(object):
    def __init__(self):
        self.get_score = getScore()
        self.lst_option = ["option1", "option2", "option3"]

    def random_lst(self, lst):
        random.shuffle(lst)
        return lst

    def random_time(self):
        time = int(random.randint(1, 10) * 0.5)
        return time

    def check_answer(self, robot_answer, robot_answer_time):
        if (robot_answer == "option1"):
            score = self.get_score.get_one_score(robot_answer_time)
        else:
            score = 0
        return score

    def run(self):
        self.random_lst(self.lst_option)
        robot_answer_time = self.random_time()
        robot_answer = self.lst_option[0]
        score = self.check_answer(robot_answer, robot_answer_time)
        return score
