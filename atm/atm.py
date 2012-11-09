import math

def checkio(input):
	balance = input[0]
	if len(input[1]) is 0:
		return balance

	withdraw = input[1].pop(0)
	if withdraw % 5 != 0:
		return checkio([ balance, input[1] ])

	balanceWithdraw = withdraw + (0.5 + (withdraw * 0.01))
	if balanceWithdraw <= balance:
		balance = math.floor(balance - balanceWithdraw)

	return checkio([ balance, input[1] ])

if __name__ == '__main__':
	assert(checkio([120, [10, 20, 30]]) == 57)
	assert(checkio([120, [200, 10]]) == 109)
	assert(checkio([120, [3, 10]]) == 109)
	assert(checkio([120, [200 , 119]]) == 120)
	assert(checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56)