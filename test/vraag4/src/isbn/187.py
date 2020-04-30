def isISBN_13(code):
    if code[:3] not in {'978', '979'}:
        return False
    o = 0
    e = 0
    for i in range(0, 6):
        try:
            o += int(code[2*i])
            e += int(code[2*i + 1])
        except ValueError:
            return False
        except TypeError:
            return False
    controle = (10 - (o + 3*e) % 10) % 10
    if str(controle) == code[-1]:
        return True
    return False
def overzicht(lijst):
    overzicht = {}
    for i in range(11):
        overzicht[i] = 0
    for code in lijst:
        if isISBN_13(code):
            overzicht[int(code[3])] += 1
        else:
            overzicht[10] += 1
    print('Engelstalige landen: {}'.format(overzicht[0] + overzicht[1]))
    print('Franstalige landen: {}'.format(overzicht[2]))
    print('Duitstalige landen: {}'.format(overzicht[3]))
    print('Japan: {}'.format(overzicht[4]))
    print('Russischtalige landen: {}'.format(overzicht[5]))
    print('China: {}'.format(overzicht[7]))
    print('Overige landen: {}'.format(overzicht[6] + overzicht[8] + overzicht[9]))
    print('Fouten: {}'.format(overzicht[10]))