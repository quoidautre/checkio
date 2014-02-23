import unittest
import task


class TaskTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(task.checkio(1, 2, 3), 2)

    def test_2(self):
        self.assertEqual(task.checkio(5, -5), 10)

    def test_3(self):
        self.assertEqual(task.checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4)

    def test_4(self):
        self.assertEqual(task.checkio(), 0)

if __name__ == '__main__':
    unittest.main()
