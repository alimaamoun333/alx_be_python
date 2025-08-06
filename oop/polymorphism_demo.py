# polymorphism_demo.py

import math

class Shape:
    """
    Base class for geometric shapes.
    Defines an interface for calculating area.
    """
    def area(self):
        """
        Calculate the area of the shape.
        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    """
    Rectangle shape, defined by length and width.
    Overrides area() to return length × width.
    """
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    """
    Circle shape, defined by radius.
    Overrides area() to return π × radius².
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)
