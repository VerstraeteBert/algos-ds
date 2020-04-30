def gift_inschrijven(x,y):
    klas, bedrag = x
    if klas in y.keys():
        y[klas] += bedrag
    else:
        y[klas] = bedrag
    return y