def gift_inschrijven(tup, giften):
    if tup[0] in giften:
        giften[tup[0]] += tup[1]
    else:
        giften[tup[0]] = tup[1]
    return giften