"""Модуль констант для валидации и конфигурации приложения."""

DEFAULT_MAX_DEPTH = 10
MIN_DEPTH = 1
MAX_DEPTH = 100
MAX_PACKAGE_NAME_LENGTH = 100
MAX_FILTER_LENGTH = 50
IMAGE_EXTENSION = ".png"
ERROR_EMPTY_PACKAGE = "Имя пакета не может быть пустым"
ERROR_PACKAGE_TOO_LONG = "Имя пакета слишком длинное"
ERROR_INVALID_URL = "Некорректный URL репозитория"
ERROR_FILE_NOT_FOUND = "Тестовый файл не найден"
ERROR_INVALID_OUTPUT = "Выходной файл должен иметь расширение .png"
ERROR_DEPTH_TOO_SMALL = "Глубина должна быть не меньше 1"
ERROR_DEPTH_TOO_LARGE = "Глубина должна быть не больше 100"
ERROR_FILTER_TOO_LONG = "Фильтр слишком длинный"
