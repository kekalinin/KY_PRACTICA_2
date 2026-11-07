"""Тесты для модуля testrepo."""

import os
import tempfile
import unittest

from src.testrepo import parse_test_repo


class TestTestRepo(unittest.TestCase):
    """Тесты парсера тестового репозитория."""

    def test_parse_simple(self):
        """Тест парсинга простого графа."""
        content = "A: B\nB: C\nC:\n"

        with tempfile.NamedTemporaryFile(
                mode='w', delete=False, suffix='.txt'
        ) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            graph = parse_test_repo(tmp_path)
            neighbors = graph.get_neighbors('A')
            self.assertIn('B', neighbors)
        finally:
            os.unlink(tmp_path)

    def test_ignore_invalid_names(self):
        """Тест игнорирования некорректных имен."""
        content = "a: B\nB: c\n"

        with tempfile.NamedTemporaryFile(
                mode='w', delete=False, suffix='.txt'
        ) as tmp:
            tmp.write(content)
            tmp_path = tmp.name

        try:
            graph = parse_test_repo(tmp_path)
            self.assertEqual(len(graph.adjacency_list), 0)
        finally:
            os.unlink(tmp_path)


if __name__ == "__main__":
    unittest.main()
