import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# Step 1: Create "Desired Capabilities"
def deviceDriver(deviceId, systemPort):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UIAutomator2'
    desired_caps['platformVersion'] = '12'
    desired_caps['deviceName'] = 'MyEmulator'
    desired_caps['udid'] = deviceId
    desired_caps['systemPort'] = systemPort
    desired_caps['app'] = ('D:\Android_Demo_App.apk')
    desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
    desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'
    # Step 2: Create "Driver object"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver


def enterText(driver):
    # Step 3: Click on the button using ID locator value
    ele_id = driver.find_element(AppiumBy.ID, "com.skill2lead.appiumdemo:id/EnterValue")
    ele_id.click()

    time.sleep(2)
    # Step 4: Enter the text
    ele_class = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    ele_class.click()
    ele_class.send_keys("TestExample")

    time.sleep(2)
    # Step 5: Close driver object
    driver.quit()


def test_deviceTest():
    device1 = deviceDriver('deviceName', 8200)
    device2 = deviceDriver('emulator-5554', 8201)

    enterText(device1)
    enterText(device2)