"""Тесты для модуля loadorder."""

import unittest

from src.graph import Graph
from src.loadorder import compute_load_order


class TestLoadOrder(unittest.TestCase):
    """Тесты порядка загрузки."""

    def test_linear_order(self):
        """Тест линейного графа A -> B -> C."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')

        result = compute_load_order(graph, 'A', 10, "")
        order = result['order']

        self.assertEqual(order[-1], 'A')
        self.assertLess(order.index('C'), order.index('B'))
        self.assertLess(order.index('B'), order.index('A'))

    def test_diamond_order(self):
        """Тест графа-ромба A -> B, A -> C, B -> D, C -> D."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('C', 'D')

        result = compute_load_order(graph, 'A', 10, "")
        order = result['order']

        self.assertEqual(order[-1], 'A')
        self.assertLess(order.index('D'), order.index('B'))
        self.assertLess(order.index('D'), order.index('C'))

    def test_cycle_handling(self):
        """Тест графа с циклом A -> B -> C -> A."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('C', 'A')

        result = compute_load_order(graph, 'A', 10, "")

        self.assertTrue(len(result['cycles']) > 0)
        self.assertIn('A', result['order'])

    def test_filter_applied(self):
        """Тест применения фильтра."""
        graph = Graph()
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')

        result = compute_load_order(graph, 'A', 10, "C")

        self.assertNotIn('C', result['order'])


if __name__ == "__main__":
    unittest.main()
