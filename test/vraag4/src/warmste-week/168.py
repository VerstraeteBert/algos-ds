def gift_inschrijven(sponsoring, dictionary):
    klas, bedrag = sponsoring
    if klas in dictionary:
        dictionary[klas] += bedrag
    else:
        dictionary[klas] = bedrag
    return dictionary