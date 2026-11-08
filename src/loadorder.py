"""Модуль для вычисления порядка загрузки зависимостей."""


def _is_filtered(name, filter_str):
    """Проверить, попадает ли имя под фильтр."""
    return bool(filter_str and filter_str in name)


def _find_cycle(neighbor, path):
    """Найти цикл, если сосед уже в текущем пути."""
    if neighbor not in path:
        return None
    cycle_start = path.index(neighbor)
    return path[cycle_start:] + [neighbor]


def _add_unique_cycle(result, cycle):
    """Добавить цикл в результат, если его ещё нет."""
    if cycle not in result['cycles']:
        result['cycles'].append(cycle)


def _add_to_order(result, node, filter_str):
    """Добавить узел в порядок загрузки."""
    if _is_filtered(node, filter_str):
        return
    if node not in result['order']:
        result['order'].append(node)


def compute_load_order(graph, start_node, max_depth, filter_str):
    """Вычислить порядок загрузки зависимостей."""
    result = {'order': [], 'cycles': []}
    visited = {start_node}
    stack = [(start_node, 0, [start_node], False)]

    def _process_neighbor(node, neighbor, path, depth):
        """Обработать одного соседа при вычислении порядка."""
        if _is_filtered(neighbor, filter_str):
            return
        cycle = _find_cycle(neighbor, path)
        if cycle is not None:
            _add_unique_cycle(result, cycle)
            return
        if neighbor not in visited:
            visited.add(neighbor)
            stack.append(
                (neighbor, depth + 1, path + [neighbor], False)
            )

    def _process_node():
        """Обработать один узел из стека."""
        node, depth, path, processed = stack.pop()
        if processed:
            _add_to_order(result, node, filter_str)
            return
        if depth > max_depth or _is_filtered(node, filter_str):
            return
        stack.append((node, depth, path, True))
        for neighbor in graph.get_neighbors(node):
            _process_neighbor(node, neighbor, path, depth)

    while stack:
        _process_node()

    return result
