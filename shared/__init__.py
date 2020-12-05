from typing import Any, List

def read_file_lines(path):
    with open(path) as input_file:
        contents = input_file.readlines()
    return [c.strip() for c in contents]

def create_int_grid(width: int, height: int, default: int = 0):
    return [[default for x in range(width)] for y in range(height)]

def create_bool_grid(width: int, height: int, default: bool = False):
    return [[default for x in range(width)] for y in range(height)]

def is_int(value) -> bool:
    try:
        int(value)
        return True
    except:
        return False

def read_ints_from_file(path: str) -> List[int]:
    with open(path) as f:
        input_data = f.readlines()
    return list(map(int, input_data))

def get_positions(input_list: List[Any], value: Any) -> List[int]:
    positions = []
    for index, input_value in enumerate(input_list):
        if input_value == value:
            positions.append(index)
    return positions

def find_locations(input_list: List[Any], value: List[Any]) -> List[int]:
    locations = []
    for start_index in range(0, len(input_list) - len(value) + 1):
        input_range = input_list[start_index:start_index + len(value)]
        if value == input_range:
            locations.append(start_index)
    return locations