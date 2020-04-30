def gift_inschrijven(klas, d):
    if klas[0] in d:
        d[klas[0]]+=klas[1]
    else:
        d[klas[0]] = klas[1]
    return d