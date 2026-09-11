import pytest

from text_tools import count_words, normalize_spaces


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("  hello   world  ", "hello world"),
        ("", ""),
        ("\t\n", ""),
        ("Привет\nмир\t!", "Привет мир !"),
    ],
)
def test_normalize_spaces(text: str, expected: str) -> None:
    assert normalize_spaces(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [("hello world", 2), ("", 0), (" \t\n", 0), ("Привет, мир!", 2), ("one-two", 1)],
)
def test_count_words(text: str, expected: int) -> None:
    assert count_words(text) == expected
