import math

class Shape:
    def __init__(self):
        self.name = "Shape"

    def area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius

class Square:
    def __init__(self, side):
        if isinstance(side, int) or isinstance(side, float):
            self.name = "Square"
            self.side = side
        else:
            raise Exception

    def area(self):
        return 4 * self.side