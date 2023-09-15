from AppiumFramework.base.BasePage import BasePage
import AppiumFramework.utils.CustomLogger as cl


class ContactForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values 'Contact Us Form'
    _contactUsButton = 'com.code2lead.kwad:id/ContactUs'  # id
    _pageTitle = 'Contact Us form'  # text
    _inputName = 'com.code2lead.kwad:id/Et2'
    _inputEmail = 'com.code2lead.kwad:id/Et3'
    _inputAddress = 'com.code2lead.kwad:id/Et6'
    _inputMobileNo = 'com.code2lead.kwad:id/Et7'
    _submitButton = 'com.code2lead.kwad:id/Btn2'

    def clickContactUsButton(self):
        self.clickElement(self._contactUsButton, 'id')
        cl.allureLogs('Click on "Contact Us Form" button')

    def verifyContactPage(self):
        element = self.isDisplayed(self._pageTitle, 'text')
        assert element == True
        cl.allureLogs('Contact Us Form page is opened')

    def enterName(self):
        self.sendText('John Smith', self._inputName, 'id')
        cl.allureLogs('Entered Name')

    def enterEmail(self):
        self.sendText('j.smith00@yahoo.com', self._inputEmail, 'id')
        cl.allureLogs('Entered Email')

    def enterAddress(self):
        self.sendText('Linkoln street 8801', self._inputAddress, 'id')
        cl.allureLogs('Entered Address')

    def enterMobileNo(self):
        self.sendText('8(800)555-35-35', self._inputMobileNo, 'id')
        cl.allureLogs('Entered Mobile Number')

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, 'id')
        cl.allureLogs('Click on "Submit" button')
