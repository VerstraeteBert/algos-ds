def isISBN13(code):
    if not type(code) is str:
        return False
    if len(code) != 13:
        return False
    if not code.isdigit():
        return False
    if code[:3] not in '978' or '979':
        return False
    for i in range(12):
        if i % 2:
            controle += 3 * int(code[i])
        else:
            controle += int(code[i])
    controlecijfer = controle % 10
    controlecijfer = (10 - controlecijfer) % 10
    return controlecijfer == int(code[-1])

def overzicht(codes):
    types = ["Engelstalige landen", "Franstalige landen", "Duitstalige landen", "Japan", "Russischtalige landen", "China", "Overige landen", "Fouten"]
    overzicht = {}
    for type in types:
        overzicht[type] = 0
    for code in codes:
        if not isISBN13(code):
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

