from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_coordinate: int | float,
            y_coordinate: int | float
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, ...],
            end_point: tuple[float, ...]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        product_of_lengths = self.get_length() * other.get_length()
        if product_of_lengths == 0:
            return 0
        angle_in_degrees = math.degrees(
            math.acos((self * other) / product_of_lengths)
        )
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rotate_x = (self.x * math.cos(math.radians(degrees))
                    - self.y * math.sin(math.radians(degrees)))
        rotate_y = (self.x * math.sin(math.radians(degrees))
                    + self.y * math.cos(math.radians(degrees)))
        return Vector(rotate_x, rotate_y)
