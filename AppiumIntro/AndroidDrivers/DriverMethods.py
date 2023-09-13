from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UIAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

print("Check if device is locked or not: ", driver.is_locked())
print("Current Package: ", driver.current_package)
print("Current Activity: ", driver.current_activity)
print("Current Context: ", driver.current_context)
print("Current Orientation: ", driver.orientation)
