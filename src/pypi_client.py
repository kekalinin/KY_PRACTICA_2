"""Клиент для получения данных из индекса PyPI."""

import json
import urllib.error
import urllib.request

from src.errors import ConfigError

PYPI_API_URL = "https://pypi.org/pypi/{package}/json"
TIMEOUT = 10


def fetch_package_info(package_name, repo_url):
    """Получить информацию о пакете из репозитория.

    Args:
        package_name: имя пакета
        repo_url: URL репозитория

    Returns:
        dict: JSON-данные о пакете

    Raises:
        ConfigError: при сетевых ошибках
    """
    url = PYPI_API_URL.format(package=package_name)
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            data = response.read()
            return json.loads(data)
    except urllib.error.HTTPError as error:
        raise ConfigError(f"Ошибка HTTP {error.code}: пакет не найден")
    except urllib.error.URLError as error:
        raise ConfigError(f"Сетевая ошибка: {error.reason}")
    except json.JSONDecodeError:
        raise ConfigError("Ошибка разбора JSON от репозитория") 
