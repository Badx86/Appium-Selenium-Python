import pytest


@pytest.fixture(scope='module')
def beforeClass():
    print("Before the Class")
    yield
    print("After the Class")


@pytest.fixture()
def beforeMethod():
    print("Before the Method")
    yield
    print("After the Method")


def test_methodA(beforeClass, beforeMethod):
    print("This is method A")


def test_methodB(beforeClass, beforeMethod):
    print("This is method B")

