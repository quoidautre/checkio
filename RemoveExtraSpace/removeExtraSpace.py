def checkio(string):
    string = string.replace('  ', ' ')
    if '  ' in string:
        return checkio(string)

    return string

if __name__ == '__main__':
    assert checkio('I  like   python') == "I like python"
