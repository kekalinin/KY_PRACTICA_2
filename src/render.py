"""Модуль для рендеринга диаграммы Mermaid в PNG."""

import os
import shutil
import subprocess

from src.errors import ConfigError


def _find_mmdc():
    """Найти исполняемый файл mmdc в PATH.

    Returns:
        str: путь к mmdc

    Raises:
        ConfigError: если mmdc не найден
    """
    mmdc_path = shutil.which("mmdc")
    if not mmdc_path:
        raise ConfigError(
            "Mermaid CLI (mmdc) не установлен. "
            "Установите его командой: "
            "npm install -g @mermaid-js/mermaid-cli"
        )
    return mmdc_path


def _write_temp_file(mermaid_text, temp_path):
    """Записать текст Mermaid во временный файл.

    Args:
        mermaid_text: текст диаграммы
        temp_path: путь к временному файлу
    """
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(mermaid_text)


def _run_mmdc(mmdc_path, input_path, output_path):
    """Запустить mmdc для рендеринга PNG.

    Args:
        mmdc_path: путь к исполняемому файлу mmdc
        input_path: путь к входному .mmd файлу
        output_path: путь к выходному PNG файлу

    Raises:
        ConfigError: если рендеринг не удался
    """
    cmd = [mmdc_path, '-i', input_path, '-o', output_path, '-b', 'white']
    try:
        subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as error:
        raise ConfigError(
            f"Ошибка рендеринга: {error.stderr.decode('utf-8')}"
        )


def render_mermaid_to_png(mermaid_text, output_path):
    """Сохранить диаграмму Mermaid в файл PNG.

    Использует Mermaid CLI (mmdc). Если mmdc не установлен,
    выводится понятное сообщение об ошибке.

    Args:
        mermaid_text: текст диаграммы Mermaid
        output_path: путь к выходному PNG-файлу

    Raises:
        ConfigError: если рендер не удался
    """
    mmdc_path = _find_mmdc()
    temp_mmd = output_path.replace('.png', '.mmd')

    try:
        _write_temp_file(mermaid_text, temp_mmd)
        _run_mmdc(mmdc_path, temp_mmd, output_path)
        print(f"Диаграмма сохранена в {output_path}")
    finally:
        if os.path.exists(temp_mmd):
            os.unlink(temp_mmd)
