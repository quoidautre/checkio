operators = [ '*', '+', '-', '^', '/']

def reader(notation):
    result = ''
    expressions = []

    for x in notation:
        if x == '(':
            checkio(notation[1:])
        elif x == ')':
            expressions.append(result)
            result = ''
        else:
            result += x

    print expressions



def checkio(notation):
    reader(notation)

if __name__ == '__main__':
    assert checkio("(a+(b*c))") == "abc*+"
    assert checkio("((a+b)*(z+x))") == "ab+zx+*"
    assert checkio("((a+t)*((b+(a+c))^(c+d)))") == "at+bac++cd+^*"
    assert checkio('a+b*c+d') == 'abc*+d+'
