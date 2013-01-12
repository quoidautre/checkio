import unittest
import polishNotation


class PolishNotationTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(polishNotation.checkio("a*b"), "ab*")

    def test_1(self):
        self.assertEqual(polishNotation.checkio("(a+(b*c))"), "abc*+")

    def test_2(self):
        self.assertEqual(polishNotation.checkio("((a+b)*(z+x))"), "ab+zx+*")

    def test_3(self):
        self.assertEqual(polishNotation.checkio("((a+t)*((b+(a+c))^(c+d)))"), "at+bac++cd+^*")

    def test_4(self):
        self.assertEqual(polishNotation.checkio("a+b*c+d"), "abc*+d+")


if __name__ == '__main__':
    unittest.main()
