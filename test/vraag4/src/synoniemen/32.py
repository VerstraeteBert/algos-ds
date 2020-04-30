def synoniemen(tekst, woordenboek):
    zin2 = []
    tekst = tekst.split(' ')
    for woord in tekst:
        if woord in woordenboek:
            zin2.append(str(woordenboek[woord]))
        else:
            zin2.append(woord)
    zin2 = (' ').join(zin2)
    return zin2
