def gift_inschrijven(tup, d):
    if tup[0] in d.keys():
        waarde = d.get(tup[0])
        waarde += tup[1]
        d[tup[0]] = waarde
    else:
        d.update({tup[0]:tup[1]})
    return d