# coding:UTF-8 -*-

#########################################
# 1、获取token
# 2、识别图片文字
#########################################

import requests
import json

class GetPicApi(object):
    def __init__(self):
        self.get_tokenurl = "https://aip.baidubce.com/oauth/2.0/token"
        self.send_data = {
                        "grant_type": "client_credentials",
                        
        }
        self.get_picurl = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        self.data = {
                    "url": "https://upload-images.jianshu.io/upload_images/7575721-40c847532432e852.png"
        }

    def get_token(self):
        html = requests.post(url = self.get_tokenurl, params = self.send_data)
        dict_list = json.loads(html.text)
        access_token = dict_list["access_token"]
        return access_token

    def get_pictext(self, access_token):
        new_url = self.get_picurl + "?access_token=" + access_token
        html = requests.post(url = new_url, data = self.data)
        print((json.dumps(html.json(), indent = 2, ensure_ascii = False)))


    def run(self):
        access_token = self.get_token()
        self.get_pictext(access_token)


def main():
    Action = GetPicApi()
    Action.run()

if __name__ == "__main__":
    main()
