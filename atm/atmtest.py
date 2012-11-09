import atm, unittest

class TestWithdrawAmount(unittest.TestCase):
	def setUp(self):
		self.startValue = 100
		self.atm = atm.Atm(self.startValue)

	def test_can_withdraw_five(self):
		self.atm.withdraw(5)
		self.assertNotEqual(self.atm.amount, self.startValue)

	def test_cannot_withdraw_seven(self):
		self.atm.withdraw(7)
		self.assertEqual(self.atm.amount, self.startValue)

class TestCommisionCalculator(unittest.TestCase):
	def setUp(self):
		self.cc = atm.CommisionCalculator()

	def test_always_return_base_commision(self):
		self.assertEqual(0.5, self.cc.calc(0))

	def test_and_one_percentage(self):
		self.assertEqual(1.5, self.cc.calc(100))
		self.assertEqual(1, self.cc.calc(50))

class TestAtm(unittest.TestCase):
	def test_only_withdraw_if_dividable_with_5(self):
		a = atm.Atm(100)
		a.withdraw(4)
		self.assertEqual(a.amount, 100)

	#def test_checkio(self):
		#self.assertTrue(checkio([120, [10, 20, 30]]) == 57)
		#self.assertTrue(checkio([120, [200, 10]]) == 109)
		#self.assertTrue(checkio([120,[3, 10]]) == 109)
		#self.assertTrue(checkio([120, [200 , 119]]) == 120)
		#self.assertTrue(checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56)

if __name__ == '__main__':
	unittest.main()