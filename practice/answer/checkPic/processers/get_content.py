# -*- coding: utf-8 -*-

from processers.get_car import getCar

class getContent(object):
    def __init__(self):
        self.get_car = getCar()

    def run(self):
        content = self.get_car.run()
        lst_result = content['result']
        good_result = lst_result[0]

        ans = '车名: ' + good_result['name']
        ans += '\n年份: ' + good_result['year']
        ans += '\n相识度: ' + '%.2f%%' % (good_result['score'] * 100)
        ans += '\n颜色: ' + content['color_result']
        print(ans)
