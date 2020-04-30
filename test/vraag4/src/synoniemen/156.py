def synoniemen(tekst, synoniemen):
    woorden = []
    for woord in tekst.split():
        if woord in synoniemen:
            woorden.append(synoniemen[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)
    