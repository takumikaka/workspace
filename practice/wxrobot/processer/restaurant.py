# -*- coding: utf-8 -*-


#!usr/bin/python
# -*- coding:utf-8 -*-

import requests
import time
from bs4 import BeautifulSoup
import config

class Restaurant(object):

    def __init__(self):
        self.url = 'https://moji.wemomo.com/restaurant'
        self.accept = config.ACCEPT
        self.accept_encoding = config.ACCEPT_ENCODING
        self.accept_language = config.ACCEPT_LANGUAGE
        self.cache_control = config.CACHE_CONTROL
        self.connection = config.CONNECTION
        self.cookie = config.COOKIE
        self.host = config.HOST
        self.upgrade_insecure_requests = config.UPGRADE_INSECURE_REQUESTS
        self.user_agent = config.USER_AGENT

    def set_headers(self):
        headers = {
            'Accept': self.accept,
            'Accept-Encoding': self.accept_encoding,
            'Accept-Language': self.accept_language,
            'Cache-Control': self.cache_control,
            'Connection': self.connection,
            'Cookie': self.cookie,
            'Host': self.host,
            'Upgrade-Insecure-Requests': self.upgrade_insecure_requests,
            'User-Agent': self.user_agent,
        }
        return headers

    def get_restMenu(self, html):
        restMenu = html.find_all('div', attrs={'class':'caption'})
        return restMenu

    def get_lunch(self, restMenu):
        lst = []
        for a in restMenu:
            lunch = a.h4.string
            lst.append(lunch)
        return lst

    def run(self):
        headers =  self.set_headers()
        url = self.url
        r = requests.get(url = url, headers = headers)
        html = r.content
        rt = BeautifulSoup(html, 'html.parser')
        restMenu = self.get_restMenu(rt)
        lunch_lst = self.get_lunch(restMenu)
        return lunch_lst
