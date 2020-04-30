def gift_inschrijven(tuple,dict):
    klas = tuple[0]
    bedrag = tuple[1]
    try:
        bedrag2 = dict[klas] + bedrag
        dict[klas] = bedrag2
    except KeyError:
        dict[klas] = bedrag
    return dict