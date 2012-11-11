import unittest
import sipher

class MapReaderTest(unittest.TestCase):
	def setUp(self):
		self.map = [
			'....',
			'X..X',
			'.X..',
			'...X'
		]

		self.sipher = [
			'xhwc',
			'rsqx',
			'xqzz',
			'fyzr'
		]

	def test_canReadLettersUsingSipher(self):
		self.assertEqual('rxqr', sipher.decode(self.map, self.sipher))

	def test_canrotate90deegres(self):
		expected = [
			'..X.',
			'.X..',
			'....',
			'X.X.'
		]

		rotated = sipher.rotate(self.map)
		print rotated
		print expected

		self.assertEqual(expected, rotated)

if __name__ == '__main__':
	unittest.main()