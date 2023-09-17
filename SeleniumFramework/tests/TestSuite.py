import unittest
from SeleniumFramework.tests.TestContactForm import ContactFormTest
from SeleniumFramework.tests.TestLocatorsSection import EnterTextTest


cf = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
et = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)

regressionTest = unittest.TestSuite([cf, et])

unittest.TextTestRunner(verbosity=1).run(regressionTest)

