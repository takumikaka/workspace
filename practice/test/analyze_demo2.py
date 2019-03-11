# coding:UTF-8 -*-

import requests
import json

class analyzeDemo2(object):
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
        with open("demo2.json", "r") as f:
            content = f.read()
        return content

    def strTojson(self, str):
        j = json.loads(str)
        return j

    def run(self):
        headers = self.headers
        content = self.readFile()
        j = self.strTojson(content)
        requests_data = j["data"]
        requests_url = j["url"]
        requests_method = j["method"]

        if requests_method == "get":
            html = requests.get(headers = headers, url = requests_url)
            text = html.text
        else:
            html = requests.post(headers = headers, url = requests_url, json = requests_data)
            text = html.text
            status_code = html.status_code
            reason = html.reason
            content = html.content
            headers = html.headers
            cookies = html.cookies

        print(cookies)

def main():
    Action = analyzeDemo2()
    Action.run()

if __name__ == "__main__":
    main()
