"""
A geometry game where the player attempts to guess both the area,
and a point which falls inside a randomly generated rectangle.
"""
from random import randint
from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        String representation of the current Point object.
        :return:
        """
        return f'<Point {self.x},{self.y}>'

    def __sub__(self, point):
        """
        Allow for the subtraction operation between 2 Point objects.
        :param point: The Point which you wish to subtract from the current Point.
        :return: The distance between the 2 Points as a float.
        """
        return self.distance_from_point(point)

    def falls_in_rectangle(self, rectangle):
        """
        Return whether the current Point falls inside the
        given Rectangle.
        :param rectangle: The Rectangle object in which to check for the current Point
        :return: The boolean result of whether the Point falls inside the Rectangle
        """
        return rectangle.point1.x < self.x < rectangle.point2.x \
               and rectangle.point1.y < self.y < rectangle.point2.y

    def distance_from_point(self, point):
        """
        Calculate and return the distance between the current Point and the given Point.
        :param point: The point from which to calculate the current Point's distance
        :return: The distance between the 2 points
        """
        return sqrt(((self.x - point.x) ** 2 + (self.y - point.y) ** 2))


class Rectangle:
    """
    Class representing a Rectangle. It accepts 2 parameters,
    a Point representing the lower-left corner of the rectangle
    and a Point representing the upper-right corner of the rectangle.
    """

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        """
        The string representation of the current Rectangle object.
        :return:
        """
        return f'<Rectangle {self.point1},{self.point2}>'

    def area(self):
        """
        Return the area of the Rectangle
        :return: The rectangle area
        """
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)


if __name__ == '__main__':
    rectangle_x = Rectangle(
        Point(randint(0, 9), randint(0, 9)),
        Point(randint(10, 19), randint(10, 19)))

    print("Rectangle coordinates: ",
          rectangle_x.point1.x, ",",
          rectangle_x.point1.y, "and",
          rectangle_x.point2.x, ",",
          rectangle_x.point2.y)

    user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

    rectangle_x_area = rectangle_x.area()
    user_area = float(input("Guess rectangle area: "))

    print("Your point was inside the rectangle:", user_point.falls_in_rectangle(rectangle_x))

    if rectangle_x_area == user_area:
        print("You guessed the correct area!")
    else:
        print("Your area was off by", rectangle_x_area - user_area)
