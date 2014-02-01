import unittest
import prime


class PrimeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(prime.checkio(31), 101)

    def test_2(self):
        self.assertEqual(checkio(130), 131)

    def test_3(self):
        self.assertEqual(checkio(131), 131)

if __name__ == '__main__':
    unittest.main()
