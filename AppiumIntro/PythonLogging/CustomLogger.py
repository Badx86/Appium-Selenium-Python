import inspect
import logging


def customLogger(logName=None):
    # Если имя журнала не указано, определите его на основе имени вызывающего метода или класса
    if logName is None:
        logName = inspect.stack()[1][3]

    # Удаляем нежелательные символы из имени файла лога
    logName = logName.replace('<', '').replace('>', '').replace('|', '')

    # Создаем объект логгера с определенным именем
    logger = logging.getLogger(logName)

    # Устанавливаем уровень логирования (в данном случае, DEBUG)
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик файла для сохранения журналов в файл с указанной кодировкой
    # fileHandler = logging.FileHandler('{0}.log'.format(logName), mode='a', encoding='utf-8')
    # fileHandler = logging.FileHandler('Logs.log'.format(logName), mode='a', encoding='utf-8')
    fileHandler = logging.FileHandler('../Reports/Logs.log'.format(logName), mode='a', encoding='utf-8')

    # Устанавливаем уровень логирования для обработчика файла (в данном случае, DEBUG)
    fileHandler.setLevel(logging.DEBUG)

    # Определяем формат сообщений в журнале
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # Применяем форматтер к обработчику файла
    fileHandler.setFormatter(formatter)

    # Проверка: если у логгера уже есть обработчики, не добавляем новый
    if not logger.handlers:
        logger.addHandler(fileHandler)

    # Возвращаем настроенный объект логгера
    return logger


# Пример использования
if __name__ == "__main__":
    # Создаем объект логгера с именем "myLog"
    logger = customLogger("myLog")

    # Записываем сообщения различных уровней в журнал
    logger.debug("Это сообщение уровня DEBUG")
    logger.info("Это сообщение уровня INFO")
