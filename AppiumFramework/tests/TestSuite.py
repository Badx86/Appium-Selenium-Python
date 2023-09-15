import unittest
from AppiumFramework.tests.LoginTest import LoginTest
from AppiumFramework.tests.ContactUsFormTest import ContactUsFormTest

# Создание объектов для загрузки тестов
cf = unittest.TestLoader().loadTestsFromTestCase(ContactUsFormTest)
lp = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# Объединение всех тестов в один пакет тестов для выполнения регрессионного тестирования
regressionTest = unittest.TestSuite([cf, lp])

# Запуск регрессионного набора тестов
unittest.TextTestRunner(verbosity=1).run(regressionTest)
