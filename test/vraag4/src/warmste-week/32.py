def gift_inschrijven(tuple, dictionary):
    klas, bedrag = tuple
    if not klas in dictionary:
        dictionary[klas] = 0
    dictionary[klas] += bedrag
    return dictionary