from SeleniumFramework.base.DriverClass import WebDriverClass
from SeleniumFramework.base.BasePage import BasePage
from SeleniumFramework.pages.ContactFormPage import ContactForm

wd = WebDriverClass()

driver = wd.getWebDriver('Chrome')
bp = BasePage(driver)
cf = ContactForm(driver)

bp.launchWebPage('http://www.dummypoint.com/', 'General Dashboard — DummyPoint')
bp.isElementDisplayed('//input[@placeholder="Search"]', 'xpath')
bp.sendText('find something interesting', '//input[@placeholder="Search"]', 'xpath')
bp.clickOnElement('//button[@class="btn"]', 'xpath')

driver.quit()
