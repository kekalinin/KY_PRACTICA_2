"""Парсер строк Requires-Dist из метаданных PyPI."""

import re

PACKAGE_NAME_REGEX = re.compile(r'^([A-Za-z0-9_.-]+)')
EXTRA_REGEX = re.compile(r'extra\s*==')


def parse_requires_dist(requires_dist_list):
    """Извлечь имена прямых зависимостей.

    Args:
        requires_dist_list: список строк Requires-Dist

    Returns:
        list: список имен пакетов-зависимостей
    """
    dependencies = []
    if not requires_dist_list:
        return dependencies

    for req_str in requires_dist_list:
        if not req_str:
            continue

        if EXTRA_REGEX.search(req_str):
            continue

        match = PACKAGE_NAME_REGEX.match(req_str)
        if match:
            dependencies.append(match.group(1))

    return dependencies
