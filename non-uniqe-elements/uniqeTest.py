import unittest
import uniqe


class UniqeTest(unittest.TestCase):
    def test_1(self):
        actual = uniqe.checkio([1, 2, 3, 1, 3])
        self.assertEqual(actual, [1, 3, 1, 3])

    def test_2(self):
        actual = uniqe.checkio([1, 2, 3, 4, 5])
        self.assertEqual(actual, [])

    def test_3(self):
        actual = uniqe.checkio([5, 5, 5, 5, 5])
        self.assertEqual(actual, [5, 5, 5, 5, 5])

    def test_4(self):
        actual = uniqe.checkio([10, 9, 10, 10, 9, 8])
        self.assertEqual(actual, [10, 9, 10, 10, 9])

if __name__ == '__main__':
    unittest.main()
