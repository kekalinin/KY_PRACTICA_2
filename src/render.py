"""Модуль для рендеринга диаграммы Mermaid в PNG."""

import os
import shutil
import subprocess

from src.errors import ConfigError


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
    mmdc_path = shutil.which("mmdc")
    if not mmdc_path:
        raise ConfigError(
            "Mermaid CLI (mmdc) не установлен. "
            "Установите его командой: "
            "npm install -g @mermaid-js/mermaid-cli"
        )

    temp_mmd = output_path.replace('.png', '.mmd')

    try:
        with open(temp_mmd, 'w', encoding='utf-8') as f:
            f.write(mermaid_text)

        cmd = [
            mmdc_path,
            '-i', temp_mmd,
            '-o', output_path,
            '-b', 'white'
        ]

        subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        print(f"Диаграмма сохранена в {output_path}")

    except subprocess.CalledProcessError as error:
        raise ConfigError(
            f"Ошибка рендеринга: {error.stderr.decode('utf-8')}"
        )
    finally:
        if os.path.exists(temp_mmd):
            os.unlink(temp_mmd)
