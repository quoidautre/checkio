def is_palindrome(input):
    s = str(input)
    le = len(s)
    for x in xrange((le / 2) + 1):
        if s[x] != s[le - x -1]:
            return False

    return True

def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def checkio(lowest):
    for prime in gen_primes():
        if prime >= lowest and is_palindrome(prime):
            return prime

if __name__ == '__main__':
    assert(checkio(31) == 101)
    assert(checkio(130) == 131)
    assert(checkio(131) == 131)