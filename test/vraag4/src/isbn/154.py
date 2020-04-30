def isISBN_13(isbn):
    if not type(isbn) is str:
        return False
    if len(isbn) != 13:
        return False
    if not isbn.isdigit():
        return False
    if isbn[:3] not in {'978', '979'}:
        return False
    even = isbn[::2]
    oneven = isbn[1::2]
    som_even = 0
    som_oneven = 0
    for i in range(6):
        cijfer = int(even[i])
        som_even += cijfer
        cijfer = int(oneven[i])
        som_oneven += cijfer
    controle = (10 - (som_even + 3 * som_oneven) %10) %10

    return controle == int(isbn[12])

def overzicht(codes):
    groepen = {}
    for i in range(11):
        groepen[i] = 0

    for code in codes:
        if not isISBN_13(code):
            groepen[10] += 1
        else:
            groepen[int(code[3])] += 1

    print("Engelstalige landen: {}".format(groepen[0] + groepen[1]))
    print("Franstalige landen: {}".format(groepen[2]))
    print("Duitstalige landen: {}".format(groepen[3]))
    print("Japan: {}".format(groepen[4]))
    print("Russischtalige landen: {}".format(groepen[5]))
    print("China: {}".format(groepen[7]))
    print("Overige landen: {}".format(groepen[6] + groepen[8] + groepen[9]))
    print("Fouten: {}".format(groepen[10]))
