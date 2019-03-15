# coding:UTF-8 -*-

import unittest
from test_user_login import TestUserLogin

suit1 = unittest.TestSuite()
suit1.addTest(TestUserLogin("test_user_login_normal"))

suit2 = unittest.makeSuite(TestUserLogin, "test_user_login_normal")

#suit = unittest.TestSuite([suit1, suit2])
suit = unittest.TestSuite()
suit.addTests([suit1, suit2])

unittest.TextTestRunner(verbosity=2).run(suit)
