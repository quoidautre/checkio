class CommisionCalculator():
	def calc(self, amountToWithdraw):
		return 0.5 + (amountToWithdraw * 0.01)

class Atm():
	def __init__(self, amount):
		self.amount = amount

	def withdraw(self, amount):
		if amount % 5 == 0:
			self.amount -= amount

		return self.amount