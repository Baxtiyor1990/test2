import unittest
from utils import arrs

class TestArrays(unittest.TestCase):
    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.get(array, 2)
        self.assertEqual(result, 3)

    def test_get_non_existing_index_with_default(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.get(array, 10, default='not_found')
        self.assertEqual(result, 'not_found')

    def test_my_slice_with_positive_indices(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array, start=1, end=4)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_with_negative_indices(self):
        array = [1, 2, 3, 4, 5]
        result = arrs.my_slice(array, start=-3, end=None)
        self.assertEqual(result, [3, 4, 5])

if __name__ == '__main__':
    unittest.main()


