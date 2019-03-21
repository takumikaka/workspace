# coding:UTF-8 -*-

import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import *

logging.info("================================== 测试开始 ==================================")

suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file, "wb") as f:
    HTMLTestRunner(stream=f, title="API Test", description="测试详情", tester="C罗").run(suite)

send_email()

logging.info("================================== 测试结束 ==================================")
