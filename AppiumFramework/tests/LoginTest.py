import unittest
import pytest
import AppiumFramework.utils.CustomLogger as cl
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.LoginPage import LoginPage


@pytest.mark.usefixtures('setup_driver', 'setup_method')
class LoginTest(unittest.TestCase):
    """
    Класс тестов для страницы входа.
    """

    @pytest.fixture(autouse=True)
    def classObjects(self):
        """
        Инициализация объектов класса перед каждым тестом.
        """
        self.lp = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.xfail
    @pytest.mark.run(order=3)
    def test_loginFail(self):
        """
        Тест на неудачный вход в систему.
        """
        cl.allureLogs('App Launched')
        self.lp.clickLoginButton()
        self.lp.enterEmail()
        self.lp.enterInvalidPassword()
        self.lp.clickOnLoginButton()
        self.lp.verifyAdminScreen()

    @pytest.mark.run(order=4)
    def test_loginPass(self):
        """
        Тест на успешный вход в систему.
        """
        self.bp.keyCode(4)
        self.lp.clickLoginButton()
        self.lp.enterEmail()
        self.lp.enterValidPassword()
        self.lp.clickOnLoginButton()
        self.lp.verifyAdminScreen()

    @pytest.mark.run(order=5)
    def test_enterDataEditBox(self):
        """
        Тест на ввод данных в поле для редактирования.
        """
        self.lp.enterText()
        self.lp.clickOnSubmitButton()
