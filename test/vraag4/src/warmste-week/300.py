def gift_inschrijven(tuple, dictionary):
    bedrag = tuple[1]
    klas = tuple[0]
    if klas in dictionary:
        dictionary[klas] += bedrag
    else:
        dictionary[klas] = bedrag
    return dictionary

