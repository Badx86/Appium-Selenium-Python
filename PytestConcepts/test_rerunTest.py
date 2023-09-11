import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time


@pytest.mark.flaky(reruns=5)
def test_runAppiumTest():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UIAutomator2'
    desired_caps['platformVersion'] = '12'
    desired_caps['deviceName'] = 'MyEmulator'
    desired_caps['app'] = ('D:\Android_Demo_App.apk')
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValu")
    ele_id.click()

    time.sleep(5)

    driver.quit()
