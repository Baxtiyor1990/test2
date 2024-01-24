import unittest
from utils import arrs


class TestGetFunction(unittest.TestCase):

    def test_existing_index(self):
        result = arrs.get([1, 2, 3], 1)
        self.assertEqual(result, 2)

    def test_non_existing_index(self):
        result = arrs.get([1, 2, 3], 5, default="Not Found")
        self.assertEqual(result, "Not Found")

    def test_negative_index(self):
        result = arrs.get([1, 2, 3], -1, default="Not Found")
        self.assertEqual(result, "Not Found")


class TestMySliceFunction(unittest.TestCase):

    def test_full_range(self):
        result = arrs.my_slice([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_start_index(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], start=2)
        self.assertEqual(result, [3, 4, 5])

    def test_end_index(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], end=2)
        self.assertEqual(result, [1, 2])

    def test_negative_start_index(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], start=-3)
        self.assertEqual(result, [3, 4, 5])

    def test_negative_end_index(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], end=-1)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_empty_list(self):
        result = arrs.my_slice([], start=1, end=3)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
