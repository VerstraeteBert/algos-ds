def gift_inschrijven(tuple,dictionary):
    try:
        klas = tuple[0]
        bedrag = tuple[1]
        dictionary[klas] = dictionary[klas] + bedrag
    except KeyError:
        dictionary[klas] = bedrag
    return dictionary