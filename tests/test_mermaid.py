"""Тесты для модуля mermaid."""

import unittest

from src.graph import Graph
from src.mermaid import generate_mermaid


class TestMermaid(unittest.TestCase):
    """Тесты генерации Mermaid-диаграммы."""

    def test_simple_graph(self):
        """Тест простого графа."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')

        result = generate_mermaid(graph, 'A', 10, "")

        self.assertIn("graph TD", result)
        self.assertIn("A --> B", result)
        self.assertIn("B --> C", result)

    def test_sanitize_id(self):
        """Тест безопасных идентификаторов."""
        graph = Graph()
        graph.add_edge('pkg.name', 'pkg-name')

        result = generate_mermaid(graph, 'pkg.name', 10, "")

        self.assertIn("pkg_name --> pkg_name", result)

    def test_filter_applied(self):
        """Тест применения фильтра."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')

        result = generate_mermaid(graph, 'A', 10, "C")

        self.assertNotIn("B --> C", result)


if __name__ == "__main__":
    unittest.main()
