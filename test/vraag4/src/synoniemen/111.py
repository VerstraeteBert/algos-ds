def synoniemen(zin, woordenboek):
    nieuwe_zin = []
    woorden = zin.split(" ")
    for woord in woorden:
        if woord in woordenboek:
            nieuwe_zin.append(woordenboek[woord])
        else:
            nieuwe_zin.append(woord)
    return " ".join(nieuwe_zin)