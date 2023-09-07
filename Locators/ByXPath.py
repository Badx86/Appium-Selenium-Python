import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
# 1.By using xpath and content description
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]')
# 2.By using xpath and Resource-Id
# ele_xpath = driver.find_element(AppiumBy.XPATH,
#                                 '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]')
# 3.By using xpath and Index value
scroll_view = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[3]')
scroll_view.click()

time.sleep(1)

button5 = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("BUTTON5")')
button5.click()

time.sleep(1)

alert_popup_message = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Alert popup")')
actual_output_text = alert_popup_message.text

print(f"Output text: {actual_output_text}")

assert actual_output_text == "Alert popup", f"Alert popup', but got '{actual_output_text}'"

# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Btn1"]')
# ele_xpath.click()
#
# time.sleep(2)
#
# ele_xpath2 = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
# ele_xpath2.send_keys("Skill2lead.com")
#
# time.sleep(2)

driver.quit()