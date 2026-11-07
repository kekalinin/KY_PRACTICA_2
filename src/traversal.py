"""Модуль для обхода графа алгоритмом DFS без рекурсии."""

from src.graph import Graph


def dfs_traversal(graph, start_node, max_depth, filter_str):
    """Обход графа в глубину без рекурсии.

    Args:
        graph: объект графа
        start_node: начальный узел
        max_depth: максимальная глубина обхода
        filter_str: подстрока для фильтрации

    Returns:
        dict: словарь с результатами обхода
    """
    result = {
        'edges': [],
        'cycles': [],
        'filtered': []
    }

    stack = [(start_node, 0, [start_node])]
    visited = set()

    while stack:
        node, depth, path = stack.pop()

        if depth > max_depth:
            continue

        if filter_str and filter_str in node:
            result['filtered'].append(node)
            continue

        for neighbor in graph.get_neighbors(node):
            if filter_str and filter_str in neighbor:
                result['filtered'].append(neighbor)
                continue

            next_depth = depth + 1
            if next_depth > max_depth:
                continue

            edge = (node, neighbor)
            result['edges'].append(edge)

            if neighbor in path:
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                result['cycles'].append(cycle)
            elif neighbor not in visited:
                visited.add(neighbor)
                stack.append(
                    (neighbor, next_depth, path + [neighbor])
                )

    return result
