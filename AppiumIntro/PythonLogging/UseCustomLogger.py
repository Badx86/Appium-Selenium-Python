import AppiumIntro.PythonLogging.CustomLogger as cl


# Создаём класс CustomLoggerDemo для демонстрации пользовательского логирования
class CustomLoggerDemo():
    # Получаем объект логгера, используя пользовательскую функцию customLogger()
    log = cl.customLogger()

    # Метод, записывающий сообщения всех уровней с помощью объекта log
    def methodOne(self):
        self.log.critical('This is Critical msg')
        self.log.error('This is Error msg')
        self.log.warning('This is Warning msg')
        self.log.info('This is Info msg')
        self.log.debug('This is Debug msg')

    # Другой метод, также записывающий сообщения, но с использованием нового объекта логгера
    # def methodTwo(self):
    #     m2 = cl.customLogger()
    #     m2.critical('Critical msg')
    #     m2.error('Error msg')
    #     m2.warning('Warning msg')
    #     m2.info('Info msg')
    #     m2.debug('Debug msg')

    def methodTwo(self):
        self.log.critical('This is Critical msg - 2')
        self.log.error('This is Error msg - 2')
        self.log.warning('This is Warning msg - 2')
        self.log.info('This is Info msg - 2')
        self.log.debug('This is Debug msg - 2')


# Создаём объект класса CustomLoggerDemo и вызываем его методы для демонстрации логирования
cld = CustomLoggerDemo()
cld.methodOne()
cld.methodTwo()
