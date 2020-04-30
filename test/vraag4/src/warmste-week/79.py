def gift_inschrijven(tup, dic):
    klas, bedrag = tup
    if klas in dic:
        dic[klas] += bedrag
    else:
        dic[klas] = bedrag
    return dic