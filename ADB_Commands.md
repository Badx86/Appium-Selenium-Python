## Android Debug Bridge(ADB) Команды

### Основные команды
- `adb devices` : Список подключенных устройств
- `adb shell` : Открыть командную строку на устройстве

### Установка и удаление приложений
- `adb install <.apk>` : Установить APK на устройство
- `adb uninstall <package_name>` : Удалить приложение

### Копирование файлов
- `adb push <local> <remote>` : Копировать файлы на устройство
- `adb pull <remote> <local>` : Копировать файлы с устройства

### Управление питанием и перезагрузка
- `adb reboot` : Перезагрузить устройство
- `adb reboot-bootloader` : Перезагрузить в режим загрузчика
- `adb reboot recovery` : Перезагрузить в режим восстановления

### События ввода
- `adb shell input tap <x> <y>` : Симулировать касание по координатам
- `adb shell input swipe <x1> <y1> <x2> <y2>` : Симулировать свайп
- `adb shell input keyevent <key_code>` : Симулировать нажатие клавиши

### Скриншоты и запись экрана
- `adb shell screencap -p /sdcard/screenshot.png` : Сделать скриншот
- `adb shell screenrecord /sdcard/record.mp4` : Записать экран

### Логи и отладка
- `adb logcat` : Просмотр логов
- `adb bugreport` : Создать отчет об ошибках

### Другие полезные команды
- `adb get-serialno` : Получить серийный номер устройства
- `adb get-state` : Получить текущее состояние устройства
- `adb shell pm list packages` : Список установленных пакетов
- `adb shell dumpsys` : Информация о состоянии системы
- `adb shell am start -n <package_name>/<activity_name>` : Запуск активности
- `adb shell am force-stop <package_name>` : Остановка приложения


#### Keyevent Codes
С помощью команды `adb shell input keyevent` можно отправить либо код события, либо строку на устройство. Возможные значения для `event_code`:

| Код  | Описание            | Код  | Описание             | Код  | Описание                 |
|------|---------------------|------|----------------------|------|--------------------------|
| 0    | "KEYCODE_UNKNOWN"   | 29   | "KEYCODE_A"          | 58   | "KEYCODE_ALT_RIGHT"      |
| 1    | "KEYCODE_MENU"      | 30   | "KEYCODE_B"          | 59   | "KEYCODE_SHIFT_LEFT"     |
| 2    | "KEYCODE_SOFT_RIGHT"| 31   | "KEYCODE_C"          | 60   | "KEYCODE_SHIFT_RIGHT"    |
| 3    | "KEYCODE_HOME"      | 32   | "KEYCODE_D"          | 61   | "KEYCODE_TAB"            |
| 4    | "KEYCODE_BACK"      | 33   | "KEYCODE_E"          | 62   | "KEYCODE_SPACE"          |
| 5    | "KEYCODE_CALL"      | 34   | "KEYCODE_F"          | 63   | "KEYCODE_SYM"            |
| 6    | "KEYCODE_ENDCALL"   | 35   | "KEYCODE_G"          | 64   | "KEYCODE_EXPLORER"       |
| 7    | "KEYCODE_0"         | 36   | "KEYCODE_H"          | 65   | "KEYCODE_ENVELOPE"       |
| 8    | "KEYCODE_1"         | 37   | "KEYCODE_I"          | 66   | "KEYCODE_ENTER"          |
| 9    | "KEYCODE_2"         | 38   | "KEYCODE_J"          | 67   | "KEYCODE_DEL"            |
| 10   | "KEYCODE_3"         | 39   | "KEYCODE_K"          | 68   | "KEYCODE_GRAVE"          |
| 11   | "KEYCODE_4"         | 40   | "KEYCODE_L"          | 69   | "KEYCODE_MINUS"          |
| 12   | "KEYCODE_5"         | 41   | "KEYCODE_M"          | 70   | "KEYCODE_EQUALS"         |
| 13   | "KEYCODE_6"         | 42   | "KEYCODE_N"          | 71   | "KEYCODE_LEFT_BRACKET"   |
| 14   | "KEYCODE_7"         | 43   | "KEYCODE_O"          | 72   | "KEYCODE_RIGHT_BRACKET"  |
| 15   | "KEYCODE_8"         | 44   | "KEYCODE_P"          | 73   | "KEYCODE_BACKSLASH"      |
| 16   | "KEYCODE_9"         | 45   | "KEYCODE_Q"          | 74   | "KEYCODE_SEMICOLON"      |
| 17   | "KEYCODE_STAR"      | 46   | "KEYCODE_R"          | 75   | "KEYCODE_APOSTROPHE"     |
| 18   | "KEYCODE_POUND"     | 47   | "KEYCODE_S"          | 76   | "KEYCODE_SLASH"          |
| 19   | "KEYCODE_DPAD_UP"   | 48   | "KEYCODE_T"          | 77   | "KEYCODE_AT"             |
| 20   | "KEYCODE_DPAD_DOWN" | 49   | "KEYCODE_U"          | 78   | "KEYCODE_NUM"            |
| 21   | "KEYCODE_DPAD_LEFT" | 50   | "KEYCODE_V"          | 79   | "KEYCODE_HEADSETHOOK"    |
| 22   | "KEYCODE_DPAD_RIGHT"| 51   | "KEYCODE_W"          | 80   | "KEYCODE_FOCUS"          |
| 23   | "KEYCODE_DPAD_CENTER"|52   | "KEYCODE_X"          | 81   | "KEYCODE_PLUS"           |
| 24   | "KEYCODE_VOLUME_UP" | 53   | "KEYCODE_Y"          | 82   | "KEYCODE_MENU"           |
| 25   | "KEYCODE_VOLUME_DOWN"|54   | "KEYCODE_Z"          | 83   | "KEYCODE_NOTIFICATION"   |
| 26   | "KEYCODE_POWER"     | 55   | "KEYCODE_COMMA"      | 84   | "KEYCODE_SEARCH"         |
| 27   | "KEYCODE_CAMERA"    | 56   | "KEYCODE_PERIOD"     | 85   | "TAG_LAST_KEYCODE"       |
| 28   | "KEYCODE_CLEAR"     | 57   | "KEYCODE_ALT_LEFT"   |      |                          |
