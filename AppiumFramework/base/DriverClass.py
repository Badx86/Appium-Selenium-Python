from appium import webdriver


class Driver:
    """
    Класс Driver используется для управления драйвером Appium.
    """
    def getDriverMethod(self):
        """
        Этот метод инициализирует и возвращает драйвер Appium с заданными параметрами.

        :return: Возвращает объект драйвера Appium.
        """
        # Задаем необходимые параметры для драйвера Appium
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['platformVersion'] = '12'
        desired_caps['deviceName'] = 'MyEmulator'
        desired_caps['app'] = ('D:\Android_Demo_App.apk')
        desired_caps['appPackage'] = 'com.code2lead.kwad'
        desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

        # Инициализация драйвера Appium
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
