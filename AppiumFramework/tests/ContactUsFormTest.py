import unittest
import pytest
from AppiumFramework.pages.ContactUsFormPage import ContactForm
import AppiumFramework.utils.CustomLogger as cl


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class ContactUsFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs('App Launched')
        self.cf.clickContactUsButton()
        self.cf.verifyContactPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMobileNo()
        self.cf.clickSubmitButton()

