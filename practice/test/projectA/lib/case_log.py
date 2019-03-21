# coding:UTF-8 -*-

import json
import sys
sys.path.append("..")
from config.config import *

def log_case_info(case_name, url, data, expect_data, res_data):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)

    logging.info("测试用例: {0}".format(case_name))
    logging.info("测试链接: {0}".format(url))
    logging.info("发送数据: {0}".format(data))
    logging.info("期望数据: {0}".format(expect_data))
    logging.info("实际数据: {0}".format(res_data))
