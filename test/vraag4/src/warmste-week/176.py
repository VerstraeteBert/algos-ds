def gift_inschrijven(x, y):
    a = x[0]
    b = x[1]
    if a in y:
        y[a] += b
    if a not in y:
        y[a] = b
    return y