def synoniemen(tekst, woordenboek):
    woorden = []
    c = tekst.split
    for woord in tekst.split():
        if woord in woordenboek:
            woorden.append(woordenboek[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)
