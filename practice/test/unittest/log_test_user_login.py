# coding:UTF-8 -*-

import unittest
import json
import requests
from read_excel import *
from config import *

class LogTestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserLogin")

    def test_log_user_login(self):
        case_data = get_test_data(self.data_list, "test_user_login_normal")

        if not case_data:
            logging.info("数据不存在!")

        url = case_data["url"]
        data = case_data["data"]
        expect_data = case_data["expect_data"]
        res = requests.post(url=url, data=json.loads(data))

        logging.info("测试用例: {0}".format("test_user_login_normal"))
        logging.info("url: {0}".format(url))
        logging.info("请求参数: {0}".format(data))
        logging.info("预期结果: {0}".format(expect_data))
        logging.info("实际结果: {0}".format(res.text))

        self.assertEqual(res.text, expect_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)
