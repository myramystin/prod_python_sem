"""Проверки поведения: запускаются обычным Python без pytest."""

from catalog import Book, Video, first_with_prefix, labels, take_labels

books = [Book("Python Patterns"), Book("Algorithms")]
videos = [Video("Python internals", 900)]

assert labels(book for book in books) == ["Python Patterns", "Algorithms"]
assert labels(videos) == ["Python internals"]
assert first_with_prefix(books, "Py") is books[0]
assert first_with_prefix(videos, "missing") is None
assert take_labels(books, 1) == ["Python Patterns"]
assert take_labels(videos, 0) == []

try:
    take_labels(books, -1)
except ValueError:
    pass
else:
    raise AssertionError("negative limit must raise ValueError")

print("Проверки поведения прошли")
