# -*- coding: utf-8 -*-

from wxpy import *
from processer.robot import Robot

version = '0.0.1'

bot = Robot()
bot.send_msg_process()
print('Version:{0}'.format(version))

embed()
