def gift_inschrijven(tup, dictionary):
    naam = tup[0]
    bedrag = tup[1]
    if naam in dictionary:
        dictionary[naam] += bedrag
    else:
        dictionary[naam] = bedrag
    return dictionary