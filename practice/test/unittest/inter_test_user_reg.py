# coding:UTF-8

import unittest
import requests
import json
from read_excel import *

class InterTestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("test_user_data.xlsx", "TestUserReg")

    def test_user_reg_exist(self):
        case_data = get_test_data(self.data_list, "test_user_reg_exist")

        if not case_data:
            print("数据不存在!")

        url = case_data["url"]
        data = case_data["data"]
        expect_data = case_data["expect_data"]

        res = requests.post(url = url, json = json.loads(data))
        res_data = res.json()

        self.assertDictEqual(res_data, json.loads(expect_data))

if __name__ == "__main__":
    unittest.main(verbosity=2)
