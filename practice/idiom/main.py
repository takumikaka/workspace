# -*- coding: utf-8 -*-

from processers.analyze_data import analyzeData
from processers.cut_img import cutImg

version = 'V 0.0.3'

cut_img = cutImg()
cut_img.run()
analyze_data = analyzeData()
analyze_data.run()

print(version)
