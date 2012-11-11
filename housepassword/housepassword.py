def checkio(password):
	return True


if __name__ == '__main__':
	assert checkio('A1213pokl') is False
	assert checkio('bAse730onE') is True
	assert checkio('asasasasasasasaas') is False
	assert checkio('QWERTYqwerty') is False
	assert checkio('123456123456') is False
	assert checkio('QwErTy911poqqqq') is True