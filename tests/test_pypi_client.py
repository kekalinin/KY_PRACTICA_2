"""Тесты для модуля pypi_client."""

import json
import unittest
from unittest.mock import patch, MagicMock
import urllib.error

from src.errors import ConfigError
from src.pypi_client import fetch_package_info


class TestPyPIClient(unittest.TestCase):
    """Тесты клиента PyPI."""

    @patch("src.pypi_client.urllib.request.urlopen")
    def test_fetch_success(self, mock_urlopen):
        """Тест успешного получения данных."""
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "info": {"requires_dist": ["requests"]}
        }).encode("utf-8")
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = fetch_package_info("test_pkg", "https://pypi.org")
        self.assertEqual(
            result["info"]["requires_dist"], ["requests"]
        )

    @patch("src.pypi_client.urllib.request.urlopen")
    def test_fetch_http_error(self, mock_urlopen):
        """Тест обработки HTTP ошибки."""
        mock_urlopen.side_effect = urllib.error.HTTPError(
            "url", 404, "Not Found", None, None
        )
        with self.assertRaises(ConfigError):
            fetch_package_info("bad_pkg", "https://pypi.org")


if __name__ == "__main__":
    unittest.main()
