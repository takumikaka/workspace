# -*- coding: utf-8 -*-


from processer.save_img import saveImg
from processer.get_result import class_get_result

version = 'V0.0.1'

save_img = saveImg()
save_img.run()
getResult = class_get_result()
getResult.run()

print(version)
