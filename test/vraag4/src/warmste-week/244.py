def gift_inschrijven(tup, dic):
    klas = tup[0]
    bedrag = tup[1]
    if klas in dic:
        dic[klas] += bedrag
    elif klas not in dic:
        dic[klas] = bedrag
    return dic