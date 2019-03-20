# coding:UTF-8 -*-

import unittest
import requests
import json
from config import *
from read_excel import *
from send_email import *
from HTMLTestReportCN import HTMLTestRunner

class RunAll(unittest.TestCase):
    def test_user_login_normal(self):
        data_case = get_test_data(case_name_one)

        if not data_case:
            logging.info("数据不存在!")

        url = data_case["url"]
        data = data_case["data"]
        expect_data = data_case["expect_data"]

        res = requests.post(url = url, data = json.loads(data))
        rece_data = res.text

        self.assertEqual(rece_data, expect_data)

    def test_user_login_wrong(self):
        data_case = get_test_data(case_name_two)

        if not data_case:
            logging.info("数据不存在!")

        url = data_case["url"]
        data = data_case["data"]
        expect_data = data_case["expect_data"]

        res = requests.post(url = url, data = json.loads(data))
        rece_data = res.text

        self.assertEqual(rece_data, expect_data)

if __name__ == "__main__":
    logging.info("================================== 测试开始 ==================================")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunAll))
    with open(report_file, "wb") as f:
        HTMLTestRunner(stream=f, title="API Report", description="测试详情", tester="C罗").run(suite)
    send_email(report_file)
    logging.info("================================== 测试完毕 ==================================")
