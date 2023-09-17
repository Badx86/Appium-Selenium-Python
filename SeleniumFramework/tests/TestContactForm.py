import unittest
import pytest
from SeleniumFramework.base.BasePage import BasePage
from SeleniumFramework.pages.ContactFormPage import ContactForm
import SeleniumFramework.utils.Logger


@pytest.mark.usefixtures('setup_driver', 'setup_method')
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.chooseGender()
        self.cf.enterMessage()
        self.cf.getCapcha()
        self.cf.enterCapcha()
        self.cf.clickOnPostBtn()

    @pytest.mark.run(order=1)
    def test_formPage(self):
        self.cf.clickContactForm()
        self.cf.verifyFormPage()
