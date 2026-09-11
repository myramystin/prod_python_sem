# seminar-text-tools

Учебный пакет: нормализация пробельных символов и подсчёт слов.
Python 3.14+. Имена: дистрибутив `seminar-text-tools`, импорт `text_tools`,
команда `text-tools`. Публиковать пакет для работы этих примеров не требуется.

Из этого каталога:

```bash
uv sync
uv run text-tools "  hello   world  "
uv run text-tools "hello world" --count
uv run python -m text_tools "hello world" --count
uv run python -c "from text_tools import count_words; print(count_words('hello world'))"
```

Ожидаемый вывод по порядку: `hello world`, `2`, `2`, `2`.
Слово здесь — фрагмент между пробельными символами: `one-two` считается одним
словом, пустая строка содержит ноль слов. Нормализация заменяет также табуляции
и переводы строк одним пробелом. Ошибки аргументов CLI обрабатывает `argparse`.

```python
from text_tools import count_words, normalize_spaces

assert normalize_spaces("  Привет\nмир!  ") == "Привет мир!"
assert count_words("Привет мир!") == 2
```

Проверки и сборка:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv build
```

Обычная установка в активное отдельное окружение: `python -m pip install .`.
Для разработки с pip: `python -m pip install -e .`, затем
`python -m pip install pytest ruff mypy`. Dev-группу pip при установке проекта
автоматически не устанавливает.

Проверка wheel вне исходников описана в [инструкции проверки wheel](../wheel-check.md).
`uv.lock` фиксирует окружение разработки; после его появления используйте
`uv sync --locked`, чтобы проверять согласованность с `pyproject.toml`.
