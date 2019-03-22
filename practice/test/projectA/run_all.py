# coding:UTF-8 -*-

import unittest
from config.config import *
from lib.send_email import *
from lib.HTMLTestReportCN import HTMLTestRunner

logging.info("================================== 测试开始 ==================================")

suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file, "wb") as f:
    HTMLTestRunner(stream=f, title="API Report", description="测试详情", tester="C罗").run(suite)

send_email()

logging.info("================================== 测试开始 ==================================")
