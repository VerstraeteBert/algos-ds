def gift_inschrijven(gift, opbrengst):
    if gift[0] in opbrengst:
        opbrengst[gift[0]] += gift[1]
    else:
        opbrengst[gift[0]] = gift[1]
    return opbrengst