def synoniemen(zin, dictionary):
    nieuwe_zin = ""
    woordenlijst = zin.split()
    for woord in woordenlijst:
        if woord in dictionary:
            nieuwe_zin += dictionary[woord] + ' '
        else:
            nieuwe_zin += woord + ' '
    return nieuwe_zin.strip()