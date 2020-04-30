def gift_inschrijven(tuple,dic):
    klas, bed = tuple
    if not klas in dic:
        dic[klas] = 0
    dic[klas] += bed
    return dic