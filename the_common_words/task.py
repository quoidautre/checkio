def checkio(first, second):
    f = first.split(",")

    result = []
    for x in second.split(","):
        if (x in f):
            result.append(x)

    result.sort()
    return ",".join(result)

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello"
    assert checkio("one,two,three", "four,five,six") == ""
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"