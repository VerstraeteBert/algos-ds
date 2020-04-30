def gift_inschrijven(tup, dic):
    klas, geld = tup
    if not klas in dic:
        dic[klas] = 0
    dic[klas] += geld
    return dic
        