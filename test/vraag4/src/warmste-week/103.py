def gift_inschrijven(gift, doelen):
    if gift[0] in doelen:
        doelen[gift[0]] += gift[1]
    else:
        doelen[gift[0]] = gift[1]
    
    return doelen