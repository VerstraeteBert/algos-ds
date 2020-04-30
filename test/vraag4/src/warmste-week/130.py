def gift_inschrijven(x, y):
    if x[0] in y:
        a = y[x[0]]
        del y[x[0]]
        a = float(a) + float(x[1])
        y[x[0]] = a
    else:
        y[x[0]] = x[1]
    return y