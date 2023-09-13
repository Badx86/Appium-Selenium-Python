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

drag_n_drop_btn = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                             'new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))'))
drag_n_drop_btn.click()

ele_pict = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ingvw"))

ele_lay = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/layout2"))

actions = TouchAction(driver)

actions.long_press(ele_pict).move_to(ele_lay).release().perform()

time.sleep(4)
driver.quit()