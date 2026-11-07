"""Тесты для модуля requires."""

import unittest

from src.requires import parse_requires_dist


class TestRequires(unittest.TestCase):
    """Тесты парсера зависимостей."""

    def test_empty_list(self):
        """Тест пустого списка."""
        self.assertEqual(parse_requires_dist([]), [])

    def test_none_list(self):
        """Тест None."""
        self.assertEqual(parse_requires_dist(None), [])

    def test_simple_dep(self):
        """Тест простой зависимости."""
        deps = parse_requires_dist(["requests>=2.0"])
        self.assertEqual(deps, ["requests"])

    def test_dep_with_extra(self):
        """Тест зависимости с extra."""
        deps = parse_requires_dist(["PySocks; extra == 'socks'"])
        self.assertEqual(deps, [])

    def test_dep_with_markers(self):
        """Тест зависимости с маркерами."""
        deps = parse_requires_dist(
            ["win-inet-pton; sys_platform == 'win32'"]
        )
        self.assertEqual(deps, ["win-inet-pton"])

    def test_complex_deps(self):
        """Тест сложного списка зависимостей."""
        raw = [
            "certifi (>=2017.4.17)",
            "chardet (<5,>=3.0.2)",
            "PySocks (!=1.5.7); extra == 'socks'"
        ]
        deps = parse_requires_dist(raw)
        self.assertEqual(deps, ["certifi", "chardet"])


if __name__ == "__main__":
    unittest.main()
