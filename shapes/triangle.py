#!/usr/bin/env python

"""
Author: Rao Parasa (as advised by Nick Russo)
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains only a radius value
    and number of decimal places to use when computing values.
    """

    decimal_places = 2

    def __init__(self, side_a, side_b, side_c):
        """
        Create the triangle having 3 sides. Assuming the default is scalene triangle
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        """
        Refer https://mste.illinois.edu/dildine/heron/triarea.html
        Check on triangle inequality theorem, triangle with sides 2 6 9 is not valid
        SUM of TWO SIDES MUST ADD UP TO BE GREATER THAN THE LENGTH OF THE REMAINING THIRD SIDE
        """
        if ( ((self.side_a + self.side_b) <= self.side_c) or ((self.side_b + self.side_c) <= self.side_a) or ((self.side_c + self.side_a) <= self.side_b) ):
            raise RuntimeError("The side lengths do not fulfill the Triangle Inequality Theorem")


    def area(self):
        """
        Compute the area using the Heron's formula sqrt(s*(s-a)*(s-b)*(s-c)) 
        """
        s = 0.5 * self.perimeter()
        return round(sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter (circumference) using the sides
        """
        return (self.side_a + self.side_b + self.side_c)

    def is_equilateral(self):
        """
        check if the triangle is having equilateral sides.
        """
        return ((self.side_a == self.side_b) and (self.side_b == self.side_c))

    def is_isosceles(self):
        """
        check if the triangle is isosceles, having 2 sides equal.
        """
        return ((self.side_a == self.side_b) or (self.side_b == self.side_c) or (self.side_c == self.side_a))

