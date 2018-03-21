# -*- coding: utf-8 -*-

from processers.analyze_data import analyzeData
from processers.screen_shoot import screenShoot
from processers.cut_img import cutImg

version = 'V 0.0.4'

screen_shoot = screenShoot()
screen_shoot.run()
cut_img = cutImg()
cut_img.run()
analyze_data = analyzeData()
analyze_data.run()

print(version)
