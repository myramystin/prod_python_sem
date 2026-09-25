"""Поведение summarize: две ветки и неизвестный режим."""

from catalog import Book, Video
from summary import summarize

items = [Book("Python Patterns"), Video("Python internals", 900)]

assert summarize(items, "count") == 2
assert summarize(items, "labels") == ["Python Patterns", "Python internals"]
assert summarize([], "count") == 0

try:
    summarize(items, "unknown")
except ValueError:
    pass
else:
    raise AssertionError("unknown mode must raise ValueError")

print("Проверки summarize прошли")
