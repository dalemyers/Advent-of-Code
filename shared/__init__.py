from typing import List

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