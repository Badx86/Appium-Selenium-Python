from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utils.CustomLogger as cl
from AppiumFramework.base.BasePage import BasePage

# Инициализация драйвера и логгера
driver1 = Driver()
log = cl.customLogger()
# Получение драйвера для работы с мобильным приложением
driver = driver1.getDriverMethod()
# Инициализация объекта BasePage для работы с элементами приложения
bp = BasePage(driver)
# Логгирование запуска приложения
log.info('Launch App')
# Делаем скриншот после запуска приложения
bp.screenShot('Launch App')
# Проверка наличия кнопки 'Contact Us' и вывод результата в консоль
contactUsBtn = bp.isDisplayed('com.code2lead.kwad:id/ContactUs', 'id')
print(contactUsBtn)
# Нажатие на кнопку 'Contact Us'
contactUsBtn = bp.clickElement('com.code2lead.kwad:id/ContactUs', 'id')
# Заполнение полей формы
inputName = bp.sendText('John Smith', 'com.code2lead.kwad:id/Et2')
inputEmail = bp.sendText('j.smith00@yahoo.com', 'com.code2lead.kwad:id/Et3')
inputAddress = bp.sendText('Linkoln street 8801', 'com.code2lead.kwad:id/Et6')
inputMobileNo = bp.sendText('8(800)555-35-35', 'com.code2lead.kwad:id/Et7')
# Нажатие на кнопку отправки формы
submitBtn = bp.clickElement('com.code2lead.kwad:id/Btn2', 'id')
# Сохранение скриншота после заполнения формы
bp.screenShot('Contact Us Form')
