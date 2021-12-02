import math

def manhattan_distance(x1, y1, x2, y2) -> int:
    return math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)

def distance(x1, y1, x2, y2) -> float:
    return math.sqrt(manhattan_distance(x1, y1, x2, y2))
