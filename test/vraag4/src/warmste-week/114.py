def gift_inschrijven(klas_bedrag, alle_klassen):
    klas, bedrag = klas_bedrag
    if not klas in alle_klassen:
        alle_klassen[klas] = 0
    alle_klassen[klas] += bedrag
    return alle_klassen