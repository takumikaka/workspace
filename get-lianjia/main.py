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

    def _set_str(self):
        str = raw_input('Input the name:')
        return str

    def _set_url(self, str):
        url = "https://cd.lianjia.com/ershoufang/rs{0}/".format(str)
        return url

    def _set_headers(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'Keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        return headers

    def _get_Price(self, html):
        price = html.find_all('div', attrs={'class':'priceInfo'})
        return price

    def _get_totalPrice(self, price):
        tp = []
        for a in price:
            totalPrice = a.span.string
            tp.append(totalPrice)
        return tp

    def _get_houseInfo(self, html):
        houseInfo = html.find_all('div', attrs={'class':'houseInfo'})
        return houseInfo

    def _get_houseInfoList(self, houseInfo):
        hi = []
        for a in houseInfo:
            house = a.get_text()
            hi.append(house)
        return hi

    def _get_followInfo(self, html):
        followInfo = html.find_all('div', attrs={'class':'followInfo'})
        return followInfo

    def _followList(self, followInfo):
        fi = []
        for a in followInfo:
            follow = a.get_text()
            fi.append(follow)
        return fi

    def _printList(self, list):
        for i in list:
            print(i)

    def _set_houseDt(self, tp, hi, fi):
        houseDt = pd.DataFrame({'TotalPrice':tp, 'HouseInfo':hi, 'FollowInfo':fi})
        return houseDt

    def _set_housePrice(self, tp):
        housePrice = pd.DataFrame({'总价[万]':tp})
        return housePrice

    def _set_houseInfoSplit(self, house):
        houseInfo_split = pd.DataFrame((x.split('|') for x in house.HouseInfo), index=house.index, columns=['小区', '户型', '面积', '朝向', '装修', '电梯'])
        return houseInfo_split

    def _set_followInfoSplit(self, house):
        followInfo_split = pd.DataFrame((x.split('/') for x in house.FollowInfo), index=house.index, columns=['关注人数', '带看次数', '发布时间'])
        return followInfo_split

    def _merge_info(self, totalInfo, info_split):
        merge_info = pd.merge(totalInfo, info_split, right_index=True, left_index=True)
        return merge_info

    def run(self):
        headers = self._set_headers()
        #str = self._set_str()
        str = '锦江城市花园三期'
        url = self._set_url(str)
        r = requests.get(url=url, headers=headers)
        html = r.content
        lj = BeautifulSoup(html, 'html.parser')
        price = self._get_Price(lj)
        tp = self._get_totalPrice(price)
        houseInfo = self._get_houseInfo(lj)
        hi = self._get_houseInfoList(houseInfo)
        followInfo = self._get_followInfo(lj)
        fi = self._get_houseInfoList(followInfo)
        house = self._set_houseDt(tp, hi, fi)
        housePrice = self._set_housePrice(tp)
        houseinfo_split = self._set_houseInfoSplit(house)
        #house = self._merge_info(house, houseinfo_split)
        followInfo_split = self._set_followInfoSplit(house)
        #house = self._merge_info(house, followInfo_split)
        new_info = self._merge_info(houseinfo_split, followInfo_split)
        total_info = self._merge_info(new_info, housePrice)
        print(total_info)
	print('test')

####################################################################

def main():
    action = Action()
    action.run()

if __name__=='__main__':
    main()
