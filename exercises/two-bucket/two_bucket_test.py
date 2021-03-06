'''
All test cases adapted from
exercism/problem-specifications/exercises/two-bucket/canonical-data.json
'''

import unittest

from two_bucket import two_bucket


class TwoBucketTest(unittest.TestCase):
    def test_bucket_one_size_3_bucket_two_size_5_start_with_bucket_one(self):
        self.assertEqual(two_bucket(3, 5, 1, "one"), (4, "one", 5))

    def test_bucket_one_size_3_bucket_two_size_5_start_with_bucket_two(self):
        self.assertEqual(two_bucket(3, 5, 1, "two"), (8, "two", 3))

    def test_bucket_one_size_7_bucket_two_size_11_start_with_bucket_one(self):
        self.assertEqual(two_bucket(7, 11, 2, "one"), (14, "one", 11))

    def test_bucket_one_size_7_bucket_two_size_11_start_with_bucket_two(self):
        self.assertEqual(two_bucket(7, 11, 2, "two"), (18, "two", 7))

    def test_bucket_one_size_1_bucket_two_size_3_start_with_bucket_two(self):
        self.assertEqual(two_bucket(1, 3, 3, "two"), (1, "two", 0))

    def test_bucket_one_size_2_bucket_two_size_3_start_with_bucket_one(self):
        self.assertEqual(two_bucket(2, 3, 3, "one"), (4, "two", 1))


if __name__ == '__main__':
    unittest.main()
