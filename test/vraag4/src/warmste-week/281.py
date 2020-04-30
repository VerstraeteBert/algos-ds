def gift_inschrijven(klas,w):
    klas=list(klas)
    if klas[0] in w:
        totaal=klas[1]+w[klas[0]]
    else:
        totaal = klas[1]
    w[klas[0]]=totaal
    return w