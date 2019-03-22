# coding:UTF-8 -*-

from config import *
import json

def log_case_info(case_name, url, data, expect_data, res_data):
    if isinstance(data, dict):
        data = json.dumps(data, ensure_ascii = False)

    logging.info("测试用例: {0}".format(case_name))
    logging.info("url: {0}".format(url))
    logging.info("请求参数: {0}".format(data))
    logging.info("预期结果: {0}".format(expect_data))
    logging.info("实际结果: {0}".format(res_data))
