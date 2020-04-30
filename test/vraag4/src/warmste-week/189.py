def gift_inschrijven(tu, di):
    if tu[0] in di:
        di[tu[0]] += tu[1]
    else:
        di[tu[0]] = tu[1]
    return di