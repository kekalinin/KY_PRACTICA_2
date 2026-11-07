"""Точка входа в приложение."""

import sys

from src.cli import parse_args
from src.config import create_config
from src.errors import ConfigError
from src.pypi_client import fetch_package_info
from src.requires import parse_requires_dist


def main():
    """Главная функция приложения."""
    try:
        args = parse_args()
        config = create_config(args)
        config.print_config()

        if not config.is_test_mode:
            info = fetch_package_info(config.package, config.repo)
            requires_dist = info.get("info", {}).get("requires_dist")
            deps = parse_requires_dist(requires_dist)

            print(f"\nПрямые зависимости '{config.package}':")
            if deps:
                for dep in deps:
                    print(f"  - {dep}")
            else:
                print("  Зависимости не найдены")

    except ConfigError as error:
        print(f"Ошибка: {error.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Неожиданная ошибка: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
