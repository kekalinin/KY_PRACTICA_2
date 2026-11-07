"""Точка входа в приложение."""

import sys

from src.cli import parse_args
from src.config import create_config
from src.errors import ConfigError
from src.graph import Graph
from src.pypi_client import fetch_package_info
from src.requires import parse_requires_dist
from src.testrepo import parse_test_repo
from src.traversal import dfs_traversal


def build_pypi_graph(package_name, repo_url, max_depth, filter_str):
    """Построить граф зависимостей из PyPI.

    Args:
        package_name: имя пакета
        repo_url: URL репозитория
        max_depth: максимальная глубина
        filter_str: подстрока фильтра

    Returns:
        Graph: граф зависимостей
    """
    graph = Graph()
    info = fetch_package_info(package_name, repo_url)
    requires_dist = info.get("info", {}).get("requires_dist")
    deps = parse_requires_dist(requires_dist)

    for dep in deps:
        if filter_str and filter_str in dep:
            continue
        graph.add_edge(package_name, dep)

    return graph


def main():
    """Главная функция приложения."""
    try:
        args = parse_args()
        config = create_config(args)
        config.print_config()

        if config.is_test_mode:
            graph = parse_test_repo(config.repo)
            start_node = config.package
        else:
            graph = build_pypi_graph(
                config.package,
                config.repo,
                config.max_depth,
                config.filter_str
            )
            start_node = config.package

        print(f"\nГраф зависимостей '{start_node}':")
        result = dfs_traversal(
            graph,
            start_node,
            config.max_depth,
            config.filter_str
        )

        for edge in result['edges']:
            print(f"  {edge[0]} -> {edge[1]}")

        if result['cycles']:
            print("\nОбнаружены циклы:")
            for cycle in result['cycles']:
                print(f"  {' -> '.join(cycle)}")

        if result['filtered']:
            print("\nОтфильтрованы пакеты:")
            for pkg in result['filtered']:
                print(f"  {pkg}")

    except ConfigError as error:
        print(f"Ошибка: {error.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Неожиданная ошибка: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
