"""Модуль для вычисления порядка загрузки зависимостей."""

from src.graph import Graph


def compute_load_order(graph, start_node, max_depth, filter_str):
    """Вычислить порядок загрузки зависимостей.

    Использует постобход DFS без рекурсии. Сначала в результат
    попадают пакеты-листья, затем их родители, в конце — сам
    start_node. При обнаружении цикла ребро, ведущее к узлу
    текущего пути, игнорируется (цикл разрывается).

    Args:
        graph: объект графа
        start_node: начальный узел
        max_depth: максимальная глубина обхода
        filter_str: подстрока для фильтрации

    Returns:
        dict: словарь с ключами 'order' и 'cycles'
    """
    result = {
        'order': [],
        'cycles': []
    }

    stack = [(start_node, 0, [start_node], False)]
    visited = set()

    while stack:
        node, depth, path, processed = stack.pop()

        if processed:
            if filter_str and filter_str in node:
                continue
            if node not in result['order']:
                result['order'].append(node)
            continue

        if depth > max_depth:
            continue

        if filter_str and filter_str in node:
            continue

        stack.append((node, depth, path, True))

        for neighbor in graph.get_neighbors(node):
            if filter_str and filter_str in neighbor:
                continue

            if neighbor in path:
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                if cycle not in result['cycles']:
                    result['cycles'].append(cycle)
                continue

            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(
                    (neighbor, depth + 1, path + [neighbor], False)
                )

    return result
