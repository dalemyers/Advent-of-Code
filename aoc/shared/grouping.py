from typing import Iterable, List, TypeVar

T = TypeVar("T")


def group_into(size: int, it: Iterable[T]) -> List[List[T]]:
    output = []
    chunk = []
    for item in it:
        chunk.append(item)
        if len(chunk) == size:
            output.append(chunk)
            chunk = []

    if len(chunk) > 0:
        output.append(chunk)

    return output
