import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=
                    [ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

tab_activity = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                          'new UiScrollable(new UiSelector()).scrollIntoView(text("TAB ACTIVITY"))'))
tab_activity.click()

print("Device Width and Height: ", driver.get_window_size())
diviceSize = driver.get_window_size()
screenWidth = diviceSize['width']
screenHeight = diviceSize['height']

"""Right to Left"""
startx = screenWidth*8/9
endx = screenWidth/9
starty = screenHeight/2
endy = screenHeight/2

"""Left to Right"""
startx2 = screenWidth/9
endx2 = screenWidth*8/9
starty2 = screenHeight/2
endy2 = screenHeight/2

actions = TouchAction(driver)
actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()
time.sleep(2)
actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()

driver.quit()
