def gift_inschrijven(t, w):
    if t[0] in w:
        w[t[0]] += t[1]
    else:
        w[t[0]] = t[1]
    return w