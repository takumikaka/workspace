# -*- coding: utf-8 -*-

from processers.answer_game import answerGame
from processers.get_score import getScore

class forTens(object):
    def __init__(self):
        self.lst_score = []
        self.answer_game = answerGame()
        self.get_score = getScore()

    def run(self):
        for i in range(10):
            print("当前第{0}题".format(i+1))
            score = self.answer_game.run()
            self.lst_score.append(score)
        sum = self.get_score.get_total_score(self.lst_score)
        print("游戏结束，你的总分为: {0}".format(int(sum)))
