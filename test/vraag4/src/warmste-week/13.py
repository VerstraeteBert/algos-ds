def gift_inschrijven(tuple, dictionary):
    klas, bedrag = tuple[0:]
    try:
        if klas in dictionary:
            dictionary[klas] += bedrag
        else:
            dictionary[klas] = bedrag
    except KeyError:
        dictionary[klas] = bedrag
    return dictionary
