from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options as ChromeOptions
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

options = ChromeOptions()
# options.browser_version = '116'
# options.platform_name = 'Windows 10'
options.browser_version = 'latest'
options.platform_name = 'macOS 13'
sauce_options = {}
sauce_options['username'] = config['sauce']['username']
sauce_options['accessKey'] = config['sauce']['access_key']
sauce_options['build'] = 'TestBuild'
sauce_options['name'] = 'SauceLabTest1 in Mac'
# sauce_options['screenResolution'] = '1280x1024'
sauce_options['screenResolution'] = '1440x900'
options.set_capability('sauce:options', sauce_options)

url = f"https://{sauce_options['username']}:{sauce_options['accessKey']}@ondemand.eu-central-1.saucelabs.com:443/wd/hub"

driver = webdriver.Remote(command_executor=url, options=options, keep_alive=True)

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID, "user_input")))
ele.send_keys("Code2Lead")

time.sleep(2)
driver.quit()
