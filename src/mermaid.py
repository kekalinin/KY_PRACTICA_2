"""Модуль для генерации диаграммы на языке Mermaid."""


def generate_mermaid(graph, start_node, max_depth, filter_str):
    """Сформировать текстовое представление графа на языке Mermaid.

    Args:
        graph: объект графа
        start_node: начальный узел
        max_depth: максимальная глубина обхода
        filter_str: подстрока для фильтрации

    Returns:
        str: текст диаграммы Mermaid
    """
    from src.traversal import dfs_traversal

    result = dfs_traversal(graph, start_node, max_depth, filter_str)

    lines = ["graph TD"]

    for edge in result['edges']:
        source = _sanitize_id(edge[0])
        target = _sanitize_id(edge[1])
        lines.append(f"    {source} --> {target}")

    return "\n".join(lines)


def _sanitize_id(name):
    """Преобразовать имя пакета в безопасный идентификатор Mermaid.

    Mermaid не разрешает точки и дефисы в идентификаторах узлов,
    поэтому заменяем их на подчёркивания.

    Args:
        name: имя пакета

    Returns:
        str: безопасный идентификатор
    """
    return name.replace('.', '_').replace('-', '_')
