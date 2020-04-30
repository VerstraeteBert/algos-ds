def gift_inschrijven(tuple, woordenboek):
    if tuple[0] in woordenboek:
        woordenboek[tuple[0]] += tuple[1]
    else:
        woordenboek[tuple[0]] = tuple[1]
    return woordenboek