"""Дополнительное упражнение: точный тип результата зависит от режима."""

from collections.abc import Sequence

from catalog import Labeled


def summarize(items: Sequence[Labeled], mode: str) -> int | list[str]:
    if mode == "count":
        return len(items)
    if mode == "labels":
        return [item.label for item in items]
    raise ValueError(f"unknown mode: {mode}")
