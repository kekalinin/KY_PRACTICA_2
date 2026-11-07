"""Тесты для модуля validation."""

import os
import tempfile
import unittest

from src.errors import ValidationError
from src.validation import (
    validate_depth,
    validate_filter,
    validate_output,
    validate_package,
    validate_repo
)


class TestValidation(unittest.TestCase):
    """Тесты валидации параметров."""

    def test_valid_package(self):
        """Тест корректного имени пакета."""
        validate_package("requests")

    def test_empty_package(self):
        """Тест пустого имени пакета."""
        with self.assertRaises(ValidationError):
            validate_package("")

    def test_whitespace_package(self):
        """Тест имени пакета из пробелов."""
        with self.assertRaises(ValidationError):
            validate_package("   ")

    def test_valid_url(self):
        """Тест корректного URL."""
        validate_repo(
            "https://pypi.org/pypi/requests/json",
            False
        )

    def test_invalid_url(self):
        """Тест некорректного URL."""
        with self.assertRaises(ValidationError):
            validate_repo("not-a-url", False)

    def test_valid_test_repo(self):
        """Тест существующего файла тестового репозитория."""
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name

        try:
            validate_repo(tmp_path, True)
        finally:
            os.unlink(tmp_path)

    def test_missing_test_repo(self):
        """Тест несуществующего файла."""
        with self.assertRaises(ValidationError):
            validate_repo("/nonexistent/file.txt", True)

    def test_valid_output(self):
        """Тест корректного имени выходного файла."""
        validate_output("graph.png")

    def test_invalid_output(self):
        """Тест некорректного имени выходного файла."""
        with self.assertRaises(ValidationError):
            validate_output("graph.jpg")

    def test_valid_depth(self):
        """Тест корректной глубины."""
        validate_depth(5)

    def test_depth_too_small(self):
        """Тест слишком маленькой глубины."""
        with self.assertRaises(ValidationError):
            validate_depth(0)

    def test_depth_too_large(self):
        """Тест слишком большой глубины."""
        with self.assertRaises(ValidationError):
            validate_depth(101)

    def test_valid_filter(self):
        """Тест корректного фильтра."""
        validate_filter("test")

    def test_empty_filter(self):
        """Тест пустого фильтра (разрешено)."""
        validate_filter("")

    def test_filter_too_long(self):
        """Тест слишком длинного фильтра."""
        with self.assertRaises(ValidationError):
            validate_filter("a" * 51)


if __name__ == "__main__":
    unittest.main()
