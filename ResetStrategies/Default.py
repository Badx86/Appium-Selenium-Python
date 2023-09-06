from appium import webdriver
import time
# Stop and clear app data after test. Do not unistall apk
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(5)

driver.quit()

# Default: По умолчанию Appium не будет переустанавливать приложение, если оно уже установлено на устройстве или
# эмуляторе. Это означает, что состояние приложения будет сохранено между сессиями.