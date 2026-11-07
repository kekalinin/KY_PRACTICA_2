"""Модуль с именованными константами проекта."""

# Значения по умолчанию
DEFAULT_MAX_DEPTH = 10
DEFAULT_FILTER = ""

# Ограничения валидации
MIN_DEPTH = 1
MAX_DEPTH = 100
MAX_PACKAGE_NAME_LENGTH = 100
MAX_FILTER_LENGTH = 50

# Расширения файлов
IMAGE_EXTENSION = ".png"

# Сообщения об ошибках
ERROR_EMPTY_PACKAGE = "Имя пакета не может быть пустым"
ERROR_INVALID_URL = "Некорректный URL репозитория"
ERROR_FILE_NOT_FOUND = "Файл тестового репозитория не найден"
ERROR_INVALID_OUTPUT = "Имя файла должно заканчиваться на .png"
ERROR_DEPTH_TOO_SMALL = "Глубина должна быть >= 1"
ERROR_DEPTH_TOO_LARGE = "Глубина должна быть <= 100"
ERROR_FILTER_TOO_LONG = "Фильтр слишком длинный"
