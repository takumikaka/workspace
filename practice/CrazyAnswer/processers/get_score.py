# -*- coding: utf-8 -*-


class getScore(object):
    def __init__(self):
        pass

    def get_one_score(self, time):
        score = 150 - (150/15)*time
        return score

    def get_lst_score(self, score, lst_score):
        return lst_score.append(score)

    def get_total_score(self, lst_score):
        sum = 0
        for i in range(len(lst_score)):
            sum = sum + lst_score[i]
        return sum
