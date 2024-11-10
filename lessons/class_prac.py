class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):  # Never a stated return in constructors
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:  # methods have to have a return value
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:  # methods have to have a return value
        self.x += dx


# Point is now a data type
p0: Point = Point(10.0, 0.0)  # parameters in __init__ constructor
p0.translate_x(-5.0)
print(p0.dist_from_origin())
p1: Point = Point(1.0, 2.0)
p1.translate_x(1.0)
print(p1.dist_from_origin())


class Coordinate:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_dist(self, other) -> float:
        return (((c1.x - other.x) ** 2) + ((c1.y - other.y) ** 2)) ** 0.5


c1: Coordinate = Coordinate(1.0, 2.0)
c2: Coordinate = Coordinate(4.0, 6.0)
distance = c1.get_dist(c2)
print("Distance:", distance)
