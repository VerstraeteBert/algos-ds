def gift_inschrijven(tuple, woordenboek):
    woord = tuple[0]
    if woord in woordenboek:
        woordenboek[woord] += tuple[1]
    else:
        woordenboek[woord] = tuple[1]
    return woordenboek
