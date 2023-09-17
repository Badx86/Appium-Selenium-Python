import time
import unittest
import pytest
from SeleniumFramework.pages.LocatorsPage import EnterText


@pytest.mark.usefixtures('setup_driver', 'setup_method')
class EnterTextTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)

    @pytest.mark.run(order=4)
    def test_enterDataInEditBox(self):
        self.driver.maximize_window()
        self.et.enterText()
        self.et.clickOnSubmitButton()

    @pytest.mark.run(order=3)
    def test_clickOnLocatorsPage(self):
        self.et.clickOnLocatorsPage()
