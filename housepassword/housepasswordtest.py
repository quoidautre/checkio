import housepassword
import unittest

class TestHousePassword(unittest.TestCase):
	def test_valid_password(self):
		self.assertTrue(housepassword.checkio('Aaaa3aaaaaaaaa'))

	def test_to_short_password(self):
		self.assertFalse(housepassword.checkio('Aa3'))

	def test_missing_lowercase_letter(self):
		self.assertFalse(housepassword.checkio('3AAAAAAAAAAAA'))

	def test_missing_uppercase_letter(self):
		self.assertFalse(housepassword.checkio('3aaaaaaaaaaaa'))

	def test_missing_digit(self):
		self.assertFalse(housepassword.checkio('AaAaAaAaAaAaAaAaAaA'))


if __name__ == '__main__':
	unittest.main()