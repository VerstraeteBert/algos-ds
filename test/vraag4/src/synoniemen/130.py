def synoniemen(zin, woordenboek):
    zin = zin.split(" ")
    nieuwe_zin = []
    for woord in zin:
        if woord in woordenboek:
            nieuwe_zin.append(woordenboek[woord])
        else:
            nieuwe_zin.append(woord)
    return " ".join(nieuwe_zin)