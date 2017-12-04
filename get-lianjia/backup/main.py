#!usr/bin/python
# -*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

###################################################################
def red(text):
	return '\033[91m{0}\033[00m'.format(text)

def green(text):
	return '\033[92m{0}\033[00m'.format(text)

def yellow(text):
	return '\033[93m{0}\033[00m'.format(text)
###################################################################

class Action(object):

    def __init__(self):
        pass

    def _save_file(self, html):
        fh = open('test.html', 'w')
        fh.write(str(html))
        fh.close()

    def _set_url(self):
        url = "https://cd.lianjia.com/ershoufang/"
        return url

    def _set_page(self):
        page = 'pg'
        return page

    def _set_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'Keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
        return headers

    def run(self):
        headers = self._set_headers()
        url_old = self._set_url()
        page = self._set_page()
        url = url_old+'rs锦江城市花园三期'+'/'
        r = requests.get(url=url, headers=headers)
        html = r.content

        '''
        for i in range(1, 2):
            if i == 1:
                i = str(i)
                a = (url+page+i+'/')
                r = requests.get(url=a, headers=headers)
                html = r.content
            else:
                i = str(i)
                a = (url+page+i+'/')
                r = requests.get(url=a, headers=headers)
                html2 = r.content
                html = html + html2
            time.sleep(0.5)
        '''

        lj = BeautifulSoup(html, 'html.parser')
        price = lj.find_all('div', attrs={'class':'priceInfo'})
        tp = []
        for a in price:
            totalPrice = a.span.string
            tp.append(totalPrice)
        #print('tp list:\n', tp)

        houseInfo = lj.find_all('div', attrs={'class':'houseInfo'})
        hi = []
        for b in houseInfo:
            house = b.get_text()
            hi.append(house)
        #print('hi list:\n', hi)

        followInfo = lj.find_all('div', attrs={'class':'followInfo'})
        fi = []
        for c in followInfo:
            follow = c.get_text()
            fi.append(follow)

        house = pd.DataFrame({'totalPrice':tp, 'houseInfo':hi, 'followInfo':fi})
        #print(house.head())

        houseinfo_split = pd.DataFrame((x.split('|') for x in house.houseInfo), index=house.index, columns=['xiaoqu', 'huixng', 'mianji', 'chaoxiang', 'zhuangxiu', 'dianti'])
        print(houseinfo_split.head())

####################################################################

def main():
    action = Action()
    action.run()

if __name__=='__main__':
    main()
