import itertools


def G(set):
    result = []
    for n in set:
        for x in itertools.combinations(set, n):
            result.append(sum(x))

    return sum(result)


def checkio(num):
    result = 0
    for n in xrange(1, num + 1):
        result += G(xrange(1, n + 1))

    return result


if __name__ == '__main__':
    assert checkio(1) == 1
    assert checkio(2) == 7
    assert checkio(3) == 31
    assert checkio(4) == 111
