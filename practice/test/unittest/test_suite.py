# coding:UTF-8 -*-

import unittest
from test_user_login import TestUserLogin
from test_user_reg import TestUserReg

suit = unittest.TestSuite()
suit.addTest(TestUserLogin("test_user_login_normal"))
suit.addTests([TestUserLogin("test_user_login_normal"), TestUserReg("test_user_reg_exist")])
unittest.TextTestRunner(verbosity=2).run(suit)
