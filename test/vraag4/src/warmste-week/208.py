def gift_inschrijven(tup, dict):
    if tup[0] in dict.keys():
        dict[tup[0]] += tup[1]
    if tup[0] not in dict.keys():
        dict[tup[0]] = tup[1]
    return dict