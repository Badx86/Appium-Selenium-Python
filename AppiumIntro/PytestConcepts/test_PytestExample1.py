"""
Установите pytest с помощью pip (pip3 install pytest)

Соглашения об именовании в PyTest
Имя файла должно начинаться с "test_PytestExample1.py"
Имя метода должно начинаться с "test_methodA"
######## 3 способа выполнения кода в pytest #############

py.test -v -s files_path # запустить все тесты в определенном files_path
py.test -v -s test_mod.py # запустить тесты в модуле или в тестовом файле
py.test -v -s test_module.py::test_method # запустить только test_method в test_module.py

-v : подробный режим (verbose - это аргумент, используемый для сообщения большего количества информации об операции в вашей программе)
-s : для вывода выражений
"""


def test_methodA():
    print("This is method A")


def test_methodB():
    print("This is method B")
