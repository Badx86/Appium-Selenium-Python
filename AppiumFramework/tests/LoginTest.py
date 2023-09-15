import unittest
import pytest
import AppiumFramework.utils.CustomLogger as cl
from AppiumFramework.base.BasePage import BasePage
from AppiumFramework.pages.LoginPage import LoginPage


@pytest.mark.usefixtures('beforeClass', 'beforeMethod')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPage(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.xfail
    @pytest.mark.run(order=3)
    def test_loginFail(self):
        cl.allureLogs('App Launched')
        self.lp.clickLoginButton()
        self.lp.enterEmail()
        self.lp.enterInvalidPassword()
        self.lp.clickOnLoginButton()
        self.lp.verifyAdminScreen()

    @pytest.mark.run(order=4)
    def test_loginPass(self):
        self.bp.keyCode(4)
        self.lp.clickLoginButton()
        self.lp.enterEmail()
        self.lp.enterValidPassword()
        self.lp.clickOnLoginButton()
        self.lp.verifyAdminScreen()

    @pytest.mark.run(order=5)
    def test_enterDataEditBox(self):
        self.lp.enterText()
        self.lp.clickOnSubmitButton()
