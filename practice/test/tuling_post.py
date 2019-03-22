# -*- coding:UTF-8 -*-

import requests
import json

class TulingTest(object):
    def __init__(self):
        self.web_url = "http://openapi.tuling123.com/openapi/api/v2"
        self.headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "h-CN,zh;q=0.9,en;q=0.8",
                        "Cache-Control": "max-age=0",
                        "Connection": "keep-alive",
                        "Host": "www.tuling123.com",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.data = {
                    "reqType":0,
                    "perception": {
                        "inputText": {
                            "text": "附近的酒吧"
                        },
                        "inputImage": {
                            "url": "imageUrl"
                        },
                        "selfInfo": {
                            "location": {
                                "city": "成都",
                                "province": "",
                                "street": "春熙路"
                            }
                        }
                    },
                    "userInfo": {
                        "apiKey": "0cb72a7c84c3433eafeb2d727bd4ecc0",
                        "userId": "223516",
                    }
        }

    def run(self):
        url = self.web_url
        headers = self.headers
        data = self.data
        inquire_info = raw_input("请输入你想要查询的内容: ")
        inquire_city = raw_input("请输入你想要查询的城市: ")
        inquire_street = raw_input("请输入你想要查询的街道: ")

        #data = json.dumps(self.data)
        data["perception"]["inputText"]["text"] = inquire_info
        data["perception"]["selfInfo"]["location"]["city"] = inquire_city
        data["perception"]["selfInfo"]["location"]["street"] = inquire_street

        html = requests.post(url = url, headers = headers, json = data)
        print(html.text)

def main():
    Action = TulingTest()
    Action.run()

if __name__ == "__main__":
    main()
