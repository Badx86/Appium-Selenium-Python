import pytest
from AppiumFramework.base.DriverClass import Driver
import pytest
import time


@pytest.fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(3)
    driver.quit()
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
