def gift_inschrijven(gift,klassen):
    klas, bedrag = gift[:]
    if klas in klassen:
        klassen[klas] += bedrag
        return klassen
    else:
        klassen[klas] = bedrag
        return klassen