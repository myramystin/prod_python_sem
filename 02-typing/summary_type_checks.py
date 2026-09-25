"""Желаемые типы для двух режимов summarize; проверяются mypy."""

from typing import assert_type

from catalog import Book, Labeled, Video
from summary import summarize

items: list[Labeled] = [Book("Python Patterns"), Video("Python internals", 900)]

assert_type(summarize(items, "count"), int)
assert_type(summarize(items, "labels"), list[str])
