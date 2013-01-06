def checkio(input):
    sofia = range(input[0], input[2], input[1])
    sofia.append(sofia[-1] + input[1])
    salesman = range(input[2], 0, (input[3] * -1))
    print salesman[-1]

    if not len(sofia):
        return input[2]

    z = zip(sofia, salesman)

    print sofia
    print salesman
    print z

    for bid in z:
        if bid[0] >= bid[1]:
            return bid[0]

if __name__ == '__main__':
    #assert checkio([150, 50, 1000, 100]) == 450
    #assert checkio([150, 50, 900, 100]) == 400
    #assert checkio([200, 100, 200, 100]) == 200
    assert checkio([500, 300, 700, 50]) == 700
