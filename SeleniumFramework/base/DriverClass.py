from selenium import webdriver
from SeleniumFramework.utils.Logger import Logger


class WebDriverClass:
    log = Logger()

    def getWebDriver(self, browser):
        driver = None

        if browser == 'Chrome':
            driver = webdriver.Chrome()
            self.log.info("Chrome Driver is initializing")
        elif browser == 'Firefox':
            driver = webdriver.Firefox()
            self.log.info("FireFox Driver is initializing")
        elif browser == 'Edge':
            driver = webdriver.Edge()
            self.log.info("Edge Driver is initializing")

        return driver
