import unittest

from L7_15 import find_popular_routes


class TestTransportAnalyzer(unittest.TestCase):

    def test_find_popular_routes_standard(self):
        trips = [
            {"start": "A", "end": "B"},
            {"start": "A", "end": "B"},
            {"start": "B", "end": "C"},
            {"start": "A", "end": "B"},
        ]
        expected = [(("A", "B"), 3), (("B", "C"), 1)]
        self.assertEqual(find_popular_routes(trips), expected)

    def test_find_popular_routes_equal_counts(self):
        trips = [{"start": "X", "end": "Y"}, {"start": "Z", "end": "W"}]
        expected = [(("X", "Y"), 1), (("Z", "W"), 1)]
        self.assertEqual(find_popular_routes(trips), expected)

    def test_find_popular_routes_empty(self):
        self.assertEqual(find_popular_routes([]), [])

    def test_find_popular_routes_missing_keys(self):
        trips = [{"start": "A"}, {"start": "A", "end": "B"}]
        expected = [(("A", "B"), 1)]
        self.assertEqual(find_popular_routes(trips), expected)

    def test_find_popular_routes_same_start_and_end(self):
        trips = [{"start": "A", "end": "A"}, {"start": "A", "end": "A"}]
        expected = [(("A", "A"), 2)]
        self.assertEqual(find_popular_routes(trips), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
