def checkio(arr):
    result = []
    for x in arr:
        if type(x) is list:
            result.extend(checkio(x))
        else:
            result.append(x)

    return result

if __name__ == '__main__':
    assert checkio([1, 2, 3]) == [1, 2, 3]
    assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
    assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
