
def isISBN(code):
    if code[:3] not in ['978', '979']:
        return False
    controle = 0
    for i in range(12):
        if i%2:
            controle += 3*int(code[i])
        else:
            controle += int(code[i])
    concijf = controle%10
    concijf = (10 - concijf)%10
    return concijf == int(code[-1])

def overzicht(codes):
    overzicht = {}
    for i in range(11):
        overzicht[i] = 0
    for code in codes:
        if not isISBN(code):
            overzicht[10] += 1
        else:
            overzicht[int(code[3])] += 1
    print('Engelstalige landen: {}'.format(overzicht[0]+overzicht[1]))
    print('Franstalige landen: {}'.format(overzicht[2]))
    print('Duitstalige landen: {}'.format(overzicht[3]))
    print('Japan: {}'.format(overzicht[4]))
    print('Russischtalige landen: {}'.format(overzicht[5]))
    print('China: {}'.format(overzicht[7]))
    print('Overige landen: {}'.format(overzicht[6]+overzicht[8]+overzicht[9]))
    print('Fouten: {}'.format(overzicht[10]))