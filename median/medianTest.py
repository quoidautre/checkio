import unittest
import median


class MedianTest(unittest.TestCase):
    def test_1(self):
        actual = median.checkio([1, 2, 3, 4, 5])
        self.assertEqual(actual, 3)

    def test_2(self):
        actual = median.checkio([3, 1, 2, 5, 3])
        self.assertEqual(actual, 3)

    def test_3(self):
        actual = median.checkio([1, 300, 2, 200, 1])
        self.assertEqual(actual, 2)

    def test_4(self):
        actual = median.checkio([3, 6, 20, 99, 10, 15])
        self.assertEqual(actual, 12.5)

if __name__ == '__main__':
    unittest.main()
