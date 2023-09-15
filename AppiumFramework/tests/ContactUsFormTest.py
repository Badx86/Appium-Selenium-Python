import unittest
import pytest
from AppiumFramework.pages.ContactUsFormPage import ContactForm
import AppiumFramework.utils.CustomLogger as cl


@pytest.mark.usefixtures('setup_driver', 'setup_method')
class ContactUsFormTest(unittest.TestCase):
    """
    Класс тестов для формы "Contact Us".
    """

    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        Инициализация объектов класса перед каждым тестом.
        """
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        """
        Тест на открытие формы "Contact Us".
        """
        cl.allureLogs('App Launched')
        self.cf.clickContactUsButton()
        self.cf.verifyContactPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        """
        Тест на заполнение данных в форме "Contact Us".
        """
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMobileNo()
        self.cf.clickSubmitButton()
