import inspect
import logging
import allure


def customLogger():
    """
    Функция для создания настроенного объекта логгера.

    :return: Возвращает объект логгера с заданными параметрами.
    """
    # Получаем имя класса/метода, откуда вызван customLogger
    logName = inspect.stack()[1][3]

    # Создаем объект логгера с полученным именем
    logger = logging.getLogger(logName)

    # Устанавливаем уровень логирования
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик файла для сохранения логов
    fileHandler = logging.FileHandler("../reports/Code2Lead.log", mode='a')

    # Устанавливаем уровень логирования для обработчика файла
    fileHandler.setLevel(logging.DEBUG)

    # Создаем форматтер для задания формата сохраняемых логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # Применяем форматтер к обработчику файла
    fileHandler.setFormatter(formatter)

    # Добавляем обработчик файла к логгеру
    logger.addHandler(fileHandler)

    return logger


def allureLogs(text):
    """
    Функция для логирования шагов в отчетах Allure.

    :param text: Текст, который будет добавлен в отчет Allure.
    """
    with allure.step(text):
        pass
