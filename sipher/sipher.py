def decode(map, sipher):
	result = ''
	rowpos = 0
	for row in map:
		linepos = 0
		for letter in row:
			if letter == 'X':
				result += sipher[rowpos][linepos]
			linepos += 1
		rowpos += 1

	return result

def rotate(map):
	result = []

	linepos = 0
	for row in map:
		rowpos = 3

		newRow = ''
		for letter in row:
			newRow += map[rowpos][linepos]
			rowpos -= 1

		result.append(newRow)
		linepos += 1

	return result

def checkio(data):
	result = ''
	map = data[0]
	sipher = data[1]

	for n in range(0, 4):
		result += decode(map, sipher)
		map = rotate(map)

	return result

if __name__ == '__main__':
	assert checkio([[
		'X...',
		'..X.',
		'X..X',
		'....'],[
		'itdf',
		'gdce',
		'aton',
		'qrdi']
		]) == 'icantforgetiddqd'

	assert checkio([[
		'....',
		'X..X',
		'.X..',
		'...X'],[
		'xhwc',
		'rsqx',
		'xqzz',
		'fyzr']
		]) == 'rxqrwsfzxqxzhczy'