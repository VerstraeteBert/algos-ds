def gift_inschrijven(t, dic):
    a, b = t
    if a in dic:
        dic[a] += b
    else:
        dic[a] = b
    return dic