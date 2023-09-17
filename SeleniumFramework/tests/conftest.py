import pytest
from SeleniumFramework.base.BasePage import BasePage
from SeleniumFramework.base.DriverClass import WebDriverClass


@pytest.fixture(scope='class')
def setup_driver(request):
    """
    Инициализация и завершение работы драйвера перед и после тестов в классе.
    """
    print('Initializing driver...')
    driver_instance = WebDriverClass()
    driver = driver_instance.getWebDriver('Chrome')
    bp = BasePage(driver)
    bp.launchWebPage('http://www.dummypoint.com/', 'General Dashboard — DummyPoint')
    if request.cls is not None:
        request.cls.driver = driver
    yield driver

    driver.quit()
    print('Driver closed.')


@pytest.fixture()
def setup_method():
    """
    Выполнение настроек перед и после каждого тестового метода.
    """
    print('Pre-method setup.')
    yield
    print('Post-method teardown.')