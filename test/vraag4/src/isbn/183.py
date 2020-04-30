def isISBN_13(code):
    if len(code) != 13:
        return False
        
    if code[:3] != "978" and code [:3] != "979":
        return False
    even = code[::2]
    oneven = code[1::2]
    someven = 0
    somoneven = 0
    for i in range(6):
        cijfer = int(even[i])
        someven += cijfer
        cijfer = int(oneven[i])
        somoneven += cijfer
    controle = (10-(someven + 3 * somoneven) %10)%10

    return controle == int(even[6])
    
    
def overzicht(codes):
    types = ["Engelstalige landen", "Franstalige landen", "Duitstalige landen", "Japan", "Russischtalige landen", "China", "Overige landen", "Fouten"]

    overzicht = {}

    for type in types:
        overzicht[type] = 0
    for code in codes:
        if not isISBN_13(code):
            overzicht["Fouten"] += 1
        else:
            nr = code[3]
            if nr == "0":
                nr = "1"
            elif nr in "689":
                nr = "7"
            elif nr == "7":
                nr = "6"
            type = types[int(nr)-1]
            overzicht[type] += 1

    for key in overzicht:
        print("{}: {}".format(key, overzicht[key]))

