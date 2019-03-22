# coding:UTF-8 -*-

import sys
sys.path.append("..")
from config.config import *

def weather_log_info(wea_date, wea_week, wea_high, wea_low, wea_type, wea_notice):
    logging.info("日期: {0}".format(wea_date))
    logging.info("星期: {0}".format(wea_week))
    logging.info("最高温度: {0}".format(wea_high))
    logging.info("最低温度: {0}".format(wea_low))
    logging.info("天气: {0}".format(wea_type))
    logging.info("需要注意: {0}".format(wea_notice))
