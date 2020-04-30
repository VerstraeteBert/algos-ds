def isISBN_13(code):
    if len(code) != 13:
        return False
    if code[:3] != "978" and code [:3] != "979":
        return False
    someven = 0
    somoneven = 0
    for i in range(0, 12, 2):
        someven += int(code[i])
        somoneven += int(code[i+1])
    controle = (10-(someven + 3 * somoneven) %10)%10
    return controle == int(code[12])

def overzicht(codes):
    types = {"0": "Engelstalige landen", "1": "Engelstalige landen",
             "2": "Franstalige landen", "3": "Duitstalige landen",
             "4": "Japan", "5": "Russischtalige landen",
             "7": "China", "6": "Overige landen", 
             "8": "Overige landen", "9": "Overige landen"}
    isbn = {}
    for type in types.values():
        isbn[type] = 0
    isbn["Fouten"] = 0
    for code in codes:
        if not isISBN_13(code):
            isbn["Fouten"] += 1
        else:
            isbn[types[code[3]]] += 1
    for key in isbn:
        print(key+":", isbn[key])
