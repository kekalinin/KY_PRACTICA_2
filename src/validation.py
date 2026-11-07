"""Модуль для валидации параметров конфигурации."""

import os
from urllib.parse import urlparse

from src import constants
from src.errors import ValidationError


def validate_package(package):
    """Проверить имя пакета.

    Args:
        package: имя пакета

    Raises:
        ValidationError: если имя некорректно
    """
    if not package or not package.strip():
        raise ValidationError(constants.ERROR_EMPTY_PACKAGE)

    if len(package) > constants.MAX_PACKAGE_NAME_LENGTH:
        raise ValidationError(
            f"Имя пакета слишком длинное "
            f"(максимум {constants.MAX_PACKAGE_NAME_LENGTH})"
        )


def validate_repo(repo, is_test_mode):
    """Проверить источник данных.

    Args:
        repo: URL или путь к файлу
        is_test_mode: флаг тестового режима

    Raises:
        ValidationError: если источник некорректен
    """
    if is_test_mode:
        if not os.path.isfile(repo):
            raise ValidationError(constants.ERROR_FILE_NOT_FOUND)
    else:
        parsed = urlparse(repo)
        if not parsed.scheme or not parsed.netloc:
            raise ValidationError(constants.ERROR_INVALID_URL)


def validate_output(output):
    """Проверить имя выходного файла.

    Args:
        output: имя файла

    Raises:
        ValidationError: если имя некорректно
    """
    if not output.endswith(constants.IMAGE_EXTENSION):
        raise ValidationError(constants.ERROR_INVALID_OUTPUT)


def validate_depth(depth):
    """Проверить максимальную глубину.

    Args:
        depth: значение глубины

    Raises:
        ValidationError: если глубина некорректна
    """
    if depth < constants.MIN_DEPTH:
        raise ValidationError(constants.ERROR_DEPTH_TOO_SMALL)

    if depth > constants.MAX_DEPTH:
        raise ValidationError(constants.ERROR_DEPTH_TOO_LARGE)


def validate_filter(filter_str):
    """Проверить подстроку фильтра.

    Args:
        filter_str: подстрока для фильтрации

    Raises:
        ValidationError: если фильтр некорректен
    """
    if filter_str and len(filter_str) > constants.MAX_FILTER_LENGTH:
        raise ValidationError(
            f"{constants.ERROR_FILTER_TOO_LONG} "
            f"(максимум {constants.MAX_FILTER_LENGTH})"
        )


def validate_all(package, repo, is_test_mode, output, depth, filter_str):
    """Проверить все параметры.

    Args:
        package: имя пакета
        repo: URL или путь к файлу
        is_test_mode: флаг тестового режима
        output: имя выходного файла
        depth: максимальная глубина
        filter_str: подстрока фильтра

    Raises:
        ValidationError: если какой-то параметр некорректен
    """
    validate_package(package)
    validate_repo(repo, is_test_mode)
    validate_output(output)
    validate_depth(depth)
    validate_filter(filter_str)
