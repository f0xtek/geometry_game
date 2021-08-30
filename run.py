from random import randint
from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<Point {self.x},{self.y}>'

    def __sub__(self, point):
        return self.distance_from_point(point)

    def falls_in_rectangle(self, rectangle):
        return rectangle.point1.x < self.x < rectangle.point2.x \
               and rectangle.point1.y < self.y < rectangle.point2.y

    def distance_from_point(self, point):
        """
        Same functionality as __sub__
        :param point: The point from which to calculate the current Point's distance
        :return: The distance between the 2 points
        """
        return sqrt(((self.x - point.x) ** 2 + (self.y - point.y) ** 2))


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return f'<Rectangle {self.point1},{self.point2}>'

    def area(self):
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
