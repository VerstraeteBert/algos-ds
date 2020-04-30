def synoniemen(tekst, woordenboek):
    zin = []
    woorden = tekst.split()
    for woord in woorden:
        if woord in woordenboek:
            zin.append(woordenboek[woord])
        else:
            zin.append(woord)
    return " ".join(zin)