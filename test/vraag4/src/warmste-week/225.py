def gift_inschrijven(klas, alle_klassen):
    if klas[0] in alle_klassen:
        alle_klassen[klas[0]] += klas[1]
    else:
        alle_klassen[klas[0]] = klas[1]
    return alle_klassen
    