def isISBN(code):
    o = 0
    e = 0
    even = 0
    try:
        for i in range(0, len(code)-1):
            even += 1
            if even % 2 == 0:
                o += i
            else:
                e += i
        controle = (10-(o+3*e) % 10) % 10
        # print(controle)
        if code[-1] == 'X':
            code[-1] = 10
        if controle == int(code[-1]):
            return True
    except ValueError:
        return False
    return False


# print(isISBN('9789743159664'))


def overzicht(lijst):
    eng = []
    fr = []
    du = []
    jap = []
    ru = []
    chi = []
    over = []
    fouten = []
    for isbn in lijst:
        if isISBN(isbn) and (isbn[:3] == '978' or isbn[:3] == '979'):
            if isbn[3] == '0' or isbn[3] == '1':
                eng.append(isbn)
            elif isbn[3] == '2':
                fr.append(isbn)
            elif isbn[3] == '3':
                du.append(isbn)
            elif isbn[3] == '4':
                jap.append(isbn)
            elif isbn[3] == '5':
                ru.append(isbn)
            elif isbn[3] == '7':
                chi.append(isbn)
            elif isbn[3] == '6' or isbn[3] == '8' or isbn[3] == '9' :
                over.append(isbn)
        else:
            fouten.append(isbn)
    print('Engelstalige landen: {}'.format(len(eng)))
    print('Franstalige landen: {}'.format(len(fr)))
    print('Duitstalige landen: {}'.format(len(du)))
    print('Japan: {}'.format(len(jap)))
    print('Russischtalige landen: {}'.format(len(ru)))
    print('China: {}'.format(len(chi)))
    print('Overige landen: {}'.format(len(over)))
    print('Fouten: {}'.format(len(fouten)))
