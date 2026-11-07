"""Тесты для модуля cli."""

import unittest

from src.cli import parse_args


class TestCLI(unittest.TestCase):
    """Тесты разбора аргументов командной строки."""

    def test_valid_args(self):
        """Тест корректных аргументов."""
        args = parse_args([
            "--package", "requests",
            "--repo", "https://pypi.org/pypi/requests/json",
            "--output", "graph.png",
            "--max-depth", "5",
            "--filter", "test"
        ])

        self.assertEqual(args.package, "requests")
        self.assertEqual(
            args.repo,
            "https://pypi.org/pypi/requests/json"
        )
        self.assertFalse(args.test_repo)
        self.assertEqual(args.output, "graph.png")
        self.assertEqual(args.max_depth, 5)
        self.assertEqual(args.filter, "test")

    def test_test_repo_flag(self):
        """Тест флага тестового репозитория."""
        args = parse_args([
            "--package", "A",
            "--repo", "test.txt",
            "--test-repo",
            "--output", "graph.png",
            "--max-depth", "3"
        ])

        self.assertTrue(args.test_repo)

    def test_missing_package(self):
        """Тест отсутствия обязательного параметра."""
        with self.assertRaises(SystemExit):
            parse_args([
                "--repo", "https://pypi.org/pypi/requests/json",
                "--output", "graph.png",
                "--max-depth", "5"
            ])


if __name__ == "__main__":
    unittest.main()
