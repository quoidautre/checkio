import unittest
import matrixTranspond


class MatrixTranspondTest(unittest.TestCase):
    def test_1(self):
        actual = matrixTranspond.checkio([[1, 2], [1, 2]])
        expected = [[1, 1], [2, 2]]
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = matrixTranspond.checkio([[1, 0, 3, 4, 0],
                                          [2, 0, 4, 5, 6],
                                          [3, 4, 9, 0, 6]])
        expected = [[1, 2, 3],
                    [0, 0, 4],
                    [3, 4, 9],
                    [4, 5, 0],
                    [0, 6, 6]]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
