def synoniemen(tekst, woordenboek):
    zin = []
    for woord in tekst.split():
        if woord in woordenboek:
            zin.append( woordenboek[woord])
        else: zin.append(woord)
    return " ".join(zin)