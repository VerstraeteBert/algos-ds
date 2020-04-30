def isISBN_13(ISBN):
    if type(ISBN) != str:
        return False
    if not len(ISBN) == 13:
        return False
    if not ISBN.isdigit():
        return False
    if not ISBN[0:3] in ('978', '979'):
        return False

    som_even = 0
    som_oneven = 0
    even = ISBN[::2]
    oneven = ISBN[1::2]

    for i in range(6):
        cijfer = int(even[i])
        som_even += cijfer
        cijfer = int(oneven[i])
        som_oneven += cijfer

    x_c = (10 - (som_even + 3 * som_oneven) % 10) % 10

    return x_c == int(ISBN[12])


def overzicht(codes):
    groepen = {}
    for i in range(11):
        groepen[i] = 0
    
    for el in codes:
        if not isISBN_13(el):
            groepen[10] += 1
        else:
            groepen[int(el[3])] += 1
            
    print('Engelstalige landen: {}'.format(groepen[0] + groepen[1]))
    print('Franstalige landen: {}'.format(groepen[2]))
    print('Duitstalige landen: {}'.format(groepen[3]))
    print('Japan: {}'.format(groepen[4]))
    print('Russischtalige landen: {}'.format(groepen[5]))
    print('China: {}'.format(groepen[7]))
    print('Overige landen: {}'.format(groepen[6] + groepen[8] + groepen[9]))
    print('Fouten: {}'.format(groepen[10]))