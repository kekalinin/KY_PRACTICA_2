"""Модуль для чтения тестового графа из файла."""

import re
from src.graph import Graph

VALID_NAME_REGEX = re.compile(r'^[A-Z]+$')


def parse_test_repo(file_path):
    """Построить граф из файла тестового репозитория.

    Формат файла:
    A: B C
    B: D

    Args:
        file_path: путь к файлу

    Returns:
        Graph: построенный граф
    """
    graph = Graph()
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if ':' not in line:
                continue

            source, targets_str = line.split(':', 1)
            source = source.strip()

            if not VALID_NAME_REGEX.match(source):
                continue

            targets = targets_str.split()
            valid_targets = [
                t.strip() for t in targets
                if VALID_NAME_REGEX.match(t.strip())
            ]

            if valid_targets:
                graph.add_node(source)
                for target in valid_targets:
                    graph.add_edge(source, target)

    return graph
