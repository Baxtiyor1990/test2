import unittest
from utils.arrs import get, my_slice

class TestArrsFunctions(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        result = get(array, 2)
        self.assertEqual(result, 3)

    def test_get_non_existing_index_with_default(self):
        array = [1, 2, 3, 4, 5]
        result = get(array, 10, default='Not found')
        self.assertEqual(result, 'Not found')

    def test_my_slice_default_parameters(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_my_slice_with_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array, start=1, end=4)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_negative_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array, start=-3, end=-1)
        self.assertEqual(result, [3, 4])

if __name__ == '__main__':
    unittest.main()

