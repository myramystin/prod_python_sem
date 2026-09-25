"""Ожидаемые типы вызовов: mypy проверяет этот файл вместе с catalog.py."""

from typing import assert_type

from catalog import Book, Video, first_with_prefix, labels, take_labels

books = [Book("Python Patterns"), Book("Algorithms")]
videos = [Video("Python internals", 900)]

assert_type(labels(books), list[str])
assert_type(labels(tuple(videos)), list[str])
assert_type(labels(book for book in books), list[str])

assert_type(first_with_prefix(books, "Py"), Book | None)
assert_type(first_with_prefix(videos, "Py"), Video | None)

assert_type(take_labels(books, 1), list[str])
assert_type(take_labels(videos, 1), list[str])
