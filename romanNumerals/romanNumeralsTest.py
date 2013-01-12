import unittest
import romanNumerals


class RomanNumeralsTest(unittest.TestCase):
    def test_6(self):
        self.assertEqual(romanNumerals.checkio(6), 'VI')

    def test_76(self):
        self.assertEqual(romanNumerals.checkio(76), 'LXXVI')

if __name__ == '__main__':
    unittest.main()
