import unittest
import polishNotation


class PolishNotationTest(unittest.TestCase):
    def dtest_0(self):
        self.assertEqual(polishNotation.checkio("a*b"), "ab*")

    def test_1(self):
        self.assertEqual(polishNotation.checkio("(a+(b*c))"), "abc*+")

    def Dtest_2(self):
        self.assertEqual(polishNotation.checkio("((a+b)*(z+x))"), "ab+zx+*")

    def Dtest_3(self):
        self.assertEqual(polishNotation.checkio("((a+t)*((b+(a+c))^(c+d)))"), "at+bac++cd+^*")

    def Dtest_4(self):
        self.assertEqual(polishNotation.checkio("a+b*c+d"), "abc*+d+")


if __name__ == '__main__':
    unittest.main()
