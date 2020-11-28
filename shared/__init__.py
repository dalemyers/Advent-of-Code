
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