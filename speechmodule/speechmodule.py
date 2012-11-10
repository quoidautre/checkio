def checkio(number):
	tens = [ "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
	nums = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
	result = ''

	if number % 100 < 20:
		result = nums[number % 100]
		number /= 100
	else:
		result = nums[number % 10]
		number /= 10

		result = tens[number % 10] + ' ' + result
		number /= 10

	if number is 0:
		return result.strip()

	return nums[number] + ' hundred ' + result

if __name__ == '__main__':
	assert checkio(4) == 'four'
	assert checkio(133) == 'one hundred thirty three'
	assert checkio(12) == 'twelve'
	assert checkio(101) == 'one hundred one'
	assert checkio(212) == 'two hundred twelve'
	assert checkio(40) == 'forty'