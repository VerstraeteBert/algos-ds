def synoniemen(tekst, woordenboek):
    woorden = []
    for woord in tekst.strip().split():
        if woord in woordenboek:
            woorden.append(woordenboek[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)

