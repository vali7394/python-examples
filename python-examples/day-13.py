"""Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute
the area. """


class Circle:
    def __init__(self, r):
        self.radius = r

    def compute_area(self):
        return self.radius * 2 * 3.14


circle = Circle(2)
print(circle.compute_area())

"""Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which 
can compute the area."""


class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def compute_area(self):
        return self.l * self.w


rect = Rectangle(2, 3)
print(rect.compute_area())

"""Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as 
argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default. 
"""


class Shape(object):
    def __init__(self):
        pass

    def get_area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length

    def get_area(self):
        return self.length * self.length


sq = Square(5)
print(sq.get_area())

"""Please raise a RuntimeError exception."""


def error_method():
    raise RuntimeError('Runtime error occurred')


error_method()