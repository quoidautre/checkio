import unittest
import romanNumerals


class RomanNumeralsTest(unittest.TestCase):
    def test_6(self):
        self.assertEqual(romanNumerals.checkio(6), 'VI')

    def test_76(self):
        self.assertEqual(romanNumerals.checkio(76), 'LXXVI')

    def test_499(self):
        self.assertEqual(romanNumerals.checkio(499), 'CDXCIX')

    def test_3888(self):
        self.assertEqual(romanNumerals.checkio(3888), 'MMMDCCCLXXXVIII')

    def test_1999(self):
        self.assertEqual(romanNumerals.checkio(1999), 'MCMXCIX')

    def test_1900(self):
        self.assertEqual(romanNumerals.checkio(1900), 'MCM')

if __name__ == '__main__':
    unittest.main()
