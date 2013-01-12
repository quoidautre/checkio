def checkio(notation):
    pass


if __name__ == '__main__':
    assert checkio("(a+(b*c))") == "abc*+"
    assert checkio("((a+b)*(z+x))") == "ab+zx+*"
    assert checkio("((a+t)*((b+(a+c))^(c+d)))") == "at+bac++cd+^*"
    assert checkio('a+b*c+d') == 'abc*+d+'
