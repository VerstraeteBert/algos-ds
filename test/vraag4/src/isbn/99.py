def isISBN_13(isbn):
    o = 0
    e = 0
    if not type(isbn) == str:
        return False
    for a in range(0,11,2):
        if isbn[a].isalpha():
            return False
        o = o + int(isbn[a])
    for b in range(1,12,2):
        if isbn[b].isalpha():
            return False
        e = e + int(isbn[b])
    som = (10 - (o + 3 * e) % 10) % 10
    if isbn[12] == "X":
        d = 10
    else:
        d = int(isbn[12])
    return d == som


def overzicht(code):
    tabel = {}
    types = ["Engelstalige landen", "Franstalige landen", "Duitstalige landen", "Japan", "Russischtalige landen", "China", "Overige landen", "Fouten"]
    for a in types:
        tabel[a] = 0
    for i in code:
        if not isISBN_13(i) or i[:3] not in ["978", "979"]:
            tabel["Fouten"] += 1
            continue
        nr = i[3]
        if nr in "01":
            nummer = 1
        elif nr == "7":
            nummer = 6
        elif nr in "689":
            nummer = 7
        else:
            nummer = int(nr)
        tabel[types[nummer - 1]] += 1

    for o in types:
        print(o, ": ", tabel[o], sep="")
