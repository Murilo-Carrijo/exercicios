from GenericArea import GenericArea

class Square(GenericArea):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Retangle(GenericArea):
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth

    def area(self):
        return self.base * self.heigth
    
    def perimeter(self):
        return 2 * (self.base + self.heigth)


class Circle(GenericArea):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159265359 * self.radius