def checkio(input):
	grouped = {}

	for x in input:
		grouped[x] = 0

	for x in input:
		grouped[x] += 1

	return filter(lambda x: grouped[x] > 1, input)

if __name__ == '__main__':
	assert(checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3])
	assert(checkio([1, 2, 3, 4, 5]) == [])
	assert(checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5])
	assert(checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9])