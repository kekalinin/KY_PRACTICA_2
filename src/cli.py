"""Модуль для разбора аргументов командной строки."""

import argparse

from src import constants


def create_parser():
    """Создать парсер аргументов командной строки.

    Returns:
        argparse.ArgumentParser: настроенный парсер
    """
    parser = argparse.ArgumentParser(
        description="Визуализатор графа зависимостей pip"
    )

    parser.add_argument(
        "--package",
        required=True,
        help="Имя анализируемого пакета"
    )

    parser.add_argument(
        "--repo",
        required=True,
        help="URL репозитория или путь к тестовому файлу"
    )

    parser.add_argument(
        "--test-repo",
        action="store_true",
        default=False,
        help="Режим работы с тестовым репозиторием"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Имя файла с изображением графа"
    )

    parser.add_argument(
        "--max-depth",
        type=int,
        required=True,
        help="Максимальная глубина анализа"
    )

    parser.add_argument(
        "--filter",
        default=constants.DEFAULT_FILTER,
        help="Подстрока для фильтрации пакетов"
    )

    return parser


def parse_args(args=None):
    """Разобрать аргументы командной строки.

    Args:
        args: список аргументов (для тестирования)

    Returns:
        argparse.Namespace: разобранные аргументы
    """
    parser = create_parser()
    return parser.parse_args(args)
