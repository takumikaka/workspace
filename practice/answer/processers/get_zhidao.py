# -*- coding: utf-8 -*-


from processers.analyze_dit import anylizeDit
from bs4 import BeautifulSoup
from urllib import parse
import requests, sys
import json

class getZhidao(object):
    def __init__(self):
        self.analyze_dit = anylizeDit()
        self.url = 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word='
        self.accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        self.accept_encoding = 'gzip, deflate, br'
        self.accept_language = 'zh-CN,zh;q=0.9,en;q=0.8'
        self.connection = 'keep-alive'
        self.cookie = 'BAIDUID=EEF2999B64E2D41A467A353C6C2BE5BE:FG=1; BIDUPSID=EEF2999B64E2D41A467A353C6C2BE5BE; PSTM=1515844908; MCITY=-75%3A; IKUT=6191; H_PS_PSSID=1426_19034_21103_20927; PSINO=3; Hm_lvt_6859ce5aaf00fb00387e6434e4fcc925=1521010322,1521621659,1521621975,1521622009; Hm_lpvt_6859ce5aaf00fb00387e6434e4fcc925=1521622171'
        self.host = 'zhidao.baidu.com'
        self.upgrade_insecure_requests = '1'
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'

    def str_Togbk(self):
        string = self.analyze_dit.run()
        print('题目为:{0}'.format(string))
        return parse.quote(string.encode('gbk'))

    def set_headers(self):
        headers = {'Accept': self.accept,
                   'Accept-Encoding': self.accept_encoding,
                   'Accept-Language': self.accept_language,
                   'Connection': self.connection,
                   'Cookie': self.cookie,
                   'Host': self.host,
                   'Upgrade-Insecure-Requests': self.upgrade_insecure_requests,
                   'User-Agent': self.user_agent,
        }
        return headers

    def set_host(self):
        host = self.url + self.str_Togbk()
        return host

    def run(self):
        headers = self.set_headers()
        url = self.set_host()
        request = requests.post(url = url, headers = headers)
        html = request.content
        zhidao = BeautifulSoup(html, 'html.parser')
        lt = zhidao.find_all('dd', attrs={'class':'dd answer'})
        ans = str(lt[0])
        ans = ans.strip('<dd class="dd answer"><i class="i-answer-text">')
        print('答案为:{0}'.format(ans))
