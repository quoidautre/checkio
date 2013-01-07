def checkio(input):
    sofiaBid = input[0]
    sofiaInc = input[1]
    salesmanOffer = input[2]
    salesmanDec = input[3]

    while(True):
        if sofiaBid >= salesmanOffer:
            return sofiaBid

        sofiaBid += sofiaInc

        if sofiaBid >= salesmanOffer:
            return salesmanOffer

        salesmanOffer -= salesmanDec


if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450
    assert checkio([150, 50, 900, 100]) == 400
    assert checkio([200, 100, 200, 100]) == 200
    assert checkio([500, 300, 700, 50]) == 700
