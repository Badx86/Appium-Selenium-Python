import pytest


@pytest.fixture(scope='module')
def beforeClass():
    print('Before Class')
    yield
    print('After Class')


@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
