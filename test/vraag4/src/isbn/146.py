def is_ISBN(code):
    o = 0
    e = 0
    for i in range(0, 11, 2):
        o += int(code[i])
    for i in range(1, 12, 2):
        e += int(code[i])
    x13 = int(code[12])
    controle = (10 - (o + 3 * e) % 10) % 10
    if x13 == controle:
        return True
    return False
def is_europees(code):
    eerste_3_cijfers = code[0:3]
    if eerste_3_cijfers in ('978','979'):
        return True
    return False
def registratiegroep(code):
    vierde_cijfer = int(code[3])
    if vierde_cijfer in range(0, 2):
        registratiegroep = 'Engelstalige landen'
    elif vierde_cijfer == 2:
        registratiegroep = 'Franstalige landen'
    elif vierde_cijfer == 3:
        registratiegroep = 'Duitstalige landen'
    elif vierde_cijfer == 4:
        registratiegroep = 'Japan'
    elif vierde_cijfer == 5:
        registratiegroep = 'Russischtalige landen'
    elif vierde_cijfer == 7:
        registratiegroep = 'China'
    else:
        registratiegroep = 'Overige landen'
    return registratiegroep
def overzicht(codes):
    groepen = {'Engelstalige landen':0, 'Franstalige landen': 0, 'Duitstalige landen': 0, 'Japan': 0, 'Russischtalige landen': 0, 'China': 0, 'Overige landen': 0, 'Fouten': 0}
    for code in codes:
        if is_europees(code) and is_ISBN(code):
            groepen[registratiegroep(code)] += 1

        else:
            groepen['Fouten'] += 1
    for naam in groepen:
        print('{}: {}'.format(naam, groepen[naam]) )