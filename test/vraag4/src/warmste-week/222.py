def gift_inschrijven(t, d):
    if t[0] in d:
        d[t[0]] += t[1]
    else:
        d[t[0]]=t[1]
    return d