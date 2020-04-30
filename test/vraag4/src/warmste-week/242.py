#oefeningen dictionaries
def gift_inschrijven(tuple, dic):
    klas , bedrag = tuple
    if klas in dic:
        dic[klas] += bedrag
    if klas not in dic:
        dic[klas] = bedrag
    return dic