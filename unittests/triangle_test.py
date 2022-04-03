#!/usr/bin/env python

"""
Author: Rao Parasa, based on code from Nick Russo
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.sides345 = Triangle(3, 4, 5)
        self.sides578 = Triangle(5, 7, 8)
        self.sides569 = Triangle(5, 6, 9)
        self.sides555 = Triangle(5, 5, 5)
        self.sides343 = Triangle(3, 4, 3)

    def test_area(self):
        """
        Compare the test rectangle area computations to the actual values.
        """
        self.assertEqual(self.sides345.area(), 6.0)
        self.assertEqual(self.sides578.area(), 17.32)
        self.assertEqual(self.sides569.area(), 14.14)
        self.assertEqual(self.sides555.area(), 10.83)
        self.assertEqual(self.sides343.area(), 4.47)

    def test_perimeter(self):
        """
        Compare the test rectangle perimeter computations to the actual values.
        """
        self.assertEqual(self.sides345.perimeter(), 12)
        self.assertEqual(self.sides578.perimeter(), 20)
        self.assertEqual(self.sides569.perimeter(), 20)
        self.assertEqual(self.sides555.perimeter(), 15)
        self.assertEqual(self.sides343.perimeter(), 10)

    def test_is_equilateral(self):
        """
        Confirm or deny if the triangle is an equilateral.
        """
        self.assertFalse(self.sides345.is_equilateral())
        self.assertFalse(self.sides578.is_equilateral())
        self.assertFalse(self.sides569.is_equilateral())
        self.assertTrue(self.sides555.is_equilateral())
        self.assertFalse(self.sides343.is_equilateral())

    def test_is_isosceles(self):
        """
        Confirm or deny if the rectangle is a square.
        """
        self.assertFalse(self.sides345.is_isosceles())
        self.assertFalse(self.sides578.is_isosceles())
        self.assertFalse(self.sides569.is_isosceles())
        self.assertTrue(self.sides555.is_isosceles())
        self.assertTrue(self.sides343.is_isosceles())
