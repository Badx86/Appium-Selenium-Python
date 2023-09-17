import time
import SeleniumFramework.utils.Logger as log
from SeleniumFramework.base.BasePage import BasePage


class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact Form
    _selenium_template = "//span[normalize-space()='Selenium Template']"  # xpath
    _contactFormPage = "a[href='Form.html']"  # css
    _formPage = '//div[@class="col-md-6 col-md-offset-3"]'  # xpath
    _enterName = 'name'  # id
    _enterEmail = 'email'  # id
    _genderRadioBtn = "(//input[@type='radio'])[1]"  # xpath
    _enterTechnology = 'tech'  # id
    _enterMessage = 'message'  # id
    _getCapcha = 'captcha_image'  # id
    _enterCapcha = "captcha"  # id
    _postItBtn = "btnContactUs"  # id

    def clickContactForm(self):
        self.clickOnElement(self._selenium_template, 'xpath')
        time.sleep(2)
        self.clickOnElement(self._contactFormPage, 'css')
        log.allureLogs('Clicked on Selenium Template -> Form')

    def verifyFormPage(self):
        element = self.isElementDisplayed(self._formPage, 'xpath')
        assert element == True
        log.allureLogs('Verified Contact Form')

    def enterName(self):
        self.sendText('ExampleName', self._enterName, 'id')
        log.allureLogs('Entered Name')

    def enterEmail(self):
        self.sendText('example@email.com', self._enterEmail, 'id')
        log.allureLogs('Entered Email')

    def chooseGender(self):
        self.clickOnElement(self._genderRadioBtn, 'xpath')
        log.allureLogs('Choose Male gender')

    def enterMessage(self):
        self.sendText('Example Message', self._enterMessage, 'id')
        log.allureLogs('Entered Message')

    def getCapcha(self):
        capcha = self.getText(self._getCapcha, 'id')
        log.allureLogs('Got the captcha data')
        return capcha

    def enterCapcha(self):
        self.sendText(self.getCapcha(), self._enterCapcha, 'id')
        log.allureLogs('Entered captcha')

    def clickOnPostBtn(self):
        self.scrollTo(self._postItBtn, 'id')
        self.clickOnElement(self._postItBtn, 'id')
        log.allureLogs('Clicked on the post button')
