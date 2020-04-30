def isISBN13(code):
    if not (isinstance(code, str) and   # code moet een string zijn
        len(code) == 13 and         # code moet bestaan uit 10 karakters
        code.isdigit()              # eerste 9 karakters moeten cijfers zijn
    ):
        return False
    if code[:3] not in {'978', '979'}:
        return False                # prefix vd gegeven code controleren
    controle = 0
    for i in range(12):             # controlecijfer berekenen
        if i%2:
            controle += 3* int(code[i])
        else:
            controle += int(code[i])
    controlecijf = controle %10
    controlecijf = (10 - controlecijf) %10
    return controlecijf == int(code[-1])

def overzicht(codes):
    groepen = {}                    # dictionary initialiseren
    for i in range(11):
        groepen[i] = 0
    for code in codes:
        if not isISBN13(code):
            groepen[10] += 1
        else:
            groepen[int(code[3])] += 1
    #samenvating uitschrijven
    print('Engelstalige landen: {}'.format(groepen[0] + groepen[1]))
    print('Franstalige landen: {}'.format(groepen[2]))
    print('Duitstalige landen: {}'.format(groepen[3]))
    print('Japan: {}'.format(groepen[4]))
    print('Russischtalige landen: {}'.format(groepen[5]))
    print('China: {}'.format(groepen[7]))
    print('Overige landen: {}'.format(groepen[6] + groepen[8] + groepen[9]))
    print('Fouten: {}'.format(groepen[10]))