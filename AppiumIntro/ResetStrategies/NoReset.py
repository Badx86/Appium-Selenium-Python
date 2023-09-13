from appium import webdriver

# Do not stop app, do not clear app data, and do not unistall apk
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'
desired_caps['deviceName'] = 'MyEmulator'
desired_caps['app'] = ('D:\Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'com.google.android.apps.chrome.Main'
desired_caps['noReset'] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# No Reset (noReset): Этот флаг гарантирует, что приложение не будет сбрасываться перед началом новой сессии,
# сохраняя все данные и состояния. Это полезно, если вы хотите продолжить тестирование с того места, где остановились
# в предыдущей сессии.