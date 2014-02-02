import unittest
import generator


class GeneratorTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(generator.checkio([4, 2, 10]), 1)

    def test_2(self):
        self.assertEqual(generator.checkio([1, 2, 3]), 0)

    def test_3(self):
        self.assertEqual(generator.checkio([5, 2, 9, 6]), 2)

if __name__ == '__main__':
    unittest.main()
