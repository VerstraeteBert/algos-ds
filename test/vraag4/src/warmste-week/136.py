def gift_inschrijven(gift, bibl):
    if gift[0] in bibl:
        bibl[gift[0]] += gift[1]
    else:
        bibl[gift[0]] = gift[1]
    return bibl
