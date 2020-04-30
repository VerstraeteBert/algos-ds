def synoniemen(zin, woordenboek):
    woorden = zin.split(" ")
    nieuwe_zin = []
    for woord in woorden:
        if woord in woordenboek:
            nieuw_woord = woordenboek[woord]
            nieuwe_zin.append(nieuw_woord)
        else:
            nieuwe_zin.append(woord)
    nieuwe_zin = " ".join(nieuwe_zin)
    return nieuwe_zin
    