import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, mx, my):
        self.x += mx
        self.y += my

    def dist(self, other=None):
        if other is None:
            return math.sqrt(self.x ** 2 + self.y ** 2)
        else:
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


p1 = Point(2, 3)
