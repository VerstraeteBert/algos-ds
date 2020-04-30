def synoniemen(zin, woordenlijst):
    zin_lijst = zin.strip().split()
    string = ""
    for woord in zin_lijst:
        if woord in woordenlijst:
            string += str(woordenlijst[woord])
            string += " "
        else:
            string += woord
            string += " "
    return string.strip()
