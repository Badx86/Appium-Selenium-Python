import time

from appium import webdriver

# Step 1: Create "Desired Capabilities"
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

# Step 2: Create "Driver object"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)

driver.start_activity("com.android.vending", "com.android.AssetBrowserActivity")

time.sleep(5)

driver.start_activity("com.skill2lead.appiumdemo", "com.skill2lead.appiumdemo.MainAvtivity")

time.sleep(5)

driver.quit()
