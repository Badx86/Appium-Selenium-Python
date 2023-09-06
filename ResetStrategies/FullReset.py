from appium import webdriver
import time
# Stop app, clear app data and unistall apk before session starts and after test
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
desired_caps['fullReset'] = True

time.sleep(5)

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)

driver.quit()

# Full Reset (fullReset): Эта стратегия полностью удалит приложение и заново его установит перед началом
# новой сессии тестирования. Это полезно, если вы хотите удостовериться,
# что тестируемое приложение стартует в исходном состоянии.