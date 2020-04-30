def gift_inschrijven(tuple, woordenboek):
    klas, bedrag = tuple
    if klas in woordenboek:
        woordenboek[klas] += bedrag
    else:
        woordenboek[klas] = bedrag
    return woordenboek
