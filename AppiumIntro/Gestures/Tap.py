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

ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))

actions = TouchAction(driver)
# actions.tap(None, 700, 1990, 1)
actions.tap(ele)
actions.perform()

# input_email = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
# input_email.send_keys("example@email.com")
#
# submit_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("SUBMIT")')
# submit_btn.click()

time.sleep(2)

driver.quit()
