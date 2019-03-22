# -*- coding: utf-8 -*-

from processers.answer_game import answerGame
from processers.get_score import getScore
from processers.get_robot import getRobot
import time

class forTens(object):
    def __init__(self):
        self.lst_score_user = []
        self.lst_score_robot = []
        self.answer_game = answerGame()
        self.get_score = getScore()
        self.get_robot = getRobot()

    def run(self):
        for i in range(10):
            time.sleep(1)
            print("当前第{0}题".format(i+1))
            score_user = self.answer_game.run()
            score_robot = self.get_robot.run()
            self.lst_score_user.append(score_user)
            self.lst_score_robot.append(score_robot)
        sum_user = self.get_score.get_total_score(self.lst_score_user)
        sum_robot = self.get_score.get_total_score(self.lst_score_robot)
        print("游戏结束，你的总分为: {0}".format(int(sum_user)))
        print("游戏结束，机器人的总分为: {0}".format(int(sum_robot)))
