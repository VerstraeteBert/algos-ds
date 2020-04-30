def gift_inschrijven(klbe, woordenboek):
    klas, bedrag = klbe
    if klas in woordenboek:
        woordenboek[klas] += bedrag
    else:
        woordenboek[klas] = bedrag
    return woordenboek