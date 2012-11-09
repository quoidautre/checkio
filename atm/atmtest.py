import math

def calculateCommision(asdf):
	return 0.5 + (amountToWithdraw * 0.01)

def atm(balance, withdraws):
	withdraw = withdraws.pop(0)

	if withdraw % 5 not 0:
		return atm(balance, withdraws)

	commision = math.ceil(0.5 +(withdraw * 0.01))

	if commision <= balance:
		balance += commision

	return balance if len(withdraws) == 0 else atm(balance, withdraws)

def checkio(input):
	balance = input[0]
	withdraws = input[1]

	return atm(balance, withdraws)


if __name__ == '__main__':
	assert(checkio([120, [10, 20, 30]]) == 57)
	assert(checkio([120, [200, 10]]) == 109)
	assert(checkio([120, [3, 10]]) == 109)
	assert(checkio([120, [200 , 119]]) == 120)
	assert(checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56)