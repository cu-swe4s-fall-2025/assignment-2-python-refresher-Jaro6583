import random as rand
import sys
import unittest

sys.path.append("../../src/")

import my_utils as tools # noqa


class my_testing(unittest.TestCase):
    def test_mean(self):
        top = 1000
        bottom = -1000
        test_array = []
        for i in range(rand.randint(5, 20)):
            test_array.append(rand.randint(bottom, top))
        self.assertTrue(tools.mean_ints(test_array) < top)
        self.assertFalse(tools.mean_ints(test_array) < bottom)

    def test_median(self):
        top = 1000
        bottom = -1000
        test_array = []
        for i in range(rand.randint(5, 20)):
            test_array.append(rand.randint(bottom, top))
        self.assertTrue(tools.median_ints(test_array) < top)
        self.assertFalse(tools.median_ints(test_array) < bottom)

    def test_standard_deviation(self):
        top = 1000
        bottom = -1000
        test_array = []
        for i in range(rand.randint(5, 20)):
            test_array.append(rand.randint(bottom, top))
        self.assertTrue(tools.standard_deviation_ints(test_array) > 0)


if __name__ == "__main__":
    unittest.main()
