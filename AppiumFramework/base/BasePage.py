from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from allure_commons.types import AttachmentType
import AppiumFramework.utils.CustomLogger as cl
import allure
import time


class BasePage:
    """
    Базовый класс для работы с элементами на мобильной странице.
    """
    log = cl.customLogger()

    def __init__(self, driver):
        """
        Инициализация драйвера.

        :param driver: Драйвер для управления мобильным приложением.
        """
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        """
        Ожидание появления элемента на мобильной странице.

        :param locatorValue: Значение локатора элемента.
        :param locatorType: Тип локатора (id, class, desc, index, text, xpath).
        :return: Возвращает найденный элемент или None.
        """
        # Преобразование типа локатора к нижнему регистру для унификации
        locatorType = locatorType.lower()
        element = None

        # Настройка явного ожидания с игнорированием определенных исключений
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=
        [ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

        # Поиск элемента в зависимости от типа локатора
        # Добавлены комментарии для каждого типа локатора для лучшего понимания
        if locatorType == 'id':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == 'class':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == 'desc':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("%s")' % locatorValue))
            return element
        elif locatorType == 'index':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().index(%d)' % int(locatorValue)))
            return element
        elif locatorType == 'text':
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("%s")' % locatorValue))
            return element
        elif locatorType == 'xpath':
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locatorValue))
            return element
        else:
            self.log.info('Locator value ' + locatorValue + ' not found')

        return element

    def getElement(self, locatorValue, locatorType='id'):
        """
        Получение элемента.

        :param locatorValue: Значение локатора элемента.
        :param locatorType: Тип локатора (по умолчанию 'id').
        :return: Возвращает найденный элемент или None.
        """
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info(
                'Element found with LocatorType: ' + locatorType + ' and LocatorValue: ' + locatorValue)
        except:
            self.log.info(
                'Element not found with LocatorType: ' + locatorType + ' and LocatorValue: ' + locatorValue)

        return element

    def clickElement(self, locatorValue, locatorType='id'):
        """
        Клик по элементу.

        :param locatorValue: Значение локатора элемента.
        :param locatorType: Тип локатора (по умолчанию 'id').
        """
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info('Clicked on Element with LocatorType: ' + locatorType +
                          ' and LocatorValue: ' + locatorValue)
        except:
            self.log.info('Unable to click on Element with LocatorType: ' + locatorType +
                          ' and LocatorValue: ' + locatorValue)

    def sendText(self, text, locatorValue, locatorType='id'):
        """
        Ввод текста в элемент.

        :param text: Текст для ввода.
        :param locatorValue: Значение локатора элемента.
        :param locatorType: Тип локатора (по умолчанию 'id').
        """
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info('Send text on Element with LocatorType: ' + locatorType +
                          ' and LocatorValue: ' + locatorValue)
        except:
            self.log.info('Unable to send text on Element with LocatorType: ' + locatorType +
                          ' and LocatorValue: ' + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def isDisplayed(self, locatorValue, locatorType='id'):
        """
        Проверка, отображается ли элемент.

        :param locatorValue: Значение локатора элемента.
        :param locatorType: Тип локатора (по умолчанию 'id').
        :return: Возвращает True, если элемент отображается, иначе False.
        """
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info('Element with LocatorType: ' + locatorType +
                          ' and LocatorValue: ' + locatorValue + ' is displayed')
            return True
        except:
            self.log.info('Element with LocatorType: ' + locatorType +
                          ' and LocatorValue: ' + locatorValue + ' is not displayed')
            self.takeScreenshot(locatorType)
            return False

    def screenShot(self, screenshotName):
        """
        Создание скриншота.

        :param screenshotName: Имя файла для сохранения скриншота.
        """
        fileName = screenshotName + '_' + (time.strftime("%d_%m_%y_%H_%M_%S")) + '.png'
        screenshotDirectory = '../screenshots/'
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info('Save Screenshot to the Path: ' + screenshotPath)
        except:
            self.log.info('Unable to save Screenshot to the Path: ' + screenshotPath)

    def takeScreenshot(self, text):
        """
        Добавление скриншота в отчет Allure.

        :param text: Имя или описание скриншота, который будет отображаться в отчете Allure.
        """
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        """
        Симуляция нажатия клавиш на устройстве.

        :param value: Код клавиши, который нужно нажать.
        """
        self.driver.press_keycode(value)
