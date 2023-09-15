from AppiumFramework.base.DriverClass import Driver
import pytest
import time


@pytest.fixture(scope='class')
def setup_driver(request):
    """
    Инициализация и завершение работы драйвера перед и после тестов в классе.
    """
    print('Initializing driver...')
    driver_instance = Driver()
    driver = driver_instance.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(3)
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
