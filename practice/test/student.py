# -*- coding: utf-8 -*-

import random

lists = []
a = 1
for i in range(1, 17):
    if i == 1:
        lists.append(a)
    else:
        a = a + 2
        lists.append(a)
print('The lists is:', lists)

Flag = True
num = 0
while Flag:
    sum_1 = lists[0] + lists[8] + lists[9] + lists[10]
    sum_2 = lists[2] + lists[10] + lists[11] + lists[12]
    sum_3 = lists[4] + lists[12] + lists[13] + lists[14]
    sum_4 = lists[5] + lists[6] + lists[7] + lists[15]
    sum_5 = lists[3] + lists[4] + lists[5] + lists[13]
    sum_6 = lists[1] + lists[2] + lists[3] + lists[11]

    if sum_1 == 64 and sum_2 == 64 and sum_3 == 64 and sum_4 == 64 and sum_5 == 64 and sum_6 == 64:
        print('Good lists...', lists)
        Flag = False
    else:
        num = num + 1
        print('Bad lists...shuffle again...', num)
        random.shuffle(lists)
