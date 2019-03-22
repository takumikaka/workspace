# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import json

class WeatherApi(object):
    def __init__(self):
        self.url = "http://t.weather.sojson.com/api/weather/city/"

    def _set_headers(self):
        headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Cache-Control": "max-age=0",
                    "Connection": "keep-alive",
                    "Host": "t.weather.sojson.com",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        }

        return headers

    def _read_json(self, city_name):
        with open("_city.json", "r") as f:
            content = f.read()
        list1 = json.loads(content)
        for i in range(len(list1)):
            if list1[i]["city_name"] == city_name:
                return list1[i]["city_code"]
            else:
                pass

    def _input_city(self):
        city_name = raw_input("请输入城市名:")
        city_name = city_name.decode("utf-8")
        return city_name

    def run(self):
        city_name = self._input_city()
        city_code = self._read_json(city_name)
        try:
            url = self.url + city_code
            headers = self._set_headers()
            r = requests.get(url=url, headers=headers)
            html = r.content
            content = json.loads(html)
            #print(content["cityInfo"]["parent"])
            print(content)
        except Exception as e:
            print("city not found")

def main():
    Action = WeatherApi()
    Action.run()

if __name__ == '__main__':
    main()
