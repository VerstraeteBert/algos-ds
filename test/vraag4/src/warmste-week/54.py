def gift_inschrijven(giften, klassen):
    klas, bedrag = giften
    if klas in klassen:
        klassen[klas] += bedrag
    else:
        klassen[klas] = bedrag
    return klassen