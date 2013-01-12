import itertools


def G(set):
    res = []
    for n in set:
        i = itertools.combinations(set, n)
        for tuppp in i:
            line = []
            l = []
            for x in tuppp:
                l.append(str(x))
                line.append(x)
            print ",".join(l)
            res.append(sum(line))

    print sum(res)
    return sum(res)


def checkio(num):
    result = 0
    for n in range(1, num + 1):
        print 'n: ' + str(n)
        result += G(range(1, n + 1))

    return result


if __name__ == '__main__':
    assert checkio(1) == 1
    assert checkio(2) == 7
    assert checkio(3) == 31
    assert checkio(4) == 111
