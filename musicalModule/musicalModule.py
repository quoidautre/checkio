def checkio(data):
    for i in range(min(data), -1, -1):
        if data[0] % i == 0 and data[1] % i == 0:
            return i

if __name__ == '__main__':
    assert checkio((12, 8)) == 4
    assert checkio((14, 21)) == 7
