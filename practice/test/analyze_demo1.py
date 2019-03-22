# -*- coding:UTF-8 -*-

import json
import requests

############################################
#读取文件
#转换为字典并获取值
#发送请求
#获取相应
############################################

class analyzeDemo1(object):
    def __init__(self):
        self.headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                        "Cache-Control": "max-age=0",
                        "Connection": "keep-alive",
                        "Host": "www.tuling123.com",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }

    def readFile(self):
        with open("demo1.json", "r") as f:
            content = f.read()
        return content

    def strTodict(self, content):
        list_dict = json.loads(content)
        return list_dict

    def run(self):
        content = self.readFile()
        list_dict = self.strTodict(content)
        headers = self.headers

        #获取对应的值
        requests_url = list_dict["url"]
        requests_method = list_dict["method"]
        requests_key = list_dict["params"]["key"]
        requests_info = list_dict["params"]["info"]

        params = {
                "key": requests_key,
                "info": requests_info
        }

        if requests_method == "get":
            html = requests.get(headers = headers, url = requests_url, params = params)
            text = html.text
        else:
            html = requests.post(headers = headers, url = requests_url, params = params)
            text = html.text

        print(text)

def main():
    Action = analyzeDemo1()
    Action.run()

if __name__ == "__main__":
    main()
