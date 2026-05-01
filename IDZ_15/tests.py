import unittest

from app import InvalidDimensionError, calculate_area


class TestRectangleArea(unittest.TestCase):

    def test_calculate_area_valid(self):
        self.assertEqual(calculate_area(5, 4), 20.0)
        self.assertEqual(calculate_area(2.5, 4), 10.0)

    def test_calculate_area_zero_dimension(self):
        with self.assertRaises(InvalidDimensionError):
            calculate_area(0, 5)
        with self.assertRaises(InvalidDimensionError):
            calculate_area(5, 0)

    def test_calculate_area_negative_dimension(self):
        with self.assertRaises(InvalidDimensionError):
            calculate_area(-5, 4)
        with self.assertRaises(InvalidDimensionError):
            calculate_area(5, -4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
