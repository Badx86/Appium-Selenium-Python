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

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the button: ", ele_id.text)
print("Text on the button: ", ele_id.get_attribute("text"))
print("Content description of the button: ", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("TestExample")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("TestExample")

driver.quit()
