"""Модуль для разбора аргументов командной строки."""

import argparse

from src.constants import DEFAULT_MAX_DEPTH


def _add_package_arg(parser):
    """Добавить аргумент --package."""
    parser.add_argument(
        '--package',
        required=True,
        help='имя анализируемого пакета'
    )


def _add_repo_args(parser):
    """Добавить аргументы --repo и --test-repo."""
    parser.add_argument(
        '--repo',
        required=True,
        help='URL репозитория или путь к тестовому файлу'
    )
    parser.add_argument(
        '--test-repo',
        action='store_true',
        help='включить режим тестового репозитория'
    )


def _add_output_args(parser):
    """Добавить аргумент --output."""
    parser.add_argument(
        '--output',
        required=True,
        help='имя файла с изображением графа'
    )


def _add_analysis_args(parser):
    """Добавить аргументы --max-depth и --filter."""
    parser.add_argument(
        '--max-depth',
        type=int,
        default=DEFAULT_MAX_DEPTH,
        help='максимальная глубина анализа'
    )
    parser.add_argument(
        '--filter',
        default='',
        help='подстрока для фильтрации пакетов'
    )


def create_parser():
    """Создать парсер аргументов командной строки.

    Returns:
        argparse.ArgumentParser: настроенный парсер
    """
    parser = argparse.ArgumentParser(
        description='CLI-инструмент визуализации графа зависимостей'
    )
    _add_package_arg(parser)
    _add_repo_args(parser)
    _add_output_args(parser)
    _add_analysis_args(parser)
    return parser


def parse_args(args=None):
    """Разобрать аргументы командной строки.

    Args:
        args: список аргументов (для тестов). По умолчанию sys.argv.

    Returns:
        argparse.Namespace: разобранные аргументы
    """
    parser = create_parser()
    return parser.parse_args(args)
