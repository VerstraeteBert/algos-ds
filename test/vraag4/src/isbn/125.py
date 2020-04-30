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
    land_codes = {"0" : "Engelstalige landen", "1" : "Engelstalige landen", "2" : "Franstalige landen",  \
    "3": "Duitstalige landen", "4": "Japan", "5": "Russischtalige landen", "7": "China", "6": "Overige landen", \
    "8": "Overige landen", "9": "Overige landen"}
    foutief = "Fouten"
    overzicht = {}
    for landtype in land_codes.values():
        overzicht[landtype] = 0
    overzicht[foutief] = 0
    for code in codes:
        if isISBN_13(code):
            overzicht[land_codes[code[3]]] += 1
        else:
            overzicht[foutief] += 1
    for landtype, aantal in overzicht.items():
        print("{}: {}".format(landtype, aantal))
        
    
