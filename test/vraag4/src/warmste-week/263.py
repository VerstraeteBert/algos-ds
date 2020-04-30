def gift_inschrijven(tup, dicti):
    i = 0
    for naam, val in dicti.items():
        if tup[0] == naam:
            dicti[naam] += tup[1]
            i += 1
    if i == 0:
        dicti[tup[0]] = tup[1]
    return dicti