def synoniemen(zin, dictionary):
    woordenlijst = zin.split()
    i = 0
    for woord in woordenlijst:
        if woord in dictionary:
            woord = dictionary[woord]
            woordenlijst[i] = woord
        i += 1
    return " ".join(woordenlijst)