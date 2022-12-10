import math
from typing import Any


class Point:

    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) * (self.x - other.x)
            + (self.y - other.y) * (self.y - other.y)
        )

    def as_sign_only(self) -> "Point":
        if self.x > 0:
            x = 1
        elif self.x < 0:
            x = -1
        else:
            x = 0

        if self.y > 0:
            y = 1
        elif self.y < 0:
            y = -1
        else:
            y = 0

        return Point(x, y)

    def __repr__(self) -> str:
        return f"<Point x={self.x} y={self.y}>"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Point):
            return False

        return self.x == other.y and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __add__(self, other: Any) -> "Point":
        if not isinstance(other, Point):
            raise ValueError("Operand must be a Point")
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Any) -> "Point":
        if not isinstance(other, Point):
            raise ValueError("Operand must be a Point")
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Any) -> "Point":
        if not isinstance(other, Point):
            raise ValueError("Operand must be a Point")
        return Point(self.x - other.x, self.y - other.y)

    def __rsub__(self, other: Any) -> "Point":
        if not isinstance(other, Point):
            raise ValueError("Operand must be a Point")
        return Point(other.x - self.x, other.y - self.y)

    def __isub__(self, other: Any) -> "Point":
        if not isinstance(other, Point):
            raise ValueError("Operand must be a Point")
        self.x -= other.x
        self.y -= other.y
        return self

    @staticmethod
    def zero() -> "Point":
        return Point(0, 0)
