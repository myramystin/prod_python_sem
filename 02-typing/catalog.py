from dataclasses import dataclass
from typing import Protocol


class Labeled(Protocol):
    # TODO: опишите читаемое строковое свойство label.
    pass


@dataclass(frozen=True)
class Book:
    title: str

    @property
    def label(self) -> str:
        return self.title


@dataclass(frozen=True)
class Video:
    label: str
    duration_seconds: int


def labels(items: list[Book]) -> list[str]:
    return [item.label for item in items]


def first_with_prefix(items: list[Book], prefix: str) -> Book | None:
    return next((item for item in items if item.label.startswith(prefix)), None)


def take_labels(items: list[Labeled], limit: int) -> list[str]:
    if limit < 0:
        raise ValueError("limit must be nonnegative")
    return [item.label for item in items[:limit]]
