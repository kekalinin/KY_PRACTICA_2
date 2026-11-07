"""Точка входа в приложение."""

import sys

from src.cli import parse_args
from src.config import create_config
from src.errors import ConfigError


def main():
    """Главная функция приложения."""
    try:
        args = parse_args()
        config = create_config(args)
        config.print_config()
    except ConfigError as error:
        print(f"Ошибка: {error.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Неожиданная ошибка: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
