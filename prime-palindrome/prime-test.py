import unittest
import prime


class PrimeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(prime.checkio(31), 101)

    def test_2(self):
        self.assertEqual(prime.checkio(130), 131)

    def test_3(self):
        self.assertEqual(prime.checkio(131), 131)

    def test_4(self):
        self.assertTrue(prime.is_palindrome('101'))

if __name__ == '__main__':
    unittest.main()
