def gift_inschrijven(deel1, woordenboek):
    klas, bedrag = deel1
    if klas not in woordenboek:
        woordenboek[klas] = 0
    woordenboek[klas] += bedrag
    return woordenboek
