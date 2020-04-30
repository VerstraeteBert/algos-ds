def gift_inschrijven(tuple,woordenboek):
    if tuple[0] in woordenboek:
        woordenboek[tuple[0]] += tuple[1]
    if tuple[0] not in woordenboek:
        woordenboek[tuple[0]] = tuple[1]
    return woordenboek