# coding:UTF-8 -*-

import unittest
import requests
from db import *

NOT_EXISI_USER = "陈真"
EXIST_USRE = "范冰冰"

db = DB()

class TestUserReg(unittest.TestCase):
    url = "http://115.28.108.130:5000/api/user/reg/"

    def test_user_reg_nomal(self):
        if db.check_user(NOT_EXISI_USER):
            db.del_user(NOT_EXISI_USER)

        data = {"name": NOT_EXISI_USER, "password": "123456"}
        res = requests.post(url = self.url, json = data)

        expect_data = {
                        "code": "100000",
                        "data": {
                                "name": NOT_EXISI_USER,
                                "password": "e10adc3949ba59abbe56e057f20f883e"
                                },
                        "msg": "成功"
                        }

        self.assertEqual(res.json(), expect_data)

        db.add_user("陈真", "123456")

        self.assertTrue(db.check_user(NOT_EXISI_USER))

        db.del_user(NOT_EXISI_USER)

    def test_user_reg_exist(self):
        if not db.check_user(EXIST_USRE):
            db.add_user(EXIST_USRE, "123456")

        data = {"name": EXIST_USRE, "password": "123456"}
        res = requests.post(url = self.url, json = data)

        expect_data = {
                        "code": "100001",
                        "data": {
                                "name": EXIST_USRE,
                                "password": "e10adc3949ba59abbe56e057f20f883e"
                                },
                        "msg": "失败，用户已存在"
                        }

        self.assertEqual(res.json(), expect_data)

if __name__ == "__main__":
    unittest.main(verbosity=2)
