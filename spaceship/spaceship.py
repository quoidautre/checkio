def checkio(input):
	sofia = range(input[0], input[2], input[1])
	salesman = range(input[2], 0, (input[3] * -1))

	for bid in zip(sofia, salesman):
		if bid[0] >= bid[1]:
			return bid[0]

if __name__ == '__main__':
	assert checkio([150, 50, 1000, 100]) == 450
	assert checkio([150, 50, 900, 100]) == 400