def checkio(input):
    fizz = input % 3 == 0
    buzz = input % 5 == 0

    if (fizz and buzz):
        return "Fizz Buzz"

    if (fizz):
        return "Fizz"

    if (buzz):
        return "Buzz"

    return str(input)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz"
    assert checkio(6) == "Fizz"
    assert checkio(5) == "Buzz"
    assert checkio(7) == "7"