def isISBN_13(code):
    if type(code) is not str:
        return False
    if len(code) != 13:
        return False
    try:
        oneven = 0
        i = 0
        while i < 11:
            oneven += int(code[i])
            i += 2
        even = 0
        i = 1
        while i < 12:
            even += int(code[i])
            i += 2
        if int(code[12]) == (10-(oneven + 3*even)%10)%10:
            return True
        return False
    except ValueError:
        return False

def overzicht(lijst):
    f = 0
    en = 0
    fr = 0
    ru = 0
    du = 0
    ch = 0
    jap = 0
    ov = 0
    for el in lijst:
        if not isISBN_13(el):
            f += 1
        elif int(el[0:3]) != 978 and int(el[0:3]) != 979:
            f += 1
        else:
            land = int(el[3])
            if land == 0 or land == 1:
                en += 1
            elif land == 2:
                fr += 1
            elif land == 3:
                du += 1
            elif land == 4:
                jap += 1
            elif land == 5:
                ru += 1
            elif land == 7:
                ch += 1
            else:
                ov += 1
    print('Engelstalige landen:', en)
    print('Franstalige landen:', fr)
    print('Duitstalige landen:', du)
    print('Japan:', jap)
    print('Russischtalige landen:', ru)
    print('China:', ch)
    print('Overige landen:', ov)
    print('Fouten:', f)