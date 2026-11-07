"""Тесты для модуля traversal."""

import unittest

from src.graph import Graph
from src.traversal import dfs_traversal


class TestTraversal(unittest.TestCase):
    """Тесты обхода графа."""

    def setUp(self):
        """Подготовка тестового графа."""
        self.graph = Graph()
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'D')
        self.graph.add_edge('C', 'D')

    def test_basic_traversal(self):
        """Тест базового обхода."""
        result = dfs_traversal(self.graph, 'A', 10, "")
        edges = result['edges']

        self.assertIn(('A', 'B'), edges)
        self.assertIn(('A', 'C'), edges)
        self.assertIn(('B', 'D'), edges)
        self.assertIn(('C', 'D'), edges)

    def test_depth_limit(self):
        """Тест ограничения глубины."""
        result = dfs_traversal(self.graph, 'A', 1, "")
        edges = result['edges']

        self.assertIn(('A', 'B'), edges)
        self.assertIn(('A', 'C'), edges)
        self.assertNotIn(('B', 'D'), edges)

    def test_filter(self):
        """Тест фильтрации узлов."""
        result = dfs_traversal(self.graph, 'A', 10, "D")
        filtered = result['filtered']

        self.assertIn('D', filtered)

    def test_cycle_detection(self):
        """Тест обнаружения цикла."""
        graph = Graph()
        graph.add_edge('X', 'Y')
        graph.add_edge('Y', 'Z')
        graph.add_edge('Z', 'X')

        result = dfs_traversal(graph, 'X', 10, "")
        self.assertTrue(len(result['cycles']) > 0)


if __name__ == "__main__":
    unittest.main()
