"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle

# TODO write 3 tests as described above


class CircleTest(unittest.TestCase):

    def set(self):
        self.circle = Circle(1)

    def test_typical_case(self):
        with self.assertRaises(ValueError):
            Circle.add_area(self.circle, Circle(1))

    def test_edge_case(self):
        with self.assertRaises(ValueError):
            Circle.add_area(self.circle, Circle(0))

    def raise_exception(self):
        with self.assertRaises(ValueError):
            Circle(-1)

