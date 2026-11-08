"""Точка входа в приложение."""

import sys

from src.cli import parse_args
from src.config import create_config
from src.errors import ConfigError
from src.graph import Graph
from src.loadorder import compute_load_order
from src.mermaid import generate_mermaid
from src.pypi_client import fetch_package_info
from src.render import render_mermaid_to_png
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


def _build_graph(config):
    """Построить граф на основе конфигурации.

    Args:
        config: объект конфигурации

    Returns:
        Graph: граф зависимостей
    """
    if config.is_test_mode:
        return parse_test_repo(config.repo)
    return build_pypi_graph(
        config.package,
        config.repo,
        config.max_depth,
        config.filter_str
    )


def _print_edges(edges):
    """Вывести список рёбер графа.

    Args:
        edges: список кортежей (источник, цель)
    """
    for edge in edges:
        print(f"  {edge[0]} -> {edge[1]}")


def _print_cycles(cycles, title):
    """Вывести список циклов с заголовком.

    Args:
        cycles: список циклов
        title: заголовок секции
    """
    if not cycles:
        return
    print(f"\n{title}:")
    for cycle in cycles:
        print(f"  {' -> '.join(cycle)}")


def _print_filtered(filtered):
    """Вывести список отфильтрованных пакетов.

    Args:
        filtered: список имён пакетов
    """
    if not filtered:
        return
    print("\nОтфильтрованы пакеты:")
    for pkg in filtered:
        print(f"  {pkg}")


def _print_order(order):
    """Вывести порядок загрузки зависимостей.

    Args:
        order: список имён пакетов в порядке загрузки
    """
    for index, package in enumerate(order, 1):
        print(f"  {index}. {package}")


def _generate_and_save(graph, start_node, max_depth, filter_str, output):
    """Сгенерировать Mermaid-диаграмму и сохранить в PNG.

    Args:
        graph: объект графа
        start_node: начальный узел
        max_depth: максимальная глубина
        filter_str: подстрока фильтра
        output: путь к выходному PNG-файлу
    """
    print("\nДиаграмма Mermaid:")
    mermaid_text = generate_mermaid(
        graph, start_node, max_depth, filter_str
    )
    print(mermaid_text)

    print(f"\nСохранение диаграммы в {output}...")
    render_mermaid_to_png(mermaid_text, output)


def _run_analysis(config, graph, start_node):
    """Выполнить анализ графа и вывести результаты.

    Обходит граф, вычисляет порядок загрузки,
    выводит рёбра, циклы и отфильтрованные пакеты.

    Args:
        config: объект конфигурации
        graph: объект графа
        start_node: начальный узел
    """
    print(f"\nГраф зависимостей '{start_node}':")
    traversal_result = dfs_traversal(
        graph, start_node, config.max_depth, config.filter_str
    )
    _print_edges(traversal_result['edges'])
    _print_cycles(traversal_result['cycles'], "Обнаружены циклы")
    _print_filtered(traversal_result['filtered'])

    print(f"\nПорядок загрузки зависимостей '{start_node}':")
    order_result = compute_load_order(
        graph, start_node, config.max_depth, config.filter_str
    )
    _print_order(order_result['order'])
    _print_cycles(
        order_result['cycles'],
        "Циклы (разорваны для сортировки)"
    )


def main():
    """Главная функция приложения."""
    try:
        args = parse_args()
        config = create_config(args)
        config.print_config()

        graph = _build_graph(config)
        start_node = config.package

        _run_analysis(config, graph, start_node)
        _generate_and_save(
            graph, start_node,
            config.max_depth, config.filter_str,
            config.output
        )

    except ConfigError as error:
        print(f"Ошибка: {error.message}", file=sys.stderr)
        sys.exit(1)
    except Exception as error:
        print(f"Неожиданная ошибка: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
