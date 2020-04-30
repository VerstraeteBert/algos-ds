def isISBN_13(code):
    if len(code) != 13:
        return False
    if code[:3] != "978" and code[:3] != "979":
        return False
    even = code[::2]
    oneven = code[1::2]
    even_som = 0
    oneven_som = 0
    for i in range(6):
        cijfer = int(even[i])
        even_som += cijfer
        cijfer = int(oneven[i])
        oneven_som += cijfer
    controle = (10 - (even_som + 3 * oneven_som) % 10) % 10
    return controle == int(even[6])


def overzicht(codes):
    types = ["Engelstalige landen", "Franstalige landen", "Duitstalige landen", "Japan", "Russischtalige landen",
             "China", "Overige landen", "Fouten"]
    lijst = {}
    for soort in types:
        lijst[soort] = 0
    for code in codes:
        if not isISBN_13(code):
            lijst["Fouten"] += 1
        else:
            nr = code[3]
            if nr == "0":
                nr = "1"
            elif nr in "689":
                nr = "7"
            elif nr == "7":
                nr = "6"
            soort = types[int(nr) - 1]
            lijst[soort] += 1
    for el in lijst:
        print("{}: {}".format(el, lijst[el]))
