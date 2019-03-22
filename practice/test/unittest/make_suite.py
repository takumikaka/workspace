# coding:utf-8 -*-

import unittest
from test_user_login import TestUserLogin

suit1 = unittest.makeSuite(TestUserLogin, "test_user_login_normal")
suit2 = unittest.makeSuite(TestUserLogin)

unittest.TextTestRunner(verbosity=2).run(suit2)
