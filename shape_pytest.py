#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_pytest.py
Purpose: Simple pytest demonstration for the defined
shape classes.
"""

from shapes.rectangle import Rectangle
from shapes.circle import Circle
from shapes.triangle import Triangle


def test_rectangle():
    """
    Defines tests on some specific rectangle objects.
    """
    len7wid3 = Rectangle(7, 3)
    len1wid6 = Rectangle(1, 6)
    len5wid5 = Rectangle(5, 5)

    # Test areas, perimeters, and whether they are squares
    assert len7wid3.area() == 21
    assert len1wid6.area() == 6
    assert len5wid5.area() == 25
    assert len7wid3.perimeter() == 20
    assert len1wid6.perimeter() == 14
    assert len5wid5.perimeter() == 20
    assert not len7wid3.is_square()
    assert not len1wid6.is_square()
    assert len5wid5.is_square()


def test_circle():
    """
    Defines tests on some specific circle objects.
    """
    radius5 = Circle(5)
    radius8 = Circle(8)

    # Test areas, perimeters, and diameters
    assert radius5.area() == 78.54
    assert radius8.area() == 201.06
    assert radius5.perimeter() == 31.42
    assert radius8.perimeter() == 50.27
    assert radius5.diameter() == 10
    assert radius8.diameter() == 16

def test_triangle():
    """
    Defines tests on some specific triangle objects.
    """
    sides345 = Triangle(3, 4, 5)
    sides578 = Triangle(5, 7, 8)
    sides569 = Triangle(5, 6, 9)
    sides555 = Triangle(5, 5, 5)
    sides343 = Triangle(3, 4, 3)

    # Test areas, perimeters
    assert sides345.area() == 6.0
    assert sides578.area() == 17.32
    assert sides569.area() == 14.14
    assert sides555.area() == 10.83
    assert sides343.area() == 4.47
    assert sides345.perimeter() == 12
    assert sides578.perimeter() == 20
    assert sides569.perimeter() == 20
    assert sides555.perimeter() == 15
    assert sides343.perimeter() == 10

    # Test for equilateral triangle
    assert not sides345.is_equilateral()
    assert not sides578.is_equilateral()
    assert not sides569.is_equilateral()
    assert sides555.is_equilateral()
    assert not sides343.is_equilateral()

    # Test for isosceles triangle
    assert not sides345.is_isosceles()
    assert not sides578.is_isosceles()
    assert not sides569.is_isosceles()
    assert sides555.is_isosceles()
    assert sides343.is_isosceles()

