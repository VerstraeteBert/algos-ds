def gift_inschrijven(t,d):
    klas = t[0]
    gift = t[1]
    if klas in d:
        d[klas] += gift
    else:
        d[klas] = gift
    return d


