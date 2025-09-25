import sys
import unittest

sys.path.append('../src/')

from my_utils import get_column

print("Made it here")

class unit_testing(unittest.TestCase):

    def test_get_column(self):
        watermelon_val = get_column('testing_numbers.csv', 0, 'Watermelon', 1)
        bananas_val = get_column('testing_numbers.csv', 0, 'Bananas', 1)
        self.assertGreater(watermelon_val, bananas_val) 
    
if __name__ == '__main__':
    unittest.main()