# -*- coding:UTF-8 -*-

import requests
import json

class TulingTest(object):
    def __init__(self):
        self.web_url = "http://www.tuling123.com/openapi/api"
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

    def input_str(self):
        input_str = raw_input("我:")
        return input_str

    def run(self):
        print("你好，我叫机器人小蕊，很高兴认识你!")
        url = self.web_url

        flag = True
        while flag:
            str = self.input_str()
            if str == "再见":
                print("再见，小蕊要睡觉了，拜拜!")
                flag = False
            else:
                params = {"key":"0cb72a7c84c3433eafeb2d727bd4ecc0", "info":str}
                headers = self.headers
                html = requests.get(url = url, params = params, headers = headers)
                content = html.content
                j = json.loads(content)
                print(j["text"])

def main():
    Action = TulingTest()
    Action.run()

if __name__ == "__main__":
    main()
