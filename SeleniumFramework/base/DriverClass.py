from selenium import webdriver
from SeleniumFramework.utils.Logger import Logger
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

import configparser

config = configparser.ConfigParser()
config_path = r'C:\Users\мвидео\PycharmProjects\Appium-Selenium-Python\SauceLabsTest\config.ini'
config.read(config_path)


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

    def getOptionsForBrowser(self, browser_name):
        if browser_name == 'Chrome':
            return ChromeOptions()
        elif browser_name == 'Firefox':
            return FirefoxOptions()
        elif browser_name == 'Edge':
            return EdgeOptions()

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    def cloudDriver(self, platform_name, browser_version, browser_name):

        options = self.getOptionsForBrowser(browser_name)
        options.browser_version = browser_version
        options.platform_name = platform_name

        sauce_options = {}
        sauce_options['username'] = config['sauce']['username']
        sauce_options['accessKey'] = config['sauce']['access_key']
        sauce_options['build'] = 'Versoin 1'
        sauce_options['name'] = 'Dummy Point Test Framework'
        sauce_options['screenResolution'] = '1280x1024'
        sauce_options['tags'] = ['Framework', 'pytest']

        options.set_capability('sauce:options', sauce_options)

        url = (f"https://{sauce_options['username']}:{sauce_options['accessKey']}@ondemand.eu-central-1.saucelabs.com"
               f":443/wd/hub")

        driver = webdriver.Remote(command_executor=url, options=options, keep_alive=True)

        return driver
