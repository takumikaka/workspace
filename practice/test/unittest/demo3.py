# coding:UTF-8 -*-

from HTMLTestReportCN import HTMLTestRunner
import unittest

class Mytest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("foo".upper().isupper())
        self.assertFalse("foo".isupper())

    def test_split(self):
        str = "Hello World"
        self.assertEqual(str.split(), ["Hello", "World"])
        with self.assertRaises(TypeError):
            str.split(2)

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    #test_suite.addTest(unittest.makeSuite(Mytest))
    test_suite.addTest(Mytest("test_isupper"))
    with open("demo3.html", "wb") as fp:
        runner = HTMLTestRunner(stream=fp, title="Demo3测试报告", description="测试详情")
        runner.run(test_suite)
