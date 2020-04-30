def isISBN_13(code):
    if len(code) != 13:
        return False
    if code[:3] != "978" and code[:3] != "979":
        return False
    e = code[::2]
    o = code[1::2]
    some = 0
    somo = 0
    for i in range(6):
        cijfer = int(e[i])
        some += cijfer
        cijfer = int(o[i])
        somo += cijfer
    controle = (10-(some + 3 * somo) % 10) % 10
    return controle == int(e[6])

def overzicht(codes):
    types = ["Engelstalige landen", "Franstalige landen", "Duitstalige landen", "Japan", "Russischtalige landen", "China", "Overige landen", "Fouten"]
    z = {}
    for type in types:
        z[type] = 0
    for code in codes:
        if not isISBN_13(code):
            z["Fouten"] += 1
        else:
            x = code[3]
            if x == "0":
                x = "1"  #engelstalig
            elif x == "7":
                x = "6" #China
            elif x in "689":
                x = "7" #Overige landen
            type = types[int(x)-1]
            z[type] += 1
    for a in z:
        print("{}: {}".format(a, z[a]))
