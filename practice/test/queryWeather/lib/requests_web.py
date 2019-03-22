# coding:UTF-8 -*-

import requests
import json
import sys
import re
sys.path.append("..")
from lib.get_city_id import *
from lib.weather_log_info import *

city_id = re.sub("CN", "", get_city_id("成都"))
url = "http://t.weather.sojson.com/api/weather/city/{0}".format(city_id)

res = requests.get(url=url)
str_2dict = json.loads(res.text)

today_data = str_2dict["data"]["forecast"][0]

wea_date = today_data["ymd"]
wea_week = today_data["week"]
wea_high = today_data["high"]
wea_low = today_data["low"]
wea_type = today_data["type"]
wea_notice = today_data["notice"]

weather_log_info(wea_date, wea_week, wea_high, wea_low, wea_type, wea_notice)
