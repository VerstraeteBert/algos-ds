def synoniemen(zin, woordenboek):
    uitvoer = []
    for woord in zin.split():
        if woord in woordenboek:
            uitvoer.append(woordenboek[woord])
        else:
            uitvoer.append(woord)
    return " ".join(uitvoer)