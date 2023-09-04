from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

# Step 1 : Import Appium Service class
from appium.webdriver.appium_service import AppiumService

# Step 2 : Create object for Appium Service class
appium_service = AppiumService()

# Step 3 : Call Start method by using Appium Service class object
appium_service.start()

# Step 4 : Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()

time.sleep(5)
driver.quit()

# Step 5 : Call stop method by using Appium Service class object
appium_service.stop()