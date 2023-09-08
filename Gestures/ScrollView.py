from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
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
ele_id = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/ScrollView"))
ele_id.click()

ele_classname = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                           'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON12"))'))
ele_classname.click()

driver.quit()