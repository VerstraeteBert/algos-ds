def gift_inschrijven(tup, dict):
    klas = tup[0]
    bedrag = tup[1]
    if klas in dict:
        dict[klas] += bedrag
    else:
        dict[klas] = bedrag
    return dict

