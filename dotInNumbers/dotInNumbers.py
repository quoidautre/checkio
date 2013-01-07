import re


def insertDots(input):
    result = ''
    dotIndex = len(input)
    for x in xrange(len(input)):
        if dotIndex % 3 == 0 and x != 0:
            result += '.'
        result += str(input[x])
        dotIndex -= 1

    return result


def checkio(input):
    result = []
    for part in input.split(' '):
        if (re.match('^\d+$', part)):
            result.append(insertDots(part))
        else:
            result.append(part)

    return " ".join(result)


if __name__ == '__main__':
    assert checkio('123456') == '123.456'
    assert checkio('333') == '333'
    assert checkio('9999999') == '9.999.999'
    assert checkio('123456 567890') == '123.456 567.890'
    assert checkio('price is 5799') == 'price is 5.799'
    assert checkio('he was born in 1966th') == 'he was born in 1966th'
    assert checkio("First, it's simple") == "First, it's simple"
