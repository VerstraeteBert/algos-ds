def isISBN_13(code):
    oneven =0
    even = 0
    if not type(code) is str:
        return False
    if len(code) != 13:
        return False
    for cijfer in code:
        if cijfer not in "0123456789":
            return False
    for i in range(0,11,2):
        even += int(code[i+1])
        oneven += int(code[i])
    controlecijfer = int(code[12])
    return controlecijfer == ((10-(oneven+3*even)%10)%10)

def overzicht(codes):
    fouten = 0
    Engels = 0
    frans = 0
    duits = 0
    japan = 0
    rus = 0
    china = 0
    overig = 0
    for element in codes:
        resultaat = isISBN_13(element)
        if ((element[:3] == '978') or (element[:3]== '979')) and (resultaat == True):
            if element[3] in '01':
                Engels += 1
            if element[3] == '2':
                frans += 1
            if element[3] == '3':
                duits += 1
            if element[3] == '4':
                japan += 1
            if element[3] == '5':
                rus += 1
            if element[3] == '7':
                china += 1
            if element[3] in '689':
                overig += 1
        else:
            fouten += 1
    print("Engelstalige landen: {}".format(Engels))
    print("Franstalige landen: {}".format(frans))
    print("Duitstalige landen: {}".format(duits))
    print("Japan: {}".format(japan))
    print("Russischtalige landen: {}".format(rus))
    print("China: {}".format(china))
    print("Overige landen: {}".format(overig))
    print("Fouten: {}".format(fouten))