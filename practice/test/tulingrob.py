# -*- coding: utf-8 -*-

import requests
from wxpy import *
import json

def talk_robot(info = '你叫什么名字'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '0cb72a7c84c3433eafeb2d727bd4ecc0'
    data = {'key': apikey,
            'info': info,
    }
    req = requests.post(api_url, data = data).text
    replys = json.loads(req)['text']
    return replys

rebot = Bot()

@rebot.register()
def replay_my_friends(msg):
    message = '{}'.format(msg.text)
    replys = talk_robot(info = message)
    return replys

embed()
#rebot.start()
