# -*- coding: utf-8 -*-

from processers.cut_img import cutImg
from processers.get_zhidao import getZhidao
from processers.screen_shoot import screenShoot
import time

version = 'V 0.0.3'

screen_shoot = screenShoot()
screen_shoot.run()
time.sleep(0.5)
cut_img = cutImg()
cut_img.run()
get_zhidao = getZhidao()
get_zhidao.run()

print(version)
