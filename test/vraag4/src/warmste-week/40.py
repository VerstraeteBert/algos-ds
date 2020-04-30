def gift_inschrijven(sponsering, woordenboek):
    klas, bedrag = sponsering
    if not klas in woordenboek:
        woordenboek[klas] = 0
    woordenboek[klas] += bedrag
    return woordenboek