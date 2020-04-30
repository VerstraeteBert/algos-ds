def gift_inschrijven(tup, dict):
    klas1 = tup[0]
    bedrag = float(tup[1])
    if klas1 in dict:
        dict[klas1] = float(dict[klas1]) + bedrag
    else:
        dict[tup[0]] = bedrag
    return dict