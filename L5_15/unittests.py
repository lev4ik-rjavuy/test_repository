import unittest

from L5_15 import calculate_average_pressure, is_pressure_normal


class TestPressureAnalyzer(unittest.TestCase):
    def test_calculate_average_multiple_measurements(self):
        measurements = [(120, 80), (110, 70), (115, 75)]
        self.assertEqual(calculate_average_pressure(measurements), (115, 75))

    def test_calculate_average_single_measurement(self):
        measurements = [(130, 85)]
        self.assertEqual(calculate_average_pressure(measurements), (130, 85))

    def test_calculate_average_empty_list(self):
        self.assertEqual(calculate_average_pressure([]), (0, 0))

    def test_calculate_average_rounding(self):
        measurements = [(110, 70), (111, 71)]
        self.assertEqual(calculate_average_pressure(measurements), (110, 70))

    def test_pressure_normal_ideal(self):
        self.assertTrue(is_pressure_normal(110, 70))

    def test_pressure_boundaries_inclusive(self):
        self.assertTrue(is_pressure_normal(120, 80))
        self.assertTrue(is_pressure_normal(90, 60))

    def test_pressure_high_systolic(self):
        self.assertFalse(is_pressure_normal(121, 70))
        self.assertFalse(is_pressure_normal(150, 70))

    def test_pressure_low_systolic(self):
        self.assertFalse(is_pressure_normal(89, 70))

    def test_pressure_high_diastolic(self):
        self.assertFalse(is_pressure_normal(110, 81))
        self.assertFalse(is_pressure_normal(110, 100))

    def test_pressure_low_diastolic(self):
        self.assertFalse(is_pressure_normal(110, 59))


if __name__ == "__main__":
    unittest.main(verbosity=2)
