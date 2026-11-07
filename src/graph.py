"""Модуль для представления графа зависимостей."""


class Graph:
    """Класс ориентированного графа."""

    def __init__(self):
        """Инициализация пустого графа."""
        self.adjacency_list = {}

    def add_node(self, node):
        """Добавить узел в граф.

        Args:
            node: имя узла
        """
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, source, target):
        """Добавить ребро в граф.

        Args:
            source: узел-источник
            target: узел-назначение
        """
        self.add_node(source)
        self.add_node(target)
        self.adjacency_list[source].append(target)

    def get_neighbors(self, node):
        """Получить список соседей узла.

        Args:
            node: имя узла

        Returns:
            list: список соседних узлов
        """
        return self.adjacency_list.get(node, [])
