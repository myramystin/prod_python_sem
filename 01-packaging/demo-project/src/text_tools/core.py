"""Обработка текста без ввода-вывода и сторонних зависимостей."""


def normalize_spaces(text: str) -> str:
    """Убрать крайние пробелы и заменить серии whitespace одним пробелом."""
    return " ".join(text.split())


def count_words(text: str) -> int:
    """Посчитать фрагменты, разделённые whitespace; пунктуацию не удалять."""
    return len(text.split())




