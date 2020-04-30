def synoniemen(tekst,syn):
    woorden = []
    for woord in tekst.split():
        if woord in syn:
            woorden.append(syn[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)