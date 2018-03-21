# -*- coding: utf-8 -*-


import requests
import json
from processers.get_html import getHtml
from processers.open_file import openFile

class getDit(object):
    def __init__(self):
        self.request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
        self.get_html = getHtml()
        self.open_file = openFile()

    def get_dit(self):
        access_token = self.get_html.run()
        headers = self.get_html.set_headers()
        params = self.open_file.get_params()
        request_url = self.request_url + "?access_token=" + access_token
        request = requests.post(url = request_url, data = params, headers = headers)
        dit = request.json()
        return dit
