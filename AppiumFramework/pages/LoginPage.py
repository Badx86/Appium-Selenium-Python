from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utils.CustomLogger as cl


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values 'Login Page' form
    _loginButton = 'com.code2lead.kwad:id/Login'  # id
    _enterEmail = 'Enter Email'  # text
    _enterPassword = 'Enter Password'  # text
    _loginPageButton = 'LOGIN'  # text
    _wrongCredentialsText = 'Wrong Credentials'  # text
    _pageTitle = 'Enter Admin'  # text
    _enterText = 'com.code2lead.kwad:id/Edt_admin'  # id
    _submitButton = 'com.code2lead.kwad:id/Btn_admin_sub'  # id

    def clickLoginButton(self):
        self.clickElement(self._loginButton, 'id')
        cl.allureLogs('Click on "Login" button')

    def enterEmail(self):
        self.sendText('admin@gmail.com', self._enterEmail, 'text')
        cl.allureLogs('Entered Email')

    def enterValidPassword(self):
        self.sendText('admin123', self._enterPassword, 'text')
        cl.allureLogs('Entered Password')

    def enterInvalidPassword(self):
        self.sendText('admin123666', self._enterPassword, 'text')
        cl.allureLogs('Entered Password')

    def clickOnLoginButton(self):
        self.clickElement(self._loginPageButton, 'text')
        cl.allureLogs('Click on "Login" button')

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle, 'text')
        assert adminScreen == True
        cl.allureLogs('Opened Admin Screen')

    def enterText(self):
        self.sendText('Admin', self._enterText, 'id')
        cl.allureLogs('Entered Text')

    def clickOnSubmitButton(self):
        self.clickElement(self._submitButton, 'id')
        cl.allureLogs('Click on "Submit" button')


