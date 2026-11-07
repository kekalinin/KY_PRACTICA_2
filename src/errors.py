"""Модуль с пользовательскими исключениями."""


class ConfigError(Exception):
    """Исключение для ошибок конфигурации."""

    def __init__(self, message):
        """Инициализация исключения.

        Args:
            message: текст ошибки
        """
        super().__init__(message)
        self.message = message


class ValidationError(ConfigError):
    """Исключение для ошибок валидации параметров."""
    pass
