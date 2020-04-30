def isISBN_13(code):
    if len(code) != 13:
        return False

    if code[:3] != "978" and code[:3] != "979":
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
    controle = (10 - (someven + 3 * somoneven) % 10) % 10

    return controle == int(even[6])

def overzicht(lijst_codes):
    landen = {"Engelstalige landen:": 0, "Franstalige landen:": 0, "Duitstalige landen:": 0, "Japan:": 0, "Russischtalige landen:": 0, "China:": 0, "Overige landen:": 0, "Fouten:": 0}
    for code in lijst_codes:
        if (code[0:3] == "978" or code[0:3] == "979") and isISBN_13(code):
            nummer_land = int(code[3])
            if nummer_land == 0 or nummer_land == 1:
                landen["Engelstalige landen:"] += 1
            elif nummer_land == 2:
                landen["Franstalige landen:"] += 1
            elif nummer_land == 3:
                landen["Duitstalige landen:"] += 1
            elif nummer_land == 4:
                landen["Japan:"] += 1
            elif nummer_land == 5:
                landen["Russischtalige landen:"] += 1
            elif nummer_land == 7:
                landen["China:"] += 1
            else:
                landen["Overige landen:"] += 1
        else:
            landen["Fouten:"] += 1
    for element in landen:
        print(element, landen[element])
    return