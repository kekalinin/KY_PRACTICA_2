"""Модуль для работы с конфигурацией."""

from dataclasses import dataclass

from src import validation


@dataclass
class Config:
    """Класс конфигурации приложения.

    Attributes:
        package: имя анализируемого пакета
        repo: URL репозитория или путь к файлу
        is_test_mode: флаг тестового режима
        output: имя файла с изображением
        max_depth: максимальная глубина анализа
        filter_str: подстрока для фильтрации
    """

    package: str
    repo: str
    is_test_mode: bool
    output: str
    max_depth: int
    filter_str: str

    def validate(self):
        """Проверить все параметры конфигурации.

        Raises:
            ValidationError: если параметры некорректны
        """
        validation.validate_all(
            self.package,
            self.repo,
            self.is_test_mode,
            self.output,
            self.max_depth,
            self.filter_str
        )

    def print_config(self):
        """Вывести параметры в формате ключ-значение."""
        print("Параметры конфигурации:")
        print(f"  package: {self.package}")
        print(f"  repo: {self.repo}")
        print(f"  test_mode: {self.is_test_mode}")
        print(f"  output: {self.output}")
        print(f"  max_depth: {self.max_depth}")
        print(f"  filter: {self.filter_str}")


def create_config(args):
    """Создать конфигурацию из аргументов.

    Args:
        args: разобранные аргументы командной строки

    Returns:
        Config: объект конфигурации
    """
    config = Config(
        package=args.package,
        repo=args.repo,
        is_test_mode=args.test_repo,
        output=args.output,
        max_depth=args.max_depth,
        filter_str=args.filter
    )
    config.validate()
    return config
