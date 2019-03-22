# -*- coding: utf-8 -*-

from processers.open_xls import openXls

class crossLst(object):

    def __init__(self):
        self.open_xls = openXls()

    def get_lst(self, lst, num):
        lst_num = lst[num]
        return lst_num

    def cross_lst(self, lst_one, lst_two):
        str = ""
        len_lst_one = len(lst_one)
        len_lst_two = len(lst_two)
        for i in range(1, len_lst_one):
            for j in range(1, len_lst_two):
                str += "{0}: {1} + {2}: {3}\n".format(lst_one[0], lst_one[i], lst_two[0], lst_two[j])
        return str

    def run(self):
        get_lst = self.open_xls.run()
        lst_one = self.get_lst(get_lst, 0)

        lst_two = self.get_lst(get_lst, 1)
        lst_three = self.get_lst(get_lst, 2)
        lst_four = self.get_lst(get_lst, 3)
        lst_five = self.get_lst(get_lst, 4)
        lst_six = self.get_lst(get_lst, 5)

        data_one = self.cross_lst(lst_one, lst_two)
        data_two = self.cross_lst(lst_one, lst_three)
        data_three = self.cross_lst(lst_one, lst_four)
        data_four = self.cross_lst(lst_one, lst_five)
        data_five = self.cross_lst(lst_one, lst_six)

        return data_one, data_two, data_three, data_four, data_five
