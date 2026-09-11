"""Командный интерфейс: только разбор аргументов и вывод."""

import argparse

from text_tools.core import count_words, normalize_spaces


def main() -> None:
    parser = argparse.ArgumentParser(description="Нормализация текста и подсчёт слов")
    parser.add_argument("text", help="Текст в кавычках")
    parser.add_argument("--count", action="store_true", help="Посчитать слова")
    args = parser.parse_args()
    if args.count:
        print(count_words(args.text))
    else:
        print(normalize_spaces(args.text))
