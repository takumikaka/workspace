# -*- coding: utf-8 -*-


import requests
from wxpy import *
import json
import random

bot = Bot()

my_friend = bot.friends().search('熊熊消')[0]

lst = ['穆斯林的骄傲', '老铁', '吃皮', '猛男', '牛皮']

@bot.register(my_friend)
def print_others(msg):
    #random.shuffle(lst)
    my_friend.send(msg)
    print(msg)
    print('send msg:', msg)

@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

embed()
