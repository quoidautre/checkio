def checkio(input):
	le = len(input)
	input.sort()

	if le % 2 == 0:
		first = float(input[le / 2 - 1])
		second = float(input[le / 2])

		return (first + second) / 2
	else:
		return float(input[le / 2])

if __name__ == '__main__':
	assert(checkio([1, 2, 3, 4, 5]) == 3)
	assert(checkio([3, 1, 2, 5, 3]) == 3)
	assert(checkio([1, 300, 2, 200, 1]) == 2)
	assert(checkio([3, 6, 20, 99, 10, 15]) == 12.5)