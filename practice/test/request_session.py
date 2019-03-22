# conding:UTF-8 -*-

import requests

class RequestSession(object):
    def __init__(self):
        self.login_url = "https://demo.fastadmin.net/admin/index/login.html"
        self.data = {
                    "username": "admin",
                    "password": "123456"
        }
        self.get_url = "https://demo.fastadmin.net/admin/dashboard?ref=addtabs"

    def run(self):
        login_url = self.login_url
        get_url = self.get_url
        data = self.data
        s = requests.session()
        s.post(url = login_url, data = data)
        html = s.get(url = get_url)
        print(html.text)

def main():
    Action = RequestSession()
    Action.run()

if __name__ == "__main__":
    main()
