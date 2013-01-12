romans = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'LX'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def checkio(num):
    result = ''

    for n, r in romans:
        while n <= num:
            result += r
            num -= n

    return result


if __name__ == '__main__':
    assert checkio(6) == 'VI'
    assert checkio(76) == 'LXXVI'
    assert checkio(499) == 'CDXCIX'
    assert checkio(3888) == 'MMMDCCCLXXXVIII'
