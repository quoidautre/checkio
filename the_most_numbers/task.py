def checkio(input):
    pass

if __name__ == '__main__':
    assert checkio(1, 2, 3) == 2
    assert checkio(5, -5) == 10
    assert checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4
    assert checkio() == 0
