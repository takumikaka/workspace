# -*- coding: utf-8 -*-

import requests, sys
import ssl
import json

class getHtml(object):
    def __init__(self):
        self.url = 'https://aip.baidubce.com/oauth/2.0/token'
        self.grant_type = 'client_credentials'
        self.client_id = 'IPieL6yGcFaxeGMksuAE7k8k'
        self.client_secret = '4D0eFPqTlK9ZYAT4GhIROSYFBKTGfi1a'
        self.content_type = 'application/x-www-form-urlencoded'
        self.accept = 'application/json; charset=UTF-8'

    def set_headers(self):
        headers = {'Content_Type': self.content_type,
                   'Accept': self.accept,
        }
        return headers

    def set_host(self):
        host = self.url + '?grant_type=' + self.grant_type + '&client_id=' + self.client_id + '&client_secret=' + self.client_secret
        return host

    def run(self):
        headers = self.set_headers()
        url = self.set_host()
        request = requests.post(url = url, headers = headers)
        content = request.json()
        access_token = content['access_token']
        return(access_token)
