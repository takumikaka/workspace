# -*- coding: utf-8 -*-

import time
import random

'''
lineLength = 20
delaySeconds = 0.05
frontSymbol = '='
frontSymbol2 = ['—', '\\', '|', '/']
backSymbol  = ' '

for i in range(10):
    lineTmpla = "{:%s<%s} {} {:<2}"%(backSymbol, lineLength)
    for j in range(lineLength):
        tmpSymbol = frontSymbol2[j%(len(frontSymbol2))]
        print("\r" + lineTmpla.format(frontSymbol * j, tmpSymbol, j), end='')
        time.sleep(delaySeconds)

delaySeconds = 0.5

pokers = [
        "红心 A", "梅花 A", "方片 A", "黑桃 A",
        "红心 2", "梅花 2", "方片 2", "黑桃 2",
        "红心 3", "梅花 3", "方片 3", "黑桃 3",
        "红心 4", "梅花 4", "方片 4", "黑桃 4",
        "红心 5", "梅花 5", "方片 5", "黑桃 5",
        "红心 6", "梅花 6", "方片 6", "黑桃 6",
        "红心 7", "梅花 7", "方片 7", "黑桃 7",
        "红心 8", "梅花 8", "方片 8", "黑桃 8",
        "红心 9", "梅花 9", "方片 9", "黑桃 9",
        "红心 十", "梅花 十", "方片 十", "黑桃 十",
        "红心 J", "梅花 J", "方片 J", "黑桃 J",
        "红心 Q", "梅花 Q", "方片 Q", "黑桃 Q",
        "红心 K", "梅花 K", "方片 K", "黑桃 K",
        ]

for i in range(10):
    j = random.randint(1, 52)
    print("\r" + "{0}".format(pokers[j]), end=' ')
    time.sleep(delaySeconds)
print("\n")

'''

dict = {
        "红心 A":1, "梅花 A":1, "方片 A":1, "黑桃 A":1,
        "红心 2":2, "梅花 2":2, "方片 2":2, "黑桃 2":2,
        "红心 3":3, "梅花 3":3, "方片 3":3, "黑桃 3":3,
        "红心 4":4, "梅花 4":4, "方片 4":4, "黑桃 4":4,
        "红心 5":5, "梅花 5":5, "方片 5":5, "黑桃 5":5,
        "红心 6":6, "梅花 6":6, "方片 6":6, "黑桃 6":6,
        "红心 7":7, "梅花 7":7, "方片 7":7, "黑桃 7":7,
        "红心 8":8, "梅花 8":8, "方片 8":8, "黑桃 8":8,
        "红心 9":9, "梅花 9":9, "方片 9":9, "黑桃 9":9,
        "红心 10":10, "梅花 10":10, "方片 10":10, "黑桃 10":10,
        "红心 J":0.5, "梅花 J":0.5, "方片 J":0.5, "黑桃 J":0.5,
        "红心 Q":0.5, "梅花 Q":0.5, "方片 Q":0.5, "黑桃 Q":0.5,
        "红心 K":0.5, "梅花 K":0.5, "方片 K":0.5, "黑桃 K":0.5,
        }

print(dict)
