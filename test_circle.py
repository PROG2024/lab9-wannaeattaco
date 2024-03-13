"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle
import math
# TODO write 3 tests as described above


class CircleTest(unittest.TestCase):

    def test_typical_case(self):
        """Test add_area with two circles having positive radii."""
        circle1 = Circle(6)
        circle2 = Circle(8)
        combined_circle = circle1.add_area(circle2)
        combined_radius = math.sqrt((circle1.get_radius()**2) + (circle2.get_radius()**2))
        combined_area = math.pi*(combined_radius**2)
        self.assertEqual(combined_circle.get_radius(), combined_radius)
        self.assertAlmostEqual(combined_circle.get_area(), combined_area)

    def test_edge_case(self):
        circle1 = Circle(0)
        circle2 = Circle(8)
        combined_circle = circle1.add_area(circle2)
        self.assertEqual(combined_circle.get_radius(), circle2.get_radius())
        self.assertAlmostEqual(combined_circle.get_area(), circle2.get_area())

    def test_circle_constructor(self):
        with self.assertRaises(ValueError):
            Circle(-1)


