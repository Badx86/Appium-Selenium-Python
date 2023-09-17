import time
from SeleniumFramework.base.BasePage import BasePage
import SeleniumFramework.utils.Logger as log


class EnterText(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact form
    _selenium_template = "//span[normalize-space()='Selenium Template']"  # xpath
    _locatorsPage = 'a[href="seleniumtemplate.html"]'  # css
    _enterTextEditBox = "user_input"  # id
    _submitButton = "submitbutton"  # id

    def clickOnLocatorsPage(self):
        self.clickOnElement(self._selenium_template, 'xpath')
        time.sleep(2)
        self.clickOnElement(self._locatorsPage, "css")

    def enterText(self):
        self.sendText("Example Text", self._enterTextEditBox, "id")
        log.allureLogs("Entered Text in Edit Box")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton, "id")
