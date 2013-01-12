def checkio(num):
    result = 0
    for x in str(num):
        if x == '0':
            x = '1'
        result += reduce(lambda x, y: x * y, range(1, int(x) + 1))

    return result


if __name__ == '__main__':
    assert checkio(100) == 3
    assert checkio(222) == 6
    assert checkio(1234) == 33
