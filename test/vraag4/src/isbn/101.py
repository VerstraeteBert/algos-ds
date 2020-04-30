def isISBN_13(isbn):
    if not (isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()):
        return False
    if isbn[:3] not in {'978', '979'}:
        return False
    controle = 0
    for i in range(12):
        if i % 2:
            controle += 3* int(isbn[i])
        else:
            controle += int(isbn[i])
    controlecijfer = controle % 10
    controlecijfer = (10 - controlecijfer) % 10
    return controlecijfer == int(isbn[-1])

def overzicht(codes):
    groepen = {}
    for i in range(11):
        groepen[i] = 0
    for isbn in codes:
        if not isISBN_13(isbn):
            groepen[10] += 1
        else:
            groepen[int(isbn[3])] += 1
    print('Engelstalige landen: {}'.format(groepen[0] + groepen[1]))
    print('Franstalige landen: {}'.format(groepen[2]))
    print('Duitstalige landen: {}'.format(groepen[3]))
    print('Japan: {}'.format(groepen[4]))
    print('Russischtalige landen: {}'.format(groepen[5]))
    print('China: {}'.format(groepen[7]))
    print('Overige landen: {}'.format(groepen[6] + groepen[8] + groepen[9]))
    print('Fouten: {}'.format(groepen[10]))