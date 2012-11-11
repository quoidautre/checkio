def checkio(arr):
	arr.sort()
	arr.reverse()

	left_hand = []
	right_hand = []

	for weight in arr:
		if left_hand > right_hand:
			right_hand.append(weight)
		else:
			left_hand.append(weight)

	r = max(sum(left_hand), sum(right_hand)) - min(sum(left_hand), sum(right_hand))
	print r
	return r

if __name__ == '__main__':
	#assert checkio([10,10]) == 0
	#assert checkio([10]) == 10
	#assert checkio([5, 8, 13, 27, 14]) == 3
	#assert checkio([5,5,6,5]) == 1
	assert checkio([12, 30, 30, 32, 42, 49]) == 9
	#assert checkio([1, 1, 1, 3]) == 0
	#assert checkio([9, 9, 7, 6, 5]) == 0