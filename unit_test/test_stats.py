import unittest
from stats import calculate_stats


class TestStatisticsCalculation(unittest.TestCase):
    def test_calculate_stats_with_valid_data(self):
        # Test with a list of numerical data
        data = [10, 6, 2, 8, 4]
        result = calculate_stats(data)
        self.assertEqual(result["mean"], 6.0)
        self.assertEqual(result["median"], 6)
        self.assertAlmostEqual(
            result["standard_deviation"], 2.828427, places=5)

    def test_calculate_stats_with_empty_list(self):
        # Test with an empty list
        data = []
        with self.assertRaises(ValueError):
            calculate_stats(data)

    def test_calculate_stats_with_single_element_list(self):
        # Test with a list containing a single element
        data = [5]
        result = calculate_stats(data)
        self.assertEqual(result["mean"], 5.0)
        self.assertEqual(result["median"], 5)
        self.assertEqual(result["standard_deviation"], 0.0)


if __name__ == "__main__":
    unittest.main()
