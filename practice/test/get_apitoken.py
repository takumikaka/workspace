# coding:UTF-8 -*-

import requests
import json

class GetApiToken(object):

    def __init__(self):
        self.get_url = "https://aip.baidubce.com/oauth/2.0/token"
        self.data = {
                    "grant_type": "client_credentials",
                    
        }

    def run(self):
        html = requests.post(url = self.get_url, params = self.data)
        content = html.text
        dict_list = json.loads(content)
        print(dict_list["access_token"])

def main():
    Action = GetApiToken()
    Action.run()

if __name__ == "__main__":
    main()
