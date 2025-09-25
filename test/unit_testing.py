import sys
import unittest
import random as rd

sys.path.append('../src/')

from my_utils import get_column, mean_ints, median_ints, standard_deviation_ints

class unit_testing(unittest.TestCase):

    def test_get_column(self):
        watermelon_val = get_column('testing_numbers.csv', 0, 'Watermelon', 1)
        bananas_val = get_column('testing_numbers.csv', 0, 'Bananas', 1)
        self.assertGreater(watermelon_val, bananas_val)
    
    def test_mean_ints(self):
        bottom = rd.randint(1,9)
        test_array = range(5, rd.randint(10, 2000))
        self.assertTrue(mean_ints(test_array) > bottom)

    def test_median_ints(self):
        mid = rd.randint(9,12)
        test_array = [rd.randint(0,4), rd.randint(5,8), mid, rd.randint(13,16), rd.randint(17,22)]
        self.assertEqual(median_ints(test_array), mid)
    
    def test_standard_deviation_ints(self):
        test_array = []
        for i in range(rd.randint(10,20)):
            test_array.append(rd.randint(5,10))
        self.assertLess(standard_deviation_ints(test_array), 15)
    
if __name__ == '__main__':
    unittest.main()