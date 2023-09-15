import unittest
from AppiumFramework.tests.LoginTest import LoginTest
from AppiumFramework.tests.ContactUsFormTest import ContactUsFormTest

cf = unittest.TestLoader().loadTestsFromTestCase(ContactUsFormTest)
lp = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

regressionTest = unittest.TestSuite([cf, lp])

unittest.TextTestRunner(verbosity=1).run(regressionTest)