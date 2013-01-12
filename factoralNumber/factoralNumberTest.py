import unittest
import factoralNumber


class FactoralNumberTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factoralNumber.checkio(100), 3)

    def test_2(self):
        self.assertEqual(factoralNumber.checkio(222), 6)

    def test_3(self):
        self.assertEqual(factoralNumber.checkio(1234), 33)

if __name__ == '__main__':
    unittest.main()
