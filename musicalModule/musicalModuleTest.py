import unittest
import musicalModule


class MusicalModuleTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(musicalModule.checkio((12, 8)),  4)

    def test_2(self):
        self.assertEqual(musicalModule.checkio((14, 21)), 7)

    def test_one_numbers_is_diveder_of_other(self):
        self.assertEqual(musicalModule.checkio((14, 7)), 7)


if __name__ == '__main__':
    unittest.main()
