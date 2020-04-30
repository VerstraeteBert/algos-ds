def synoniemen(zin, woordenboek):
    woorden = []
    for woord in zin.split():
        if woord in woordenboek:
            woorden.append(woordenboek[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)