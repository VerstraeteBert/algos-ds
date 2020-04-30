def synoniemen(zin, woordenboek):
    nieuwe_zin = []
    zin = zin.split(" ")
    for woord in zin:
        if woord in woordenboek:
            nieuw_woord = woordenboek.get(woord)
            nieuwe_zin.append(nieuw_woord)
        else:
            nieuwe_zin.append(woord)
    return " ".join(nieuwe_zin)
            