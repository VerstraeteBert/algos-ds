def synoniemen(tekst,dictionary):
    woorden = []
    for woord in tekst.split():
        if woord in dictionary:
            woorden.append(dictionary[woord])
        else:
            woorden.append(woord)
    return " ".join(woorden)      