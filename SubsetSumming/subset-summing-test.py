import unittest
import subsetSumming


class SubsetSummingTest(unittest.TestCase):
    def test_G_1(self):
        self.assertEqual(subsetSumming.G(range(1, 2)), 1)

    def test_G_2(self):
        self.assertEqual(subsetSumming.G(range(1, 3)), 6)

    def test_G_3(self):
        self.assertEqual(subsetSumming.G(range(1, 4)), 24)

    def test_checkio_1(self):
        self.assertEqual(subsetSumming.checkio(1), 1)

    def test_checkio_2(self):
        self.assertEqual(subsetSumming.checkio(2), 7)

    def test_checkio_3(self):
        self.assertEqual(subsetSumming.checkio(3), 31)

    def test_checkio_4(self):
        self.assertEqual(subsetSumming.checkio(4), 111)

if __name__ == '__main__':
    unittest.main()
