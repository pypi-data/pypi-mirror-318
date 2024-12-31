import unittest
from stats_calculator.calculations import calculate_mean, calculate_std_dev


class TestStatsCalculations(unittest.TestCase):

    def test_calculate_mean(self):
        numbers = [1, 2, 3, 4, 5]
        expected_mean = 3
        self.assertEqual(calculate_mean(numbers), expected_mean)

    def test_calculate_std_dev(self):
        numbers = [1, 2, 3, 4, 5]
        # 精确到小数点后几位进行比较，这里以 5 位为例
        expected_std_dev = 1.41421
        result_std_dev = calculate_std_dev(numbers)
        self.assertAlmostEqual(result_std_dev, expected_std_dev, places=5)


if __name__ == '__main__':
    unittest.main()
