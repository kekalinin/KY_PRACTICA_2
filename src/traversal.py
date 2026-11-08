"""Модуль для обхода графа алгоритмом DFS без рекурсии."""


def _is_filtered(name, filter_str):
    """Проверить, попадает ли имя под фильтр."""
    return bool(filter_str and filter_str in name)


def _find_cycle(neighbor, path):
    """Найти цикл, если сосед уже в текущем пути."""
    if neighbor not in path:
        return None
    cycle_start = path.index(neighbor)
    return path[cycle_start:] + [neighbor]


def _add_unique_edge(result, edge):
    """Добавить ребро в результат, если его ещё нет."""
    if edge not in result['edges']:
        result['edges'].append(edge)


def _add_unique_cycle(result, cycle):
    """Добавить цикл в результат, если его ещё нет."""
    if cycle not in result['cycles']:
        result['cycles'].append(cycle)


def _add_unique_filtered(result, name):
    """Добавить имя в отфильтрованные, если его ещё нет."""
    if name not in result['filtered']:
        result['filtered'].append(name)


def dfs_traversal(graph, start_node, max_depth, filter_str):
    """Обойти граф алгоритмом DFS без рекурсии."""
    result = {'edges': [], 'cycles': [], 'filtered': []}
    visited = {start_node}
    stack = [(start_node, 0, [start_node])]

    def _process_neighbor(node, neighbor, path, depth):
        """Обработать одного соседа узла."""
        if _is_filtered(neighbor, filter_str):
            _add_unique_filtered(result, neighbor)
            return
        if depth < max_depth:
            _add_unique_edge(result, (node, neighbor))
        cycle = _find_cycle(neighbor, path)
        if cycle is not None:
            _add_unique_cycle(result, cycle)
            return
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append((neighbor, depth + 1, path + [neighbor]))

    def _process_node():
        """Обработать один узел из стека."""
        node, depth, path = stack.pop()
        if depth > max_depth:
            return
        if _is_filtered(node, filter_str):
            _add_unique_filtered(result, node)
            return
        for neighbor in graph.get_neighbors(node):
            _process_neighbor(node, neighbor, path, depth)

    while stack:
        _process_node()

    return result
