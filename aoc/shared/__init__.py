from typing import Any, Iterable, List

from .grids import *
from .input import *
from .maths import *


def is_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_positions(input_list: List[Any], value: Any) -> List[int]:
    positions = []
    for index, input_value in enumerate(input_list):
        if input_value == value:
            positions.append(index)
    return positions


def find_locations(input_list: List[Any], value: List[Any]) -> List[int]:
    locations = []
    for start_index in range(0, len(input_list) - len(value) + 1):
        input_range = input_list[start_index : start_index + len(value)]
        if value == input_range:
            locations.append(start_index)
    return locations


def product(iterable: Iterable) -> Any:
    value = 1
    for i in iterable:
        value = value * i
    return value


def transpose(values: List[List[Any]]) -> List[List[Any]]:
    return list(map(list, zip(*values)))
