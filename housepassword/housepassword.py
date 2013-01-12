def checkio(password):
	if (len(password) < 10):
		return False

	requirement = [
		lambda x: x.isupper(),
		lambda x: x.islower(),
		lambda x: x.isdigit()
	]

	for char in password:
		for req in requirement:
			if req(char) is True:
				requirement.remove(req)
				if len(requirement) == 0:
					return True

	return False


if __name__ == '__main__':
	assert checkio('A1213pokl') is False
	assert checkio('bAse730onE') is True
	assert checkio('asasasasasasasaas') is False
	assert checkio('QWERTYqwerty') is False
	assert checkio('123456123456') is False
	assert checkio('QwErTy911poqqqq') is True