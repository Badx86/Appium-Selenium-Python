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
ele_id.click()

time.sleep(2)

ele_class = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_class.send_keys("TestExample")

submit_btn = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
submit_btn.click()

output_text_element = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv1")
actual_output_text = output_text_element.text

print(f"Output text: {actual_output_text}")

assert actual_output_text == "TestExample", f"Expected 'TestExample', but got '{actual_output_text}'"

driver.quit()