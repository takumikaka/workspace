# coding:UTF-8 -*-

import requests

class RequestCookies(object):
    def __init__(self):
        self.get_url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"
        self.headers = {
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                        "cache-control": "max-age=0",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }
        self.cookies = {
                        "cookie": "PHPSESSID=3e24465d7e9dac3e345b81f44bc5d381; Hm_lvt_58347d769d009bcf6074e9a0ab7ba05e=1552276704; PHPSESSID=0b6792a10f2f171ebc74da79f2b239c3; Hm_lpvt_58347d769d009bcf6074e9a0ab7ba05e=1552286963"
        }

    def run(self):
        html = requests.get(url = self.get_url, headers = self.headers, cookies = self.cookies)
        print(html.text)

def main():
    Action = RequestCookies()
    Action.run()

if __name__ == "__main__":
    main()
