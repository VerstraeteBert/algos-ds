def gift_inschrijven(klas,klassen):
    try:
        klas1, geld1 = klas[0], klas[1]
        geld2 = klassen[klas1]
        som = geld1 + geld2
        klassen[klas1] = som
        return klassen
    except KeyError:
        klassen[klas1] = geld1
        return klassen