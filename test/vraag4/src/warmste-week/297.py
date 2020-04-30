def gift_inschrijven(tup, dic):
    klas, gift = tup
    if klas in dic:
        dic[klas] += gift
    else:
        dic[klas] = gift
    return dic