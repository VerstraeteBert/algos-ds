def gift_inschrijven(tup, dic):
    if tup[0] in dic:
        dic[tup[0]] += tup[1]
    else:
        dic[tup[0]] = tup[1]
    return dic