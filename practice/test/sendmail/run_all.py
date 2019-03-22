# coding:UTF-8 -*-

import unittest
from HTMLTestReportCN import HTMLTestRunner
from config import *
from send_email import send_email

class RunAll(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(1, 1)

    def test_case_two(self):
        self.assertTrue(1)

if __name__ == "__main__":
    logging.info("================================== 测试开始 ==================================")

    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(RunAll))

    with open("report.html", "wb") as f:
        HTMLTestRunner(stream=f, title="API Report", description="测试报告", tester="C罗").run(suit)

    send_email("report.html")

    logging.info("================================== 测试开始 ==================================")
